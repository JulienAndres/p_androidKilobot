# coding: utf-8
import os
from analysis_script import *

NB_TEST = 40

MIN_DISTRIBUTE_PERCENT = 1.0
MAX_DISTRIBUTE_PERCENT = 1.0
STEP_DISTRIBUTE_PERCENT = 0.2

NAME_EXECUTABLE = "./main"
FILE_PATH = "results/final"
FILE_PATH_RESULTS = "./analysis_results"

with open("kilombo.json", "r") as config_file:
    data = config_file.read().split("\n")

#print data
dp = MIN_DISTRIBUTE_PERCENT
while(dp<= MAX_DISTRIBUTE_PERCENT):
    
    data[4] = "\t\"distributePercent\" : " + str(dp) + ","

    avg = 0
    loss = 0
    maxCluster = 0
    nbClusters = 0

    listAvgClusterSize = []
    listMaxClusterSize = []
    listLoss = []
    listDistIntraCluster = []

    for i in range(NB_TEST):
        data[1] =  "\t\"randSeed\" : " + str(i) + ","
        data[2] = "\t\"finalImage\" : \"" + FILE_PATH +str(i) + ".bmp\","
        data[3] = "\t\"imageName\" :  \"./results/movie" + str(i)  + "/f%04d.bmp\","
        #os.mkdir("./results/movie" + str(i))
        #print "\n".join(data)

        with open("kilombo.json", "w") as config_file:
            config_file.write("\n".join(data))

        os.system("./main")

        data_results = getRobotsFromFile("endstate.json")
        clusters = getClusters(data_results["bot_states"])

        result_run = getResultsCluster(clusters, 50)

        listAvgClusterSize.append(result_run[0])
        listMaxClusterSize.append(result_run[2])
        listLoss.append(result_run[3])
        listDistIntraCluster.append(getDistIntraCluster(clusters))

        avg += result_run[0]
        nbClusters += result_run[1]
        maxCluster += result_run[2]
        loss += result_run[3]

        #write_results(clusters, "analysis_results1")
        
    avg = float(float(avg)/float(NB_TEST))
    nbClusters = float(float(nbClusters)/float(NB_TEST))
    maxCluster = float(float(maxCluster)/float(NB_TEST))
    loss = float(float(loss)/float(NB_TEST))


    with open(FILE_PATH_RESULTS, "a") as file:
        file.write("------------------>   distribute percent : "+ str(dp) + "\n")
        file.write("nb clusters : "+ str(nbClusters)+ "\navg : "+ str(avg)+ "\nloss : "+ str(loss)+ "\nmaxCluster : "+ str(maxCluster) + "\n")
        file.write("max cluster -> min, 1er quartile, médiane, 3eme quartile, max : " + str(getBoxPlot(np.sort(listMaxClusterSize))) + "\n")
        file.write("avg cluster -> min, 1er quartile, médiane, 3eme quartile, max : " + str(getBoxPlot(np.sort(listAvgClusterSize))) + "\n")
        file.write("loss -> min, 1er quartile, médiane, 3eme quartile, max : " + str(getBoxPlot(np.sort(listLoss))) + "\n\n")
        file.write("distance intra cluster -> min, 1er quartile, médiane, 3eme quartile, max : " + str(getBoxPlot(np.sort(listDistIntraCluster))) + "\n")
        #file.write(str(np.sort(listMaxClusterSize)) + "\n" + str(np.sort(listAvgClusterSize)) + "\n" + str(np.sort(listLoss)) + "\n\n")
    dp += STEP_DISTRIBUTE_PERCENT
