#include <kilombo.h>
#include "coverage.h"


REGISTER_USERDATA(USERDATA)



void update_from_message(){
  /*
Mise à jour de la liste des voisins en fonction du message recu
  ->ajout dans la liste s'il n esite pas
  ->mise à jour des parametres si il est déjà dans la liste
  */
  uint8_t ID=mydata->messagerx.data[0];
  //DEFINIR ID A PARTIR DU MESSAGE
  uint8_t found=0;
  uint8_t i=0;
  printf("        message from %d\n", ID);
  while(i<mydata->nb_voisins && found==0){
    if (mydata->voisins_liste[i].id==ID){
      found=1;
      printf("        deja dans la liste\n");
    }else{
      i++;
    }
  }
  if (found==0){
    if (mydata->nb_voisins<MAXVOISIN){
      mydata->nb_voisins++;
    }
  }
  mydata->voisins_liste[i].id=ID;
  mydata->voisins_liste[i].timestamp=kilo_ticks;
  mydata->voisins_liste[i].dist=mydata->distance;
  printf("mise a jour : id : %d time : %d distace : %d\n", mydata->voisins_liste[i].id,mydata->voisins_liste[i].timestamp,mydata->voisins_liste[i].dist);
  mydata->distance=-1;

}

void update_voisins(){
  /*
Mise à jour de la liste des voisins tenu par le kilobot
->on enleve un voisin si on a pas recu de message de lui depuis plus de 2 secondes
  */
  printf("    update_voisins\n");
  if (mydata->nb_voisins==0){
    printf("        pas de voisins\n");
    return ;
  }
      int8_t i;

      for (i = mydata->nb_voisins-1; i >= 0; i--){
        printf("        liste : id: %d time: %d dist : %d \n",mydata->voisins_liste[i].id,mydata->voisins_liste[i].timestamp,mydata->voisins_liste[i].dist );
          if (kilo_ticks - mydata->voisins_liste[i].timestamp  > 2*SECONDE){  //this one is too old.
            printf("kiloticks %d\n",kilo_ticks );
            printf("        delete voisin %d\n", mydata->voisins_liste[i].id);
              mydata->voisins_liste[i]= mydata->voisins_liste[mydata->nb_voisins];
              mydata->voisins_liste[mydata->nb_voisins-1].id=-1;
              mydata->nb_voisins--;
            }
      }
}

void update_motors(uint8_t direction) {
/*
Update des moteurs
*/
    if (direction != mydata->previous_dir) {
        switch(direction) {
            case STRAIGHT:
                spinup_motors();
                set_motors(kilo_straight_left, kilo_straight_right);
                break;
            case LEFT:
                spinup_motors();
                set_motors(kilo_turn_left,0);
                break;
            case RIGHT:
                spinup_motors();
                set_motors(0,kilo_turn_right);
                break;
            case STOP:
            default:
                set_motors(0,0);
                break;
        }
        mydata->previous_dir = direction;
      }
}
message_t *message_tx()
{
    return &mydata->messagetx;
}

void message_rx(message_t *message, distance_measurement_t *d)
{
    mydata->messagerx= *message;
    mydata->distance= estimate_distance(d);
    mydata->new_message = 1;
}

void setup(){
  /*
Initialisation des variables globales et du message envoyé.
  */
    printf("setup\n");
    printf("%d\n",kilo_uid );
    // Initialize message:
    mydata->messagetx.type = NORMAL;
    mydata->messagetx.data[0]=kilo_uid;
    mydata->messagetx.crc = message_crc(&mydata->messagetx);
    mydata->previous_dir=STOP;
    mydata->nb_voisins=0;
    mydata->last_update=kilo_ticks;
    mydata->next_direction=STOP;
    mydata->new_message=0;
    mydata->distance=-1;
    mydata->nb=1;
}

uint8_t tooClose(){
  /*
Retourne 1 si tous les voisins sont trop pres (macro ASK)
Retourne 0 sinon
  */
  uint8_t i;
  uint8_t stop=0;
  for(i=0;i<mydata->nb_voisins;i++){
    if (mydata->voisins_liste[i].dist<ASK){
      stop=1;
    }
  }
  printf("tooClose %d\n",stop );
  return stop;
}

void loop(){
/*
Traitement des messages
décide des comportement en fontion du nombre de voisin ou de tooClose()
*/

  //si un message est arrivé,le traiter
  if (mydata->new_message == 1)
  {
    printf("    Nouveau message\n");
    update_from_message();
    mydata->new_message=0;
  }
  //possible changement de direction toute les secondes
    if (kilo_ticks>mydata->last_update+mydata->nb*SECONDE) {
      mydata->next_direction=(rand_hard()%3)+1;
      mydata->last_update=kilo_ticks;
    }
    printf("----------------------------------");
    printf("loop\n");
    printf("    mydata->nb_voisins%d\n",mydata->nb_voisins );
    update_voisins(); //met a jour la liste de ses voisins

    if (tooClose() || mydata->nb_voisins==0){
      if(mydata->next_direction!=STOP){
        mydata->nb=1;
      }
      printf("    tooclose or new voisins\n");
      update_motors(mydata->next_direction);//randomdirection
      set_color(RGB(1,0,0));
    }else{
      mydata->nb=2;
      printf("    perfect mydata->distance\n");
      update_motors(STOP);
      mydata->next_direction=STOP;
      set_color(RGB(1,1,1));
    }
}


int main()
{
/*
Initialise callback et lance la main loop
*/
    kilo_init();
    // Register the message_rx & message_tx callback function.
    kilo_message_rx = message_rx;
    kilo_message_tx=message_tx;
    //start loop
    kilo_start(setup, loop);

    return 0;
}