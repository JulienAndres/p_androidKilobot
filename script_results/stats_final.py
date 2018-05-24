import numpy as np
import matplotlib.pyplot as plt


plt.subplot(111)


### COVERAGE 
#ymoy=[6.5,6,8.25,20.25,25]
#ymin=[4,4,6,10,15]
#ymax=[13,9,11,35,34]
#x=[70,65,60,55,50]
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("taille moyenne cluster")
#plt.title("Couverture - taille max/moy/min cluster - distance demande")
#plt.show()
#
#
#
#ymoy=[14,15.5,7.25,5.25,2]
#ymin=[7,7,3,0,0]
#ymax=[22,23,13,12,5]
#x=[70,65,60,55,50]
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Nombre de Kilobot perdu")
#plt.title("Couverture - loss max/moy/min Kilobot - distance demande")
#plt.show()
#
#ymoy=[10.5,9.25,7.75,3.75,3.5]
#ymin=[7,7,6,2,2]
#ymax=[14,14,11,6,7]
#x=[70,65,60,55,50]
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Nombre de cluster")
#plt.title("Couverture - Nb max/moy/min Cluster - distance demande")
#plt.show()

## AGREGATION NAIVE
ymoy=[52,48.25,46.75,45.5,32.5]
ymin=[38,35,33,35,26]
ymax=[64,65,51,56,40]
x=[70,65,60,55,50]
plt.scatter(x, ymoy,marker='o')
plt.scatter(x, ymin,marker='_')
plt.scatter(x, ymax,marker='_')
plt.ylabel("taille moyenne cluster")
plt.title("Couverture - taille max/moy/min cluster - distance minimale d'agregation")
plt.show()



ymoy=[18,20.75,21.5,24.5,34.6]
ymin=[6,5,19,14,23]
ymax=[29,35,35,47,44]
x=[70,65,60,55,50]
plt.scatter(x, ymoy,marker='o')
plt.scatter(x, ymin,marker='_')
plt.scatter(x, ymax,marker='_')
plt.ylabel("Nombre de Kilobot perdu")
plt.title("Couverture - loss max/moy/min Kilobot - distance minimale d'agregation")
plt.show()

### AGREGATION
##avg_size
#ymoy = [5.5, 21, 7.25] 
#ymin = [4, 14, 4]
#ymax = [7, 35, 9]
#x = np.array([0,1,2])
#my_xticks = ['constant_proba','cluster_proba','cluster_proba_mix']
#plt.xticks(x, my_xticks)
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Taille du cluster")
#plt.title("Agrégation - Taille max/moy/min Cluster - méthode probabiliste")
#plt.show()
#
##nb_clusters
#ymoy = [9.75, 1.5, 9.25] 
#ymin = [9, 3, 7]
#ymax = [11, 1, 13]
#x = np.array([0,1,2])
#my_xticks = ['constant_proba','cluster_proba','cluster_proba_mix']
#plt.xticks(x, my_xticks)
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Nombre de clusters")
#plt.title("Agrégation - Nombre max/moy/min de clusters - méthode probabiliste")
#plt.show()
#
##nb_kilobots_clusters
#ymoy = [12.5, 41.25, 8.25] 
#ymin = [10, 35, 5]
#ymax = [15, 52, 11]
#x = np.array([0,1,2])
#my_xticks = ['constant_proba','cluster_proba','cluster_proba_mix']
#plt.xticks(x, my_xticks)
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Nombre de kilobots par cluster")
#plt.title("Agrégation - Nombre max/moy/min de kilobots par cluster - méthode probabiliste")
#plt.show()

#ymoy=[]
#ymin=
#ymax=
#x=
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Plus grand cluster(Nb de robot)")
#plt.title("Couverture - Nb max/moy/min robot par cluster - distance demande")
#plt.show()

## COVERAGE 
#groupe
ymoy=[6.4,9.8,15.2,35,37.6]
ymin=[5,7,10,15,22]
ymax=[8,11,23,69,67]
x=[70,65,60,55,50]
plt.scatter(x, ymoy,marker='o')
plt.scatter(x, ymin,marker='_')
plt.scatter(x, ymax,marker='_')
plt.ylabel("taille moyenne cluster")
plt.title("Couverture - taille max/moy/min cluster - distance demande")
plt.show()



ymoy=[8.4,8.8,4.3,2.6,3.2]
ymin=[1,1,1,1,1]
ymax=[21,25,8,8,6]
x=[70,65,60,55,50]
plt.scatter(x, ymoy,marker='o')
plt.scatter(x, ymin,marker='_')
plt.scatter(x, ymax,marker='_')
plt.ylabel("Nombre de Kilobot perdu")
plt.title("Couverture - loss max/moy/min Kilobot - distance demande")
plt.show()

ymoy=[9.6,6.2,4.8,2.4,2]
ymin=[8,4,3,1,1]
ymax=[11,8,7,4,3]
x=[70,65,60,55,50]
plt.scatter(x, ymoy,marker='o')
plt.scatter(x, ymin,marker='_')
plt.scatter(x, ymax,marker='_')
plt.ylabel("Nombre de cluster")
plt.title("Couverture - Nb max/moy/min Cluster - distance demande")
plt.show()


## Analyse de la proba cluster_proba en fonction de la taille du cluster demandé
# avg_size
#ymoy = [24.75, 19.75, 18.25, 11]
#ymin = [17, 10, 10, 0]
#ymax = [35, 30, 27, 23]
#myticks = [5, 6, 7, 8]
#x = np.array([0, 1, 2, 3])
#plt.xticks(x, myticks)
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Taille du cluster")
#plt.xlabel("Taille \"big\" cluster")
#plt.title("Agrégation - Taille max/moy/min Cluster - Taille \"big\" cluster")
#plt.show()
#
## nb_clusters
#ymoy = [1, 1, 1, 0.68]
#ymin = [1, 1, 1, 0]
#ymax = [1, 1, 1, 1]
#myticks = [5, 6, 7, 8]
#x = np.array([0, 1, 2, 3])
#plt.xticks(x, myticks)
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Nombre de clusters")
#plt.xlabel("Taille \"big\" cluster")
#plt.title("Agrégation - Nombre max/moy/min de clusters - Taille \"big\" cluster")
#plt.show()
#
## loss
#ymoy = [45.25, 50.25, 51.75, 59]
#ymin = [35, 40, 43, 47]
#ymax = [53, 60, 60, 70]
#myticks = [5, 6, 7, 8]
#x = np.array([0, 1, 2, 3])
#plt.xticks(x, myticks)
#plt.scatter(x, ymoy,marker='o')
#plt.scatter(x, ymin,marker='_')
#plt.scatter(x, ymax,marker='_')
#plt.ylabel("Nombre de Kilobot perdu")
#plt.xlabel("Taille \"big\" cluster")
#plt.title("Agrégation - loss max/moy/min Kilobots - Taille \"big\" cluster")
#plt.show()



##### ALGORITHM COMPARISON
## INFINITE
#plt.boxplot([
#          (11, 18, 23, 27, 32),
#          [25, 30, 34, 36, 44]
#    ])
#
#plt.gca().xaxis.set_ticklabels(['Parametrized Probabilistic Aggregation', 'Beeclust'])
#plt.ylim(0, 51)
#plt.ylabel("Number of robots")
#plt.title("Loss - Algorithms Comparison - Infinite environment ")
#plt.show()


#plt.boxplot([
#           (12, 19, 21, 24, 37),
#          [2, 5, 7, 8, 15]
#    ])
#
#plt.gca().xaxis.set_ticklabels(['Parametrized Probabilistic Aggregation', 'Beeclust'])
#plt.ylim(0, 51)
#plt.ylabel("Number of robots")
#plt.title("Max Cluster Size - Algorithms Comparison - Infinite environment ")
#plt.show()
#
#
#plt.boxplot([
#          (11, 16, 19, 24, 37),
#          [2, 3, 4, 5, 9]
#    ])
#
#plt.gca().xaxis.set_ticklabels(['Parametrized Probabilistic Aggregation', 'Beeclust'])
#plt.ylim(0, 51)
#plt.ylabel("Number of robots")
#plt.title("Average Cluster Size - Algorithms Comparison - Infinite environment ")
#plt.show()


## CLOSED
# plt.boxplot([
#           (1, 5, 9, 11, 18),
#          (3, 6, 8, 9, 14)
#     ])

# plt.gca().xaxis.set_ticklabels(['Parametrized Probabilistic Aggregation', 'Beeclust'])
# plt.ylim(0, 51)
# plt.ylabel("Number of robots")
# plt.title("Loss - Algorithms Comparison - Infinite environment ")
# plt.show()


# plt.boxplot([
#            (15, 22, 27, 32, 42),
#           (6, 8, 9, 11, 20)
#     ])

# plt.gca().xaxis.set_ticklabels(['Parametrized Probabilistic Aggregation', 'Beeclust'])
# plt.ylim(0, 51)
# plt.ylabel("Number of robots")
# plt.title("Max Cluster Size - Algorithms Comparison - Infinite environment ")
# plt.show()


# plt.boxplot([
#           (12, 20, 22, 24, 42),
#          (3, 4, 4, 4, 7)
#     ])

# plt.gca().xaxis.set_ticklabels(['Parametrized Probabilistic Aggregation', 'Beeclust'])
# plt.ylim(0, 51)
# plt.ylabel("Number of robots")
# plt.title("Average Cluster Size - Algorithms Comparison - Infinite environment ")
# plt.show()

##### SPARCITY 

## CLOSED

# plt.boxplot([
#           [17, 24, 29, 37, 45],
#           [16, 22, 27, 32, 42],
#           [15, 22, 26, 29, 38],   
#           [3, 20, 25, 27, 37],
#           [13, 21, 24, 27, 34],
#           [2, 19, 22, 25, 32],
#           [0, 20, 23, 26, 32],
#           [9, 18, 20, 24, 31], 
#           [2, 17, 21, 25, 35], 
#           [0, 17, 24, 26, 35],
#     ])

# plt.gca().xaxis.set_ticklabels(['1.0', '1.2', '1.4', '1.6', '1.8', '2.0', '2.2', '2.4', '2.6', '2.8'])
# plt.ylim(0, 51)
# plt.xlabel("Sparcity")
# plt.ylabel("Number of robots")
# plt.title("Max Cluster Size - Sparcity - Closed environment ")
# plt.show()



# plt.boxplot([
#           [14, 20, 21, 35, 45],
#           [9, 18, 21, 32, 42],
#           [12, 19, 20, 26, 38],   
#           [3, 15, 19, 24, 37],
#           [11, 16, 20, 26, 34],
#           [2, 14, 19, 21, 32],
#           [0, 14, 20, 21, 30],
#           [6, 14, 18, 22, 31], 
#           [2, 14, 18, 24, 35], 
#           [0, 14, 19, 21, 35],
#     ])

# plt.gca().xaxis.set_ticklabels(['1.0', '1.2', '1.4', '1.6', '1.8', '2.0', '2.2', '2.4', '2.6', '2.8'])
# plt.ylim(0, 51)
# plt.xlabel("Sparcity")
# plt.ylabel("Number of robots")
# plt.title("Average Cluster Size - Sparcity - Closed environment ")
# plt.show()


# plt.boxplot([
#           [3, 7, 9, 11, 21],
#           [5, 10, 13, 17, 26],
#           [4, 10, 12, 17, 26],   
#           [5, 13, 18, 25, 47],
#           [3, 14, 19, 24, 35],
#           [3, 9, 16, 23, 48],
#           [7, 10, 16, 22, 50],
#           [5, 12, 22, 26, 40], 
#           [0, 15, 21, 24, 48], 
#           [5, 10, 20, 26, 50],
#     ])

# plt.gca().xaxis.set_ticklabels(['1.0', '1.2', '1.4', '1.6', '1.8', '2.0', '2.2', '2.4', '2.6', '2.8'])
# plt.ylim(0, 51)
# plt.xlabel("Sparcity")
# plt.ylabel("Number of robots")
# plt.title("Loss - Sparcity - Closed environment ")
# plt.show()


## INFINITE
# plt.boxplot([
#     [12, 17.875, 23, 33.25, 42],# 0.8
#     [11, 13.83, 16, 20.25, 35],# 1.0
#     [0, 15, 17, 19.5, 27],# 1.2
#     [0, 11.75, 15, 20, 25],# 1.4
#     [0, 0, 0, 14.25, 28]# 1.6
#     ])
# plt.ylim(0, 51)
# plt.xlabel("Sparcity")
# plt.ylabel("Number of robots")
# plt.gca().xaxis.set_ticklabels(['0.8', '1.0', '1.2', '1.4', '1.6'])
# plt.title("Average Cluster Size - Sparcity - Infinite environment ")
# plt.show()

# plt.boxplot([    
#         [4, 10.75, 14.5, 16.25, 21],# LS0.8
#         [10, 17.5, 20, 24.25, 39],# LS1.0
#         [16, 23.75, 30, 33.25, 50],#LS1.2
#         [17, 28, 33, 38.25, 50],# LS1.4
#         [22, 35.75, 50, 50, 50]# LS1.6
#         ])
# plt.ylim(0, 51)
# plt.xlabel("Sparcity")
# plt.ylabel("Number of robots")
# plt.gca().xaxis.set_ticklabels(['0.8', '1.0', '1.2', '1.4', '1.6'])
# plt.title("Loss - Sparcity - Infinite environment ")
# plt.show()


# plt.boxplot([
#     [12, 22, 30, 33.75, 42],# 0.8
#     [11, 14, 17, 24.25, 31],# 1.0
#     [0, 15, 17.5, 19.5, 27],# 1.2
#     [0, 11.75, 16, 20.25, 25],# 1.4
#     [0, 0, 0, 14.25, 28]# 1.6
#     ])
# plt.ylim(0, 51)
# plt.xlabel("Sparcity")
# plt.ylabel("Number of robots")
# plt.gca().xaxis.set_ticklabels(['0.8', '1.0', '1.2', '1.4', '1.6'])
# plt.title("Max Cluster Size - Sparcity -Infinite environment ")
# plt.show()


### ROBUST_CLUSTER_SIZE

# plt.boxplot([
#            [11, 12.5, 20, 28, 42],# LL5
#            [12, 14.8, 20, 31.25, 41],# LL8
#            [13, 17.375, 19, 23.5, 35],# LL10          
#            [0, 18, 21, 26.5, 32],# LL12
#     ])

# plt.gca().xaxis.set_ticklabels(['5', '8', '10', '12', '15'])
# plt.ylim(0, 51)
# plt.title("Average Cluster Size - ROBUST_CLUSTER_SIZE parameter")
# plt.show()

# plt.boxplot([
#         [14, 21, 27.5, 37.5, 42],# LL5
#         [13, 22.5, 25.5, 31.25, 41],# LL8
#         [16, 19.75, 22, 28, 35],# LL10
#         [0, 19.5, 22.5, 27.25, 32],# LL12
#         [0, 0, 0, 23.5, 27],# LL15
#     ])

# plt.gca().xaxis.set_ticklabels(['5', '8', '10', '12', '15'])
# plt.ylim(0, 51)
# plt.title("Max cluster size - ROBUST_CLUSTER_SIZE parameter ")
# plt.show()

# plt.boxplot([
#           [0, 3.75, 7.5, 10.25, 14], #LL5
#           [5, 8.75, 10.5, 14, 21], #LL8
#           [6, 12.75, 15, 16.25, 29], #LL10
#           [4, 18, 23, 29.25, 50], #LL12
#           [23, 26.5, 50, 50, 50], #LL15
#     ])

# plt.gca().xaxis.set_ticklabels(['5', '8', '10', '12', '15'])
# plt.ylim(0, 51)
# plt.title("Loss - ROBUST_CLUSTER_SIZE parameter ")
# plt.show()



### PROBABILITY MEASURES




# plt.boxplot([
#     (11, 18, 20, 21, 28),
#     (12, 19, 21, 24, 37),
#     (14, 18, 21, 23, 31),
#     (12, 16, 19, 23, 34),
#     (8, 13, 18, 20, 29)
#     ])

# plt.gca().xaxis.set_ticklabels(['Linear\nLinear', 'Linear\nSigmoid' , 'Sigmoid\nLinear', 'Sigmoid\nSigmoid', 'Constant\nConstant'])
# plt.ylim(0, 51)
# plt.ylabel("Number of robots")
# plt.title("Max Cluster Size - Probability measures - Infinite environment ")
# plt.show()


# plt.boxplot([
#     (11, 16, 17, 20, 28),
#     (11, 16, 19, 24, 37),
#     (12, 15, 17, 20, 31),
#     (10, 14, 18, 19, 34),
#     (3, 5, 7, 8, 12)
#     ])

# plt.gca().xaxis.set_ticklabels(['Linear\nLinear', 'Linear\nSigmoid', 'Sigmoid\nLinear', 'Sigmoid\nSigmoid', 'Constant\nConstant'])
# plt.ylim(0, 51)
# plt.ylabel("Number of robots")
# plt.title("Average Cluster Size - Probability measures - Infinite environment ")
# plt.show()



# plt.boxplot([
#     (12, 17, 21, 25, 39),
#     (11, 18, 23, 27, 32),
#     (5, 14, 19, 20, 30),
#     (8, 14, 19, 23, 31),
#     (1, 2, 4, 5, 7)
#     ])

# plt.gca().xaxis.set_ticklabels(['Linear\nLinear', 'Linear\nSigmoid', 'Sigmoid\nLinear',   'Sigmoid\nSigmoid', 'Constant\nConstant'])
# plt.ylim(0, 51)
# plt.ylabel("Number of robots")
# plt.title("Loss - Probability measures - Infinite environment ")
# plt.show()