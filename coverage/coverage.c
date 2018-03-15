#include <kilolib.h>

#define MAXVOISIN 5
#define SECONDE 32
#define ASK 50

#define STOP 0
#define STRAIGHT 1
#define LEFT 2
#define RIGHT 3

// typedef enum {
//     STRAIGHT,
//     LEFT,
//     RIGHT,
//     STOP
// } motion_dir;

uint8_t nb_voisins;

typedef struct{
  uint8_t timestamp;
  uint8_t dist;
  uint8_t id;
}voisins;

voisins voisins_liste[MAXVOISIN];
uint8_t previous_dir=STOP;
message_t messagetx;
message_t messagerx;
int new_message=0;
int distance=-1;

// void message_rx(message_t *m, distance_measurement_t *d)
// {
//     new_message = 1;
//     distance = estimate_distance(d);
// }
void update_from_message(){
  uint8_t ID=messagerx.data[0];
  //DEFINIR ID A PARTIR DU MESSAGE
  uint8_t found=0;
  int i=0;
  while(i<nb_voisins && found==0){
    if (voisins_liste[i].id==ID){
      found=1;
    }else{
      i++;
    }
  }
  if (found==0){
      nb_voisins++;
  }
  voisins_liste[i].id=ID;
  voisins_liste[i].timestamp=kilo_ticks;
  voisins_liste[i].dist=distance;//METTRE DISTANCE A PARTIR DU MESSAGE
  distance=-1;

}

void update_voisins(){
  if (nb_voisins==0){
    return ;
  }
      int8_t i;

      for (i = nb_voisins-1; i >= 0; i--){
          if (kilo_ticks - voisins_liste[i].timestamp  > 2*SECONDE){  //this one is too old.
              voisins_liste[i]= voisins_liste[nb_voisins];
              nb_voisins--;
            }
      }
}

void update_motors(int direction) {
    if (direction != previous_dir) {
        if (previous_dir==STOP){
          spinup_motors();
          spinup_motors();
          spinup_motors();
          spinup_motors();
          set_color(RGB(1,1,1));
        }
        previous_dir = direction;
        switch(direction) {
            case STRAIGHT:
                set_motors(kilo_straight_left, kilo_straight_right);
                break;
            case LEFT:
                set_motors(kilo_turn_left,0);
                break;
            case RIGHT:
                set_motors(0,kilo_turn_right);
                break;
            case STOP:
                set_motors(0,0);
                break;
        }
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
    // Initialize message:
    messagetx.type = NORMAL;
    messagetx.data[0]=kilo_uid;
    messagetx.crc = message_crc(&messagetx);
    previous_dir=STOP;
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

  return stop;
}

void loop()
{
    // Blink the LED magenta whenever a message is sent.
    update_voisins();
    if (new_message == 1)
    {
      update_from_message();
      set_color(RGB(0, 1, 0));
    }
    if (tooClose() || nb_voisins==0){
      update_motors(rand_soft()%2+2);//randomdirection
    }else{
      update_motors(STOP);
      set_color(RGB(1,1,1));
    }
}


int main()
{
    kilo_init();
    // Register the message_rx & message_tx callback function.
    kilo_message_rx = message_rx;
    kilo_message_tx=message_tx;
    //start loop
    kilo_start(setup, loop);

    return 0;
}
