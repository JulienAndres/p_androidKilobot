#include <kilombo.h>
#include <stdio.h>
#include "aggregation.h"
#include "proba.h"
#include "communication.h"
#include "movement.h"

/*
TODO :
Rajouter un timer en mode repelling ? (genre 10s pour eveiter de faire n imp)
Ajouter une fonction de proba qui donne une proba de leave en fonction du nombre de voisins que on a
Demander au prof stage
Demander au prof comment mettre le bloc actif dans cet algo. -idée : faire comme sin il avait déjà 5 voisins (variable ?)-
*/

//Idée de cahier des charges : mettre en avant l experimentation du bloc actif et de la modification des algos pour ces blocs actifs.





REGISTER_USERDATA(USERDATA)

void setup() {
	// put your setup code here, to be run only once

	mydata->msg_transmis.type = NORMAL;
	mydata->msg_transmis.data[0] = kilo_uid;
	mydata->msg_transmis.data[1] =0;
	mydata->msg_transmis.crc = message_crc(&mydata->msg_transmis);

	mydata->toAggregate.nb_voisins=0;
	mydata->toAggregate.dist=-1;

	mydata->new_message = 0;
	mydata->last_dist_update = -1;
	mydata->toAggregate.dist = -1;
	mydata->state = SEARCHING;
	mydata->broadcast = 1;
	mydata->message_sent = 0;
	mydata->last_motion_update=0;
	mydata->nb_voisins=0;
	mydata->start_repelling=0;
	//mydata->curr_motion = STOP;
	set_motion(STOP);
	printf("%d\n",kilo_uid );
	//mydata->toAggregate = NULL;
}

void aggregation() {
	// if (kilo_uid==0){
	// 	emission();
	// 	return;
	// }
	update_voisins();
	if(mydata->new_message==1){
		update_from_message();
	}

	//printf("uid : %d last motion update %d \n",kilo_uid,mydata->last_motion_update);
	if (kilo_ticks > mydata->last_motion_update + SECONDE){
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
			case REPELLING:
				repelling();
				break;
		}
	}

	set_motion(mydata->curr_motion);
	//printf("MOTION : %d\n",mydata->curr_motion);
	//("DISTANCE.toAggregate : %d\n",mydata->toAggregate.dist);
	//printf("DISTANCE.last_dist_update : %d\n", mydata->last_dist_update);
}

void searching(){
	set_color(RGB(1,0,0));
	mydata->last_motion_update = kilo_ticks;
//	printf("NEW MESSAGE : %d\n", mydata->new_message);
	if(hasBestNeighbor()){
		mydata->state = CONVERGING;
		set_motion(STRAIGHT);
		mydata->last_dist_update = mydata->toAggregate.dist;
	} else {
		mydata->state = SEARCHING;
		set_random_direction();
	}
}

uint8_t hasBestNeighbor(){
    int8_t i;
		if(!mydata->nb_voisins){
			return 0;
		}
    for (i = mydata->nb_voisins-1; i >= 0; i--) {
        if (mydata->voisins_liste[i].nb_voisins >= mydata->toAggregate.nb_voisins){
            mydata->toAggregate = mydata->voisins_liste[i];
        }
    }
    return 1;
}


void repelling(){
	set_color(RGB(1,1,1));
	// if ((kilo_ticks>mydata->start_repelling+10*SECONDE)){//10 secondes pour se liberer
	// 	mydata->state=SEARCHING;
	// }

	makeJoinDecision();
	if (!mydata->nb_voisins){
		mydata->state=SEARCHING;
	}else{
		if(mydata->toAggregate.dist <= mydata->last_dist_update){
			// printf("IN TEST\n");
			switch (mydata->curr_motion) {
				case RIGHT:
					set_motion(LEFT);
					break;
				case LEFT:
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


	return;
}

void converging(){
	// printf("MOTION : %d\n",mydata->curr_motion);

	set_color(RGB(0,1,0));
	if(is_too_close()){
		mydata->state = SLEEPING;
		set_motion(STOP);
	} else {
		if(mydata->toAggregate.dist >= mydata->last_dist_update){
			// printf("IN TEST\n");
			switch (mydata->curr_motion) {
				case RIGHT:
					set_motion(LEFT);
					break;
				case LEFT:
					set_motion(RIGHT);
					break;
				case STRAIGHT:
				default:
					set_random_turning_direction();
					break;
			}
		}
		if(!hasBestNeighbor()){
			mydata->state = SEARCHING;
		}

		mydata->last_dist_update = mydata->toAggregate.dist;
	}

}

void sleeping(){
	set_color(RGB(0,0,1));
	set_motion(STOP);
	//enable_tx = 1;
	if(!is_too_close()){
		mydata->state = SEARCHING;
		//enable_tx = 0;
		mydata->new_message = 0;
	}
	makeLeaveDecision();

	//printf("broadcast : %d\n", mydata->broadcast);
}

uint8_t is_too_close(){
	//printf("dist dans is_too_close %d\n", mydata->toAggregate.dist);

	int i=0;
	for (;i<mydata->nb_voisins;i++){
		if (mydata->voisins_liste[i].dist <= DIST_TO_AGGREGATE){
			//printf("tooclose\n");
			return 1;
		}
	}

	return 0;
}





int main() {
	/*
Initialise callback et lance la main loop
*/
    kilo_init();

    kilo_message_rx = message_rx;
    kilo_message_tx = message_tx;
		kilo_message_tx_success = message_tx_success;

		kilo_start(setup, aggregation);

    return 0;
}
