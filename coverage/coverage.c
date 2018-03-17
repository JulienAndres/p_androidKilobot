#include <kilolib.h>

#define MAXVOISIN 5
#define SECONDE 32
#define ASK 50

#define STOP 0
#define STRAIGHT 1
#define LEFT 2
#define RIGHT 3

#define DEBUG
#include <debug.h>


uint8_t nb_voisins;

typedef struct{
  uint32_t timestamp;
  uint8_t dist;
  uint16_t id;
}voisins;

voisins voisins_liste[MAXVOISIN];
uint8_t previous_dir;
message_t messagetx;
message_t messagerx;
uint8_t new_message=0;
uint8_t distance=-1;
int last_update;
uint8_t next_direction;

void update_from_message(){
  uint8_t ID=messagerx.data[0];
  //DEFINIR ID A PARTIR DU MESSAGE
  uint8_t found=0;
  uint8_t i=0;
  printf("        message from %d\n", ID);
  while(i<nb_voisins && found==0){
    if (voisins_liste[i].id==ID){
      found=1;
      printf("        deja dans la liste\n");
    }else{
      i++;
    }
  }
  if (found==0){
    if (nb_voisins<MAXVOISIN){
      nb_voisins++;
    }

  }
  voisins_liste[i].id=ID;
  voisins_liste[i].timestamp=kilo_ticks;
  voisins_liste[i].dist=distance;//METTRE DISTANCE A PARTIR DU MESSAGE
  printf("mise a jour : id : %d time : %d distace : %d\n", voisins_liste[i].id,voisins_liste[i].timestamp,voisins_liste[i].dist);
  distance=-1;

}

void update_voisins(){
  printf("    update_voisins\n");
  if (nb_voisins==0){
    printf("        pas de voisins\n");
    return ;
  }
      int8_t i;

      for (i = nb_voisins-1; i >= 0; i--){
        printf("        liste : id: %d time: %d dist : %d \n",voisins_liste[i].id,voisins_liste[i].timestamp,voisins_liste[i].dist );
          if (kilo_ticks - voisins_liste[i].timestamp  > 2*SECONDE){  //this one is too old.
            printf("kiloticks %d\n",kilo_ticks );
            printf("        delete voisin %d\n", voisins_liste[i].id);
              voisins_liste[i]= voisins_liste[nb_voisins];
              voisins_liste[nb_voisins-1].id=-1;
              nb_voisins--;
            }
      }
}

void update_motors(uint8_t direction) {
    // printf(" new direction %d\n",direction );
    // printf("ancienne direction %d\n",previous_dir );
    if (direction != previous_dir) {
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
        previous_dir = direction;
      }
}
message_t *message_tx()
{
    return &messagetx;
}

void message_rx(message_t *message, distance_measurement_t *d)
{
    messagerx= *message;
    distance= estimate_distance(d);
    new_message = 1;
}

void setup()
{
    printf("setup\n");
    printf("%d\n",kilo_uid );
    // Initialize message:
    messagetx.type = NORMAL;
    messagetx.data[0]=kilo_uid;
    messagetx.crc = message_crc(&messagetx);
    previous_dir=STOP;
    nb_voisins=0;
    last_update=kilo_ticks;
    next_direction=STOP;

    //int i=0;
    // for(;i<MAXVOISIN;i++){
    //   voisins_liste[i]=NULL;
    // }
}

uint8_t tooClose(){
  uint8_t i;
  uint8_t stop=0;
  for(i=0;i<nb_voisins;i++){
    if (voisins_liste[i].dist<ASK){
      stop=1;
    }
  }
  printf("tooClose %d\n",stop );
  return stop;
}

void loop()
{
  //si un message est arrivé,le traiter
  if (new_message == 1)
  {
    printf("    Nouveau message\n");
    update_from_message();
    new_message=0;
  }
  //possible changement de direction toute les secondes
    if (kilo_ticks>last_update+SECONDE) {
      next_direction=(rand_hard()%3)+1;
      last_update=kilo_ticks;
    }
    printf("----------------------------------");
    printf("loop\n");
    printf("    nb_voisins%d\n",nb_voisins );
    update_voisins(); //met a jour la liste de ses voisins

    if (tooClose() || nb_voisins==0){
      printf("    tooclose or new voisins\n");
      update_motors(next_direction);//randomdirection
      set_color(RGB(1,0,0));
    }else{
      printf("    perfect distance\n");
      update_motors(STOP);
      set_color(RGB(1,1,1));
    }
}


int main()
{
    debug_init();
    kilo_init();
    // Register the message_rx & message_tx callback function.
    kilo_message_rx = message_rx;
    kilo_message_tx=message_tx;
    //start loop
    kilo_start(setup, loop);

    return 0;
}
