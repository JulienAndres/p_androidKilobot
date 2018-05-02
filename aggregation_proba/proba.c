#include "proba.h"
#include <kilombo.h>
#include <stdio.h>
#include <math.h>

void makeJoinDecision(){
    double p = getProbJoining();
    double random = rand()/(double)RAND_MAX;

    if (random < p){
        mydata->state = CONVERGING;
        mydata->direction =  rand_hard()%2 + 1;
    }

}

double getProbJoining(){
    uint8_t nbNeighborsBestNeighbor= mydata->neighbors[mydata->indexBestNeighbor].N_Neighbors;
    double p;

    switch(JOINING_PROB_METHOD){
        case LOG:
            p = getLogProbJoining(nbNeighborsBestNeighbor);
            break;
        case SIGMOID:
            p = getSigmoidProbJoining(nbNeighborsBestNeighbor, 0.01);
            break;
        case CONSTANT:
            p = CONSTANT_REPEL_PROBA;
            break;
        default:
            p = getLinearProbJoining(nbNeighborsBestNeighbor);
            break;
    }

    return (p<1)? p:1;
}

double getProbLeaving(){
    double p;
    double nbNeighbors = mydata->N_Neighbors;
    switch(LEAVING_PROB_METHOD){
        case LOG:
            p = getLogProbJoining(nbNeighbors);
            break;
        case SIGMOID:
            p = getSigmoidProbJoining(nbNeighbors, 0.01);
            break;
        case CONSTANT:
            p = 1 - CONSTANT_LEAVING_PROBA;
            break;
        default:
            p = getLinearProbJoining(nbNeighbors);
            break;
    }
    return 1-p;
}


void makeLeaveDecision(){
    if (rand_hard()/256 < getProbLeaving()){
        mydata->state = REPELLING;
        mydata->direction = rand_hard()%2 + 1;
        mydata->start_repelling = kilo_ticks;
    }
}
