#ifndef PROBABILITY_H
    #define PROBABILITY_H

    double getLinearProbJoining(int nbNeighbors);
    double getSigmoidProbJoining(int x, double error);
    double getLogProbJoining(int nbNeighbors);

    double getProbJoining();
    double getProbLeaving();
    void makeJoinDecision();
    void makeLeaveDecision();


#endif
