#include <kilombo.h>
#include <stdio.h>
#include "mEDEA.h"
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
	mydata->msg_transmis.type = NORMAL;
	mydata->msg_transmis.data[0] = kilo_uid;
	mydata->msg_transmis.data[8] =0;//on utilise cet octet pour savoir si le message est un génome ou information seulement 0=info 1=genome
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
mydata->dead=0;
mydata->genome_setup=0;
mydata->nb_genome=0;
mydata->last_allowed=0;
mydata->last_genome_update=0;
int i=0;
for(i=0;i<TIMEUPDATE;i++){
	mydata->last_fitness[i]=0;
}
mydata->last_update_fitness=0;
i=0;
for(i=1;i<9;i++){
	mydata->msg_transmis.data[i]=0;
}

genome_alea();
	set_motion(STRAIGHT);
}

void genome_alea(){
	if (!mydata->genome_setup){ //la premiere fois : setup du genome aleatoirement
		int i;
		for (i=0;i<GENOMEPARAM;i++){ //initialisation du génome aléatoirement
			mydata->genome[i]=rand_hard()%3;
		}
		mydata->genome_setup=1;
		printf("%d genome set\n",kilo_uid );
		int j=0;
		for(;j<GENOMEPARAM;j++){
			printf("%d  ",mydata->genome[j] );
		}
		printf("\n");
	}else{
		if(!mydata->nb_genome){
			printf("%d DIED\n", kilo_uid);
			mydata->dead=1;
			mydata->last_genome_update=kilo_ticks;
			return;
		}
		float bestfit=mydata->genome_list[0].fitness;
		int best_indice=0;
		int i=0;
		for (i=0;i<mydata->nb_genome;i++){
			if (mydata->genome_list[i].fitness > bestfit){
				bestfit=mydata->genome_list[i].fitness;
				best_indice=i;

			}
		}
		// printf("best fit %d\n",bestfit );
		i=0;
		for (i=0;i<GENOMEPARAM; i++){
			mydata->genome[i]=mydata->genome_list[best_indice].genome[i];
			printf("%d ",mydata->genome[i] );
		}
		printf("apres mutation\n" );

		//mutation
		if (((float)rand_hard())/256 < PROBA_MUTATION){
			int indice_change=rand_hard()/(256/GENOMEPARAM);
			int chang=(rand_hard()/128)+1;
			mydata->genome[indice_change]=(mydata->genome[indice_change]+chang)%3;

		}

		for (i=0;i<GENOMEPARAM;i++){
			printf("%d ",mydata->genome[i]);
		}
		printf("apres mutation\n" );
		/* SI CHOIX RANDOM PARMIS TOUS LES GENOMES */
		// int i=rand_hard()%mydata->nb_genome;
		// int j;
		// for (j=0;j<GENOMEPARAM;j++){//pas de mutation pour le moment
		// 	mydata->genome[j]=mydata->genome_list[i].genome[j];
		// }

	}
	mydata->last_genome_update=kilo_ticks;
	mydata->nb_genome=0;//reset des genomes recus
	setup_message();
}

float fitness(){
	int i;
	float toRet=0;
	for (i=0;i<TIMEUPDATE;i++){
		toRet+=mydata->last_fitness[i];
	}
	toRet/=TIMEUPDATE;
	return toRet;
}



void loop() {
	// if (kilo_uid==IDFOOD){
	// set_color(RGB(1,0,0));
	//  	emission();
	// 	return;
	// }
	// setup_message();
	update_voisins();
	update_fitness();
	setup_message_fitness();
	if(mydata->new_message==1){
		update_from_message();
	}
	if (kilo_ticks > mydata->last_genome_update + 60 * SECONDE){
			genome_alea(); //choisir génome aléatoirement
	}

	//printf("uid : %d last motion update %d \n",kilo_uid,mydata->last_motion_update);
	if (kilo_ticks > mydata->last_motion_update + SECONDE){
		mydata->last_motion_update = kilo_ticks;
		if (mydata->dead){
			set_color(RGB(0,0,0));
			motion_dead();
		}else{
			genome_motion();//CONTROLLEUR

		}

	}

}


int main() {
	/*
Initialise callback et lance la main loop
*/
    kilo_init();
    kilo_message_rx = message_rx;
    kilo_message_tx = message_tx;
		kilo_message_tx_success = message_tx_success;

		kilo_start(setup, loop);

    return 0;
}
