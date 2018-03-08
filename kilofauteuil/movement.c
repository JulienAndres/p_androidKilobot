#include <kilolib.h>
#include "main.h"
#include "movement.h"

#define STOP 0
#define FORWARD 1
#define LEFT 2
#define RIGHT 3

extern data_t *mydata;

void set_motion (int new_motion){
	switch(mydata->curr_motion){
		case STOP:
			set_motors(0, 0);
			break;
		case FORWARD:
		  spinup_motors();
			set_color(RGB(0, 1, 0));
		  set_motors(kilo_straight_left, kilo_straight_right);
			break;
		case LEFT:
			spinup_motors();
			set_color(RGB(1, 0, 0));
	    set_motors(kilo_turn_left, 0);
			break;
		case RIGHT:
	    spinup_motors();
			set_color(RGB(0, 0, 1));
		 	set_motors(0, kilo_turn_right);
			break;
		default:
			set_motors(0, 0);
			break;
		}
	mydata->curr_motion = new_motion;
}

void set_random_direction(){
	uint8_t rand = rand_hard()%4;
	if( (rand == 0) || (rand == 1)){
		set_motion(FORWARD);
	} else if (rand == 2){
		set_motion(LEFT);
	} else if (rand == 3){
		set_motion(RIGHT);
	} else {
		set_color(RGB(0, 1, 1));
	}
}
