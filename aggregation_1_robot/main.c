#include <kilolib.h>
#define DEBUG
#include <debug.h>
#include <stdio.h>
#include "main.h"

data_t data;
data_t *mydata = &data;

void setup() {
// put your setup code here, to be run only once
//message.type = NORMAL;
//message.crc = message_crc(&message);
mydata->new_message = 0;
mydata->last_dist_update = -1;
mydata->toAggregate.dist = -1;
mydata->state = SEARCHING;
//mydata->curr_motion = STOP;
set_motion(STOP);
//mydata->toAggregate = NULL;
}

void aggregation() {
	if (kilo_ticks > mydata->last_motion_update + 32){
		mydata->last_motion_update = kilo_ticks;

		switch(mydata->state){
			case SEARCHING:
				searching();
				break;
			case CONVERGING:
				converging();
				break;
			case SLEEPING:
				sleeping();
				break;
		}
	}

	set_motion(mydata->curr_motion);
	//printf("MOTION : %d\n",mydata->curr_motion);
	//("DISTANCE.toAggregate : %d\n",mydata->toAggregate.dist);
	printf("DISTANCE.last_dist_update : %d\n", mydata->last_dist_update);
}

void searching(){
	set_color(RGB(1,0,0));
	mydata->last_motion_update = kilo_ticks;

	if(found_to_aggregate()){
		mydata->new_message = 0;
		mydata->state = CONVERGING;
		//mydata->curr_motion = STRAIGHT;
		set_motion(STRAIGHT);
		mydata->last_dist_update = mydata->toAggregate.dist;
	} else {
		mydata->state = SEARCHING;
		set_random_direction();
	}
}

uint8_t found_to_aggregate(){
	uint8_t found = 0;
	if(mydata->new_message == 1){
		mydata->toAggregate.timestamp = kilo_ticks;
		found = 1;
	}
	return found;
}

void converging(){
	set_color(RGB(0,1,0));
	if(is_too_close()){
		mydata->state = SLEEPING;
		//mydata->curr_motion = STOP;
		set_motion(STOP);
	} else {
		if(mydata->toAggregate.dist > mydata->last_dist_update){
			printf("IN TEST");
			switch (mydata->curr_motion) {
				case RIGHT:
					//mydata->curr_motion = LEFT;
					set_motion(LEFT);
					break;
				case LEFT:
					//mydata->curr_motion = RIGHT;
					set_motion(RIGHT);
					break;
				case STRAIGHT:
				default:
					set_random_turning_direction();
					break;
			}
		}
		mydata->last_dist_update = mydata->toAggregate.dist;
	}

}

void sleeping(){
	set_color(RGB(0,0,1));
	set_motion(STOP);
}

uint8_t is_too_close(){
	uint8_t stop = 0;
	printf("dist dans is_too_close %d\n", mydata->toAggregate.dist);
	if(mydata->toAggregate.dist <= 40){

		stop = 1;
	}
	return stop;
}

void set_motion(uint8_t motion){
	if(mydata->curr_motion != motion){
		switch(motion){
			case LEFT:
				spinup_motors();
				set_motors(kilo_turn_left, 0);
				break;
			case RIGHT:
				spinup_motors();
				set_motors(0, kilo_turn_right);
				break;
			case STRAIGHT:
				spinup_motors();
				set_motors(kilo_straight_left, kilo_straight_right);
				break;
			case STOP:
				default:
				set_motors(0, 0);
			break;
		}
		mydata->curr_motion = motion;
	}
}

void set_random_direction(){
    uint8_t random_number = rand_hard()%4;
    //Compute the remainder of random_number when divided by 3.
    // This gives a new random number in the set {0, 1, 2}. The value is incremented and returned.
    if ((random_number == 0) || (random_number == 3)){
        //mydata->curr_motion = STRAIGHT;
				set_motion(STRAIGHT);
    }
    else if(random_number == 1){
        //mydata->curr_motion = LEFT;
				set_motion(LEFT);
    }
    else{
        //mydata->curr_motion = RIGHT;
				set_motion(RIGHT);
    }
}

void set_random_turning_direction(){
	uint8_t random_number = rand_hard()%2;
	if(random_number == 0){
		//mydata->curr_motion = LEFT;
		set_motion(LEFT);
	} else {
		//mydata->curr_motion = RIGHT;
		set_motion(RIGHT);
	}
}


void message_rx (message_t *message, distance_measurement_t *distance){
    mydata->new_message = 1;

		mydata->toAggregate.dist = estimate_distance(distance);
		printf("DISTANCE.toAggregate : %d\n",mydata->toAggregate.dist);
}

//message_t *message_tx(){
//    return &message;
//}


int main() {
    kilo_init();
		debug_init();
    kilo_message_rx = message_rx;
    //kilo_message_tx = message_tx;
    kilo_start(setup, aggregation);

    return 0;
}
