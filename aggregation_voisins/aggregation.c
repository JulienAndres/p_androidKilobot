#include <kilombo.h>
#include <stdio.h>
#include "aggregation.h"

#define SECONDE 32
#define DIST_TO_AGGREGATE 50


REGISTER_USERDATA(USERDATA)

void setup() {
	// put your setup code here, to be run only once
	mydata->message.type = NORMAL;
	mydata->message.data[0] = kilo_uid;
	mydata->message.crc = message_crc(&mydata->message);
	mydata->nb_voisins = 0;
	mydata->new_message = 0;
	mydata->last_dist_update = -1;
	mydata->state = SEARCHING;
	mydata->broadcast = 0;
	mydata->message_sent = 0;
	mydata->last_motion_update=0;
	//mydata->curr_motion = STOP;
	set_motion(STOP);
	printf("%d\n",kilo_uid );
	//mydata->toAggregate = NULL;
}

void emission(){
	// Blink the LED magenta whenever a message is sent.
	if (mydata->message_sent == 1)
	{
		//printf("EMISSION %d\n",kilo_uid );
		mydata->message_sent = 0;
		set_color(RGB(0, 0, 1));
			if (kilo_ticks>mydata->last_dist_update+(SECONDE/5)){
				mydata->last_dist_update=kilo_ticks;

			}
	}
}

void aggregation() {
	if (kilo_uid==0){
		emission();
		return;
	}

	if(mydata->new_message == 1){
		update_from_message();
		mydata->new_message = 0;
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
		}
	}
	update_voisins();
	set_motion(mydata->curr_motion);
	//printf("MOTION : %d\n",mydata->curr_motion);
	//("DISTANCE.toAggregate : %d\n",mydata->toAggregate.dist);
	//printf("DISTANCE.last_dist_update : %d\n", mydata->last_dist_update);
}

void searching(){
	set_color(RGB(1,0,0));
	mydata->last_motion_update = kilo_ticks;
//	printf("NEW MESSAGE : %d\n", mydata->new_message);
	if(found_to_aggregate()){
		mydata->state = CONVERGING;
		set_motion(STRAIGHT);
	} else {
		mydata->state = SEARCHING;
		set_random_direction();
	}
}

uint8_t found_to_aggregate(){
	uint8_t found = 0;
	if(mydata->new_message == 1){
		mydata->new_message = 0;
		found = 1;
	}
	return found;
}

uint8_t get_closest_neighbour_dist(){
	uint8_t mindist = mydata->voisins_liste[0].dist;
	uint8_t i;
	for(i=0; i<mydata->nb_voisins; i++){
		if(mydata->voisins_liste[i].dist < mindist){
			mindist = mydata->voisins_liste[i].dist;
		}
	}
	return mindist;
}

void converging(){
	// printf("MOTION : %d\n",mydata->curr_motion);

	set_color(RGB(0,1,0));
	if(is_too_close()){
		mydata->state = SLEEPING;
		set_motion(STOP);
	} else {
		if(get_closest_neighbour_dist() >= mydata->last_dist_update){
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
		if(!found_to_aggregate()){
			mydata->state = SEARCHING;
		}
	}
}

void sleeping(){
	set_color(RGB(0,0,1));
	set_motion(STOP);
	mydata->broadcast = 1;
	//enable_tx = 1;
	if(!found_to_aggregate()){
		mydata->state = SEARCHING;
		mydata->broadcast = 0;
		//enable_tx = 0;
		mydata->new_message = 0;
	}

	//printf("broadcast : %d\n", mydata->broadcast);
}

uint8_t is_too_close(){
	uint8_t stop = 0;
	//printf("dist dans is_too_close %d\n", mydata->toAggregate.dist);
	if(get_closest_neighbour_dist() <= DIST_TO_AGGREGATE){

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
				set_motion(STRAIGHT);
    }
    else if(random_number == 1){
				set_motion(LEFT);
    }
    else{
				set_motion(RIGHT);
    }
}

void set_random_turning_direction(){
	//printf("ici N?\n" );
	uint8_t random_number = rand_hard()%2;
	if(random_number == 0){
		set_motion(LEFT);
	} else {
		set_motion(RIGHT);
	}
}

int lost_aggregate(){
	uint8_t lost = 0;
	if(mydata->new_message == 0){
		lost = 1;
	}
	return lost;
}

void update_from_message(){
  /*
Mise à jour de la liste des voisins en fonction du message recu
  ->ajout dans la liste s'il n esite pas
  ->mise à jour des parametres si il est déjà dans la liste
  */
  uint8_t ID=mydata->message.data[0];
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

void message_rx (message_t *message, distance_measurement_t *distance){
    mydata->new_message = 1;
		mydata->distance = estimate_distance(distance);
		//if (kilo_uid==8) printf("DISTANCE.toAggregate : %d\n",mydata->toAggregate.dist);
}

message_t *message_tx(){
	if (kilo_uid==0){
		return &mydata->message;
	}
	if(mydata->broadcast){
		//printf("BROADCASTING %d\n",mydata->message.data[0]);
		//return &mydata->message;
		//printf("Adresse message : %d\n", &(mydata->message));
		return &(mydata->message);
	} else {
  	return 0;
	}

	//return &(mydata->message);
}

void message_tx_success()
{
    // Set the flag on message transmission.
    mydata->message_sent = 1;
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
