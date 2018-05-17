#include <kilombo.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include "proba.h"
#include "aggregation.h"

extern USERDATA * mydata;

void makeJoinDecision(){
    if (rand() > RAND_MAX*(1-PROBA_JOIN)){
      printf("makeJoinDecision\n" );
        mydata->state = CONVERGING;
        mydata->curr_motion =  rand_hard()%2 + 1;
    }

}

void makeLeaveDecision(){
    int p=clusters_proba2();
    // int p=clusters_proba();
    // int p=uniform_proba();

    if (rand() > p){
      printf("makeLeaveDecision %d\n" ,kilo_uid);
        mydata->state = REPELLING;
        mydata->curr_motion = rand_hard()%2 + 1;
        mydata->start_repelling = kilo_ticks;
    }
}

int uniform_proba(){
  return RAND_MAX*(1-PROBA_LEAVE );
}
int clusters_proba(){
  return (mydata->nb_voisins/(double)CLUSTER_SIZE)*RAND_MAX;
}

int clusters_proba2(){
  if (mydata->nb_voisins>CLUSTER_SIZE){
    return RAND_MAX;
  }else{
    return uniform_proba();
  }
}
