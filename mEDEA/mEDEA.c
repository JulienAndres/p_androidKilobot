#include <kilombo.h>
#include "mEDEA.h"


REGISTER_USERDATA(USERDATA)

void update_liste_genome(){
  return;
}

void emission(){
	// Blink the LED magenta whenever a message is sent.
  if (kilo_uid==0) set_color(RGB(0,0,1));
  if (kilo_uid==1) set_color(RGB(0,1,0));
}

void update_from_message(){
  /*
Mise à jour de la liste des voisins en fonction du message recu
  ->ajout dans la liste s'il n esite pas
  ->mise à jour des parametres si il est déjà dans la liste
  */
  if (mydata->messagerx.data[1]){
    return update_blocs();
  }
  update_liste_genome();
  uint8_t ID=mydata->messagerx.data[0];
  //DEFINIR ID A PARTIR DU MESSAGE
  uint8_t found=0;
  uint8_t i=0;
  //printf("        message from %d\n", ID);
  while(i<mydata->nb_voisins && found==0){
    if (mydata->voisins_liste[i].id==ID){
      found=1;
      //printf("        deja dans la liste\n");
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
  mydata->distance=-1;

}

void update_blocs(){
  uint8_t found=0;
  uint8_t i=0;
  uint8_t ID=mydata->messagerx.data[0];

  if (mydata->messagerx.data[1]==1){ //si c est un bloc répulsion
    while (i< mydata->nb_repuls && found ==0){
      if (mydata->liste_blocs_repuls[i].id==ID){
        found=1;
      }else{
        i++;
      }
    }
    if (!found){
      if (mydata->nb_repuls<MAXBLOCK){
        mydata->nb_repuls++;
      }
    }

    mydata->liste_blocs_repuls[i].id=ID;
    mydata->liste_blocs_repuls[i].timestamp=kilo_ticks;
    mydata->liste_blocs_repuls[i].dist=mydata->distance;

  }else if (mydata->messagerx.data[1]==2){//si c est un bloc attraction

    while (i< mydata->nb_attract && found ==0){
      if (mydata->liste_blocs_attract[i].id==ID){
        found=1;
      }else{
        i++;
      }
    }
    if (!found){
      if (mydata->nb_attract<MAXBLOCK){
        mydata->nb_attract++;
      }
    }

    mydata->liste_blocs_attract[i].id=ID;
    mydata->liste_blocs_attract[i].timestamp=kilo_ticks;
    mydata->liste_blocs_attract[i].dist=mydata->distance;
  }
  return;
}

void update_world(){
  int cpt_voisin=0;
  int i;
  for (i = 0; i < mydata->nb_voisins; i++) {
    cpt_voisin+=mydata->voisins_liste[i].dist;
  }
  int cpt_repuls=0;
  for (i=0; i< mydata->nb_repuls;i++){
    cpt_repuls+=mydata->liste_blocs_repuls[i].dist;
  }
  int cpt_attract=0;
  for(i=0; i< mydata->nb_attract;i++){
    cpt_attract+=mydata->liste_blocs_attract[i].dist;
  }
  mydata->world[0]=(mydata->nb_voisins) ? cpt_voisin/mydata->nb_voisins : 0 ; //moyenne des distances de ses voisins
  mydata->world[1]=(mydata->nb_repuls) ? cpt_repuls/mydata->nb_repuls : 0 ; //moyenne des distances des blocks répulsions
  mydata->world[2]=(mydata->nb_attract) ? cpt_attract/mydata->nb_attract : 0; //moyenne des distances des blocks attractions;
  mydata->world[3]=get_ambientlight(); //niveau de luminosité actuelle
  mydata->world[4]=1;
}
void update_voisins(){
  /*
Mise à jour de la liste des voisins tenu par le kilobot
->on enleve un voisin si on a pas recu de message de lui depuis plus de 2 secondes
  */
  //printf("    update_voisins\n");
  if (mydata->nb_voisins==0){
    //printf("        pas de voisins\n");
    mydata->world[0]=0;//maj genome avec distance moyenne voisins
    return ;
  }
      int i;

      for (i = mydata->nb_voisins-1; i >= 0; i--){
          if (kilo_ticks - mydata->voisins_liste[i].timestamp  > 2*SECONDE){  //this one is too old.
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
    if (kilo_uid==0){
      mydata->messagetx.data[1]=1; //1=expulsion
      mydata->messagetx.crc = message_crc(&mydata->messagetx);

    }
    else if (kilo_uid==1){
      mydata->messagetx.data[1]=2; //2=attraction
      mydata->messagetx.crc = message_crc(&mydata->messagetx);

    }
    return &mydata->messagetx;
}

void majmessage(){
  return;
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
    //printf("setup\n");
    //printf("%d\n",kilo_uid );
    // Initialize message:
    mydata->messagetx.type = NORMAL;
    mydata->messagetx.data[0]=kilo_uid;
    mydata->messagetx.data[1]=0;
    mydata->messagetx.crc = message_crc(&mydata->messagetx);
    mydata->previous_dir=STOP;
    mydata->nb_voisins=0;
    mydata->last_update=kilo_ticks;
    mydata->next_direction=STOP;
    mydata->new_message=0;
    mydata->distance=-1;
    mydata->nb=1;
    mydata->nb_repuls=0;
    mydata->nb_attract=0;
}



void loop(){
/*
Traitement des messages
décide des comportement en fontion du nombre de voisin ou de tooClose()
*/

  //si un message est arrivé,le traiter
  if (kilo_uid==0 || kilo_uid==1){
    emission();
    return;
  }
  if (mydata->new_message == 1)
  {
    update_from_message();
    mydata->new_message=0;
  }
  //possible changement de direction toute les secondes = décide la direction random à prendre si besoin
    if (kilo_ticks>mydata->last_update+mydata->nb*SECONDE) {
      mydata->next_direction=(rand_hard()%3)+1;
      mydata->last_update=kilo_ticks;
    }
    //printf("----------------------------------");
    //printf("loop\n");
    //printf("    mydata->nb_voisins%d\n",mydata->nb_voisins );
    update_voisins(); //met a jour la liste de ses voisins


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
