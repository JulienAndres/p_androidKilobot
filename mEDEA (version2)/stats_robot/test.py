import numpy as np
import matplotlib.pyplot as plt
#lecture
test=[]
for i in range(70):
    test.append(open(str(i+1),"r"))
#========================================================================================   
#STATISTIQUE SUR PARENTS
robot=[[] for i in range(71)]
for i in range(59):
    f=0
    for file in test:
        print f
        tmp=file.readline()
        robot[f].append(int(tmp))
        f+=1
        
#    final={}.fromkeys(set(toRet),0)
#    for i in toRet:
#        final[i]+=1
#        
#    print toRet 
#    print final   
        
#========================================================================================
#STATISTIQUE SUR DEAD
#    
#toRet=[0 for i in range(59)]
#for i in range(59):
#    for file in test:
#        tmp=file.readline()
#        tmp=int(tmp)
#        toRet[i]+=tmp

#print toRet






#print toRet.index(99)

#mutation 66
#run1=[0, 0, 0, 2, 4, 7, 11, 12, 18, 22, 23, 26, 35, 44, 49, 54, 57, 60, 62, 64, 67, 70, 74, 78, 81, 90, 90, 90, 90, 90, 91, 93, 93, 93, 96, 96, 96, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
#run2=[0, 0, 0, 3, 9, 15, 19, 23, 31, 41, 46, 51, 56, 63, 67, 70, 73, 75, 79, 79, 81, 82, 83, 86, 86, 90, 92, 92, 92, 93, 93, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 96, 97, 97, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
#run3=[0, 0, 1, 6, 12, 16, 26, 33, 36, 41, 47, 54, 63, 67, 70, 77, 78, 82, 83, 83, 87, 88, 88, 91, 91, 95, 97, 97, 97, 97, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
#run4=[0, 0, 1, 4, 11, 19, 21, 25, 32, 36, 43, 47, 51, 56, 66, 70, 75, 75, 77, 78, 81, 85, 85, 88, 88, 93, 93, 93, 93, 93, 93, 95, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
#run5=[0, 0, 2, 9, 13, 22, 25, 29, 37, 44, 49, 54, 57, 62, 67, 71, 75, 76, 79, 81, 83, 84, 84, 87, 91, 97, 97, 97, 97, 97, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
#run6=[0, 0, 1, 3, 6, 12, 17, 27, 38, 45, 50, 51, 57, 62, 64, 68, 72, 73, 77, 79, 83, 85, 87, 90, 90, 94, 94, 94, 95, 95, 95, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
#
##mutation 0.2
#run7=[0, 0, 0, 4, 6, 10, 12, 17, 19, 22, 24, 26, 27, 34, 37, 40, 42, 44, 47, 47, 49, 51, 51, 54, 54, 58, 58, 60, 60, 60, 61, 64, 66, 67, 68, 72, 74, 74, 75, 75, 78, 78, 79, 79, 80, 80, 80, 81, 83, 84, 85, 86, 86, 86, 87, 87, 87, 87, 87]
#run8=[0, 0, 0, 6, 9, 9, 9, 10, 14, 17, 19, 21, 23, 31, 35, 37, 38, 40, 41, 45, 50, 52, 52, 56, 59, 65, 65, 65, 66, 66, 67, 70, 71, 71, 74, 74, 76, 77, 77, 77, 79, 79, 81, 85, 90, 91, 92, 94, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95]
#run9=[0, 0, 0, 4, 8, 8, 8, 8, 9, 11, 14, 15, 18, 22, 27, 33, 33, 33, 35, 35, 39, 40, 41, 44, 44, 48, 48, 50, 50, 51, 52, 56, 56, 56, 56, 57, 57, 57, 58, 58, 59, 59, 62, 62, 62, 62, 65, 66, 67, 69, 71, 75, 75, 76, 76, 77, 79, 81, 83]
#run10=[0, 0, 0, 3, 8, 9, 14, 16, 20, 24, 25, 31, 34, 39, 45, 51, 53, 54, 56, 59, 63, 65, 67, 72, 73, 77, 77, 77, 77, 77, 77, 79, 79, 79, 79, 79, 79, 79, 79, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 83, 84]
#
##mutation 0.4
#run11=[0, 0, 0, 1, 3, 7, 8, 10, 11, 16, 20, 23, 25, 31, 36, 40, 41, 45, 51, 51, 55, 57, 59, 64, 66, 71, 74, 74, 74, 74, 75, 77, 78, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 82, 82, 82, 82, 82, 84, 85, 85, 85, 88, 88, 88, 88, 88]
#run12=[0, 0, 0, 4, 7, 9, 10, 12, 16, 21, 23, 24, 26, 32, 34, 38, 41, 41, 43, 43, 47, 48, 49, 56, 60, 66, 67, 70, 70, 72, 73, 75, 79, 79, 79, 80, 81, 81, 81, 81, 82, 86, 88, 88, 90, 92, 92, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95, 95]
#run13=[0, 0, 0, 4, 8, 9, 10, 12, 14, 17, 21, 23, 29, 34, 38, 44, 47, 48, 49, 50, 52, 54, 54, 57, 59, 64, 65, 66, 67, 70, 72, 76, 77, 82, 84, 84, 87, 87, 88, 88, 90, 90, 90, 92, 92, 92, 92, 92, 93, 93, 97, 97, 99, 99, 99, 99, 99, 99, 99]
#run14=[0, 0, 0, 2, 5, 8, 9, 10, 12, 18, 19, 22, 24, 29, 32, 35, 36, 38, 40, 41, 45, 48, 52, 55, 55, 59, 60, 60, 61, 62, 63, 67, 68, 68, 68, 69, 69, 70, 71, 72, 73, 73, 75, 79, 80, 80, 80, 82, 87, 88, 90, 90, 90, 90, 93, 94, 94, 94, 94]
#
##mutation=0
#run15=[0, 0, 0, 1, 6, 9, 9, 9, 10, 13, 17, 19, 21, 25, 30, 35, 37, 41, 43, 46, 50, 54, 56, 60, 61, 67, 67, 67, 69, 69, 71, 73, 73, 73, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 77, 77, 77, 77, 77, 78, 78]
#run16=[0, 0, 0, 2, 5, 5, 5, 5, 8, 12, 15, 19, 23, 28, 31, 33, 33, 34, 37, 37, 39, 40, 40, 43, 43, 47, 47, 47, 47, 47, 47, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49]
#run17=[0, 0, 1, 2, 4, 4, 5, 6, 9, 13, 14, 16, 17, 21, 23, 25, 25, 25, 26, 26, 28, 29, 29, 32, 32, 36, 36, 36, 36, 36, 36, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38]
#run18=[0, 0, 1, 4, 9, 10, 12, 13, 15, 17, 20, 21, 22, 26, 29, 31, 32, 32, 33, 33, 35, 36, 36, 40, 40, 44, 44, 44, 44, 44, 44, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46]


#runTMP4=[]
#for i in range(len(run1)):
#    runTMP4.append(run15[i]+run16[i]+run17[i]+run18[i])
#    runTMP4[i]/=4
#
#
#runTMP3=[]
#for i in range(len(run1)):
#    runTMP3.append(run11[i]+run12[i]+run13[i]+run14[i])
#    runTMP3[i]/=4
#
#
#
#runTMP2=[]
#for i in range(len(run1)):
#    runTMP2.append(run7[i]+run8[i]+run9[i]+run10[i])
#    runTMP2[i]/=4
#
#
#
#runTMP=[]
#for i in range(len(run1)):
#    runTMP.append(run1[i]+run2[i]+run3[i]+run4[i]+run5[i]+run6[i])
#    runTMP[i]/=6
#    
#    
#    
#    
#   
#    
#plt.subplot(111)
#
#x=[i for i in range(1,len(run3)+1)]
#
#plt.plot(x, runTMP,label="$p = %.1f$" % 0.6)
#
#plt.plot(x, runTMP3,label='$p = %.1f$' % 0.4)
#
#plt.plot(x, runTMP2,label='$p = %.1f$' % 0.2)
#plt.plot(x, runTMP4,label='$p = %.1f$' % 0.0)
#
#
#plt.legend()
#
#plt.ylabel("Nombre de robot mort")
#plt.xlabel("Temps (minutes)")
#
#plt.show() 