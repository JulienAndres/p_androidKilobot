# coding: utf-8

import json
import math
import numpy as np

def  getRobotsFromFile(path):
	""" Return the dict corresponding to the robot's state from the given path
		  @params path: the file's path
		  @return the dict corresponding to the file
	"""
	with open(path) as file:
		data = file.read()
		state  = json.loads(data)
	return state

def getClusters(robotList):
	""" Returns the different clusters from the state list
		  @params the robot's state list
		  @return a list of all cluster, each cluster is a list of dict, where each dict represents a single robot.
	"""
	clusterList = []
	affectedList = []

	for  i in range(len(robotList)):
		robot = robotList[i]

		# if the robot is in a cluster and is not affected
		if  (robot["state"]["states"] == "SLEEPING"):

			if robot["ID"] in affectedList:
				cluster = getAffectedCluster(robot, clusterList)
				clusterList.remove(cluster)
			else:
				cluster = [robot]
				affectedList.append(robot["ID"])


			# we search to define the cluster for each robot
			for j in range(i+1, len(robotList)):

				if robotList[j]["state"]["states"] == "SLEEPING" and \
				   communicating(robot, robotList[j]) and\
				   robotList[j] not in cluster:

					if robotList[j]["ID"] in affectedList:
						oldCluster = getAffectedCluster(robotList[j], clusterList)
						clusterList.remove(oldCluster)
						cluster  = list( cluster + oldCluster )
#						print oldCluster is cluster, oldCluster == cluster

					else:
						cluster.append(robotList[j])
						affectedList.append(robotList[j]["ID"])

			if(cluster not in clusterList):
				clusterList.append(cluster)

	return clusterList

def getMaxCluster(clusters):
	"""
	Return the largest cluster in the list of clusters
	@params the list of clusters
	@return the largest cluster
	"""
	maxClusters = []
	for cluster in clusters:
		if len(cluster) > len(maxClusters) and len(cluster) > 1:
			maxClusters = [cluster]
		elif len(cluster) == len(maxClusters):
			maxClusters.append(cluster)
	return maxClusters

def getClusterSize(cluster):
	"""
	Return the distance intra cluster of the cluster
	@params The cluster for which the distance is calculated
	@return the distance intra cluster
	"""
	max_dist = 0.
	for i in range(len(cluster)):
		for j in range(i+1, len(cluster)):
			euclidDist = math.sqrt((cluster[i]["x_position"]-cluster[j]["x_position"])**2 + (cluster[i]["y_position"]-cluster[j]["y_position"])**2)
			if(euclidDist > max_dist):
				max_dist = euclidDist
	return max_dist

def getDistIntraCluster(clusters):
	"""
	Return the maximum distance intra cluster of all clusters
	@params The list of clusters
	@return the maximum distance intra cluster
	"""
	maxDist = 0
	for cluster in clusters:
		dist = getClusterSize(cluster)
		if(dist>maxDist):
			maxDist = dist
	return maxDist

def affected(robot, affectedList):
	"""
	Verify if the robot is affected into the list
	@params robot : the robot
			affectedList : the list into check if the robot is affected
	@return true if the robot is affected into the list, else false
	"""
	return robot["ID"] in affectedList

def communicating(robot, other):
	"""
	Check if 2 robots are communicating depending of their position
	@params robot : the first robot
			other : the second robot
	@return true if the distance if less than the maximum distance required to communicate, else false
	"""
	euclidDist =  math.sqrt( (other["x_position"]-robot["x_position"])**2 + (other["y_position"]-robot["y_position"])**2 )
	return (euclidDist <= 100)

def write_results(clusters, path):
	"""
	Write each cluster size into a file
	@params clusters : the list of clusters
			path : the path of the file
	"""
	file = open(path, "a")
	file.write(str(len(clusters)) + " clusters trouvés" + "\n")
	for cluster in clusters:
		file.write("Cluster de taille " + str(len(cluster)) + "\n")
	file.write("-------------------------" + "\n")
	file.close()

def getAffectedCluster(robot, clusters):
	"""
	Verify if a robot is affected in a cluster
	@params robot : a robot
			clusters : the list of all clusters
	@return true if the robot is in a cluster, else false
	"""
	for cluster in clusters:
		if robot in cluster:
			return cluster
	return None

def getResultsCluster(clusters, nbKilobots):
	"""
	calculate the average size of the clusters, the number of clusters,
	the maximum size of all clusters and the loss
	@params clusters : the list of all clusters
			nbKilobots : the number of robot used in simulation
	@return : the average size of the clusters, the number of clusters, the size of the largest cluster, the number of robots in any cluster
	"""
	avg = 0
	nbCluster = 0
	maxCluster = 0
	loss = nbKilobots

	for cluster in clusters:

		if(len(cluster) >1):
			avg += len(cluster)
			nbCluster +=1
			loss -= len(cluster)

			if len(cluster) > maxCluster:
				maxCluster = len(cluster)

	if(nbCluster >0):
		avg = avg/nbCluster

	return avg, nbCluster, maxCluster, loss

def getBoxPlot(values):
	""" Return the minimum, the first quartile, the median, the 3rd quartile and the maximum of a list
	@params values : a list of valuues
	@return minimum, 1st quartile, median, 3rd quartile, maximum
	"""
	return np.min(values), np.percentile(values, 25, interpolation = "nearest"), np.percentile(values, 50, interpolation = "nearest"), np.percentile(values, 75, interpolation = "nearest"), np.max(values)

if __name__ == "__main__":
	data= getRobotsFromFile("endstate.json")
	clusters = getClusters(data["bot_states"])
	print data["bot_states"][0]
	print "(average size cluster,nbCluster,largest,nbKilo no cluster)"
	print getResultsCluster(clusters,70)
#
#	print len(clusters), "clusters trouvés"
#	for cluster in clusters:
#		print "Cluster de taille ", len(cluster)
#		for el in cluster:
#			print "\t", el["ID"], "\t", el["state"]["states"]
