#include <kilolib.h>
#include "main.h"
#include "movement.h"

#define STOP 0
#define FORWARD 1
#define LEFT 2
#define RIGHT 3

data_t data;
data_t *mydata = &data;


void setup() {
// put your setup code here, to be run only once
//message.type = NORMAL;
//message.crc = message_crc(&message);
mydata->curr_motion = STOP;

}

void loop() {
	if (mydata->curr_motion == STOP){
		set_motion(FORWARD);
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
