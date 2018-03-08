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
mydata->new_message = 0;
}

void loop() {
	if (kilo_ticks > mydata->last_motion_update + 64){
		mydata->last_motion_update = kilo_ticks;
		if (mydata->new_message == 1){
			set_random_direction();
			mydata->new_message = 0;
		} else {
			set_color(RGB(1,1,1));
			set_motion(STOP);
		}
	}
	delay(2000);
	//set_color(RGB(0,0,0));
}

void message_rx (message_t *message, distance_measurement_t *distance){
    mydata->new_message = 1;
}

//message_t *message_tx(){
//    return &message;
//}


int main() {
    kilo_init();

    kilo_message_rx = message_rx;
    //kilo_message_tx = message_tx;
    kilo_start(setup, loop);

    return 0;
}
