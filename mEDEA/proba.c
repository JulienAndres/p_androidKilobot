#include <kilombo.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "proba.h"
#include "mEDEA.h"
#include "communication.h"

extern USERDATA * mydata;

int probaBroadcast(uint8_t dist){//TODO proba en fonction de la distance
  return 1;
}

int canBroadcast(){
  if(kilo_ticks<mydata->last_allowed+2*SECONDE){
    return mydata->msg_transmis.data[8];
  }
  mydata->last_allowed=kilo_ticks;
  int i;
  for(i=0;i<mydata->nb_voisins;i++){
    if (mydata->voisins_liste[i].id==IDFOOD){
      int proba=probaBroadcast(mydata->voisins_liste[i].dist);
      int rd=rand();
      if (rd> RAND_MAX*(1-proba)){
        share_genome_allowed();
        return 1;
      }
      else{
        share_genome_forbiden();
        return 0;
      }
    }
  }
  return 0;
}

int arrondi(double n){
	return n+0.5;
}
