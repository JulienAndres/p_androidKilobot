#include <kilolib.h>
#include "main.h"

#define STOP 0
#define FORWARD 1
#define LEFT 2
#define RIGHT 3

data_t data;
data_t *mydata = &data;

int val = 80;
int test = 1;
void setup() {
// put your setup code here, to be run only once
//message.type = NORMAL;
//message.crc = message_crc(&message);
mydata->curr_motion = STOP;

}

void loop() {
  if(test){
    set_motors(val, val);
    val += 10;
    delay(10000);
  }else{
    set_motors(kilo_straight_left, kilo_straight_right);
  }

}

//void message_rx (message_t *message, distance_measurement_t *distance){
//    mydata->new_message = 1;
//}

//message_t *message_tx(){
//    return &message;
//}


int main() {
    kilo_init();

    //kilo_message_rx = message_rx;
    //kilo_message_tx = message_tx;
    kilo_start(setup, loop);

    return 0;
}
