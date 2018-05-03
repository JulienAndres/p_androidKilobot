#include <kilombo.h>
#include <stdio.h>
#include <math.h>
#include "proba.h"
#include "aggregation.h"

extern USERDATA * mydata;

void makeJoinDecision(){
    if (rand_hard()/255 > PROBA_JOIN){
      printf("makeJoinDecision\n" );
        mydata->state = CONVERGING;
        mydata->curr_motion =  rand_hard()%2 + 1;
    }

}

void makeLeaveDecision(){
    if (rand_hard()/255 > PROBA_LEAVE ){
      printf("makeLeaveDecision %d\n" ,kilo_uid);
        mydata->state = REPELLING;
        mydata->curr_motion = rand_hard()%2 + 1;
        mydata->start_repelling = kilo_ticks;
    }
}
