#include <kilombo.h>
#include <stdio.h>
#include "proba.h"
#include "mEDEA.h"
#include "communication.h"
#include "movement.h"

extern USERDATA * mydata;

void update_voisins(){
	if (!mydata->nb_voisins){
		return;
	}
	int i;
	for(i=mydata->nb_voisins-1;i>=0;i--){
		if (kilo_ticks-mydata->voisins_liste[i].timestamp > SECONDE){
		// if (kilo_uid==83)	printf("delete %d\n",mydata->voisins_liste[i].id );
			mydata->voisins_liste[i]=mydata->voisins_liste[mydata->nb_voisins];
			mydata->voisins_liste[mydata->nb_voisins-1].id=-1;

			mydata->nb_voisins--;
		}
	}
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
void update_only_voisins_from_message(){
	/*update de la distance
	*/
	uint8_t found_id=0;
	uint32_t distance=mydata->message_dist;
	int ID=mydata->message.data[0];
	int i=0;
	while (i< mydata->nb_voisins && !found_id ){
		if(mydata->voisins_liste[i].id ==ID){
			found_id=1;
		}else{
			i++;
		}
	}
	if (!found_id){
		if (mydata->nb_voisins<MAXVOISIN){
			mydata->nb_voisins++;
		}else{
			i--;
		}
	}
		mydata->voisins_liste[i].id=ID;
		mydata->voisins_liste[i].timestamp=kilo_ticks;
		mydata->voisins_liste[i].dist=distance;

	// if (kilo_uid==83) printf("%d %d nb %d\n",message->data[0],distance ,mydata->nb_voisins);

	mydata->new_message=0;
}

void update_from_message(){
	/*update de la distance
	*/
	if (!mydata->message.data[8] || mydata->message.data[0]==IDFOOD){ //on se fout du génome du bloc actif
		update_only_voisins_from_message();
		return;
	}
	uint8_t found_id=0;
	uint32_t distance=mydata->message_dist;
	int ID=mydata->message.data[0];
	int i=0;
	while (i< mydata->nb_voisins && !found_id ){
		if(mydata->voisins_liste[i].id ==ID){
			found_id=1;
		}else{
			i++;
		}
	}
	if (!found_id){
		if (mydata->nb_voisins<MAXVOISIN){
			mydata->nb_voisins++;
		}else{
			i--;
		}
	}
		mydata->voisins_liste[i].id=ID;
		mydata->voisins_liste[i].timestamp=kilo_ticks;
		mydata->voisins_liste[i].dist=distance;


/*update du génome de ce voisin
*/
	found_id=0;
	i=0;
		while (i< mydata->nb_genome && !found_id ){
			if(mydata->genome_list[i].id ==ID){
				found_id=1;
			}else{
				i++;
			}
		}
		if (!found_id){
			if (mydata->nb_genome<MAXROBOT){
				mydata->nb_genome++;
			}else{
				i--;
			}
		}
			int j;
			mydata->genome_list[i].id=ID;
			for(j=0;j<GENOMEPARAM;j++){
				mydata->genome_list[i].genome[j]=mydata->message.data[j+1];
			}


	// if (kilo_uid==83) printf("%d %d nb %d\n",message->data[0],distance ,mydata->nb_voisins);

	mydata->new_message=0;
}


void message_rx (message_t *message, distance_measurement_t *distance){
    mydata->new_message = 1;
		mydata->message=*message;
		mydata->message_dist=estimate_distance(distance);
	//	mydata->toAggregate.dist = estimate_distance(distance);
		//if (kilo_uid==8) printf("DISTANCE.toAggregate : %d\n",mydata->toAggregate.dist);
}
void setup_message(){
	mydata->broadcast=0;//ne pas transmettre quand on change le message

	mydata->msg_transmis.type = NORMAL;
	mydata->msg_transmis.data[0] = kilo_uid; //on sait que le kilo_uid < 256 car on a pas autant de kilobot
int i;
	for(i=0;i<GENOMEPARAM;i++){
		mydata->msg_transmis.data[i+1]=mydata->genome[i];
	}
	mydata->msg_transmis.crc = message_crc(&mydata->msg_transmis);


	mydata->broadcast=1;
	return;
}

void share_genome_allowed(){
	mydata->broadcast=0;//ne pas transmettre quand on change le message

	mydata->msg_transmis.type = NORMAL;
	mydata->msg_transmis.data[0] = kilo_uid; //on sait que le kilo_uid < 256 car on a pas autant de kilobot
int i;
	for(i=0;i<GENOMEPARAM;i++){
		mydata->msg_transmis.data[i+1]=mydata->genome[i];
	}
	mydata->msg_transmis.data[8]=1;
	mydata->msg_transmis.crc = message_crc(&mydata->msg_transmis);


	mydata->broadcast=1;
	return;
}

void share_genome_forbiden(){
	mydata->broadcast=0;//ne pas transmettre quand on change le message

	mydata->msg_transmis.type = NORMAL;
	mydata->msg_transmis.data[0] = kilo_uid; //on sait que le kilo_uid < 256 car on a pas autant de kilobot
int i;
	for(i=0;i<GENOMEPARAM;i++){
		mydata->msg_transmis.data[i+1]=mydata->genome[i];
	}
	mydata->msg_transmis.data[8]=0;
	mydata->msg_transmis.crc = message_crc(&mydata->msg_transmis);


	mydata->broadcast=1;
	return;
}

message_t *message_tx(){
	if (kilo_uid==0){
		return &mydata->msg_transmis;
	}
	if(mydata->broadcast){
		canBroadcast(); //vérification de si il est proche du bloc qui permet de broadcast-peut changer toutes les 2 secondes
		//printf("%d test\n",kilo_uid );
		return &(mydata->msg_transmis);

	} else {
  	return 0;
	}
	return 0;
	//return &(mydata->message);
}

void message_tx_success()
{
    // Set the flag on message transmission.
    mydata->message_sent = 1;
}
