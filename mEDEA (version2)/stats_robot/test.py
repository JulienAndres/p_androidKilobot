import numpy as np
import matplotlib.pyplot as plt
#lecture
test=[]
for i in range(69):
    test.append(open(str(i+1),"r"))
    
    
#========================================================================================   
#STATISTIQUE SUR GENOME
robot=[[] for i in range(69)]
for i in range(59):
    f=0
    for file in test:
        tmp=file.readline()
        robot[f].append(int(tmp))
        f+=1

toRet=[]
yep=dict()
for i in range(59):
    tmp=[j[i] for j in robot]
    final={}.fromkeys(set(tmp),0)
    for k in tmp:
        final[k]+=1
    if -1 in final.keys() : del final[-1]
    toRet.append(len(final))

print toRet
#mutation 0
run1=[69, 69, 36, 22, 19, 17, 16, 14, 13, 11, 11, 10, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6]
run2=[69, 69, 35, 25, 23, 19, 17, 16, 12, 11, 11, 11, 10, 10, 10, 10, 10, 9, 8, 8, 8, 8, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
run3=[69, 69, 33, 21, 17, 16, 14, 12, 11, 9, 8, 6, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
run4=[68, 68, 33, 20, 16, 16, 12, 10, 10, 8, 8, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]



#mutation 0.2
run5=[69, 69, 42, 33, 32, 31, 31, 32, 31, 28, 26, 30, 28, 33, 30, 29, 19, 23, 22, 25, 21, 16, 17, 17, 21, 22, 22, 14, 17, 19, 15, 16, 10, 14, 13, 12, 10, 11, 12, 13, 13, 12, 13, 12, 13, 14, 10, 15, 10, 11, 11, 8, 8, 7, 9, 11, 13, 9, 9]
run6=[69, 69, 43, 40, 37, 33, 33, 31, 27, 27, 33, 33, 30, 28, 27, 29, 32, 27, 28, 34, 26, 25, 26, 24, 23, 23, 20, 17, 19, 18, 21, 22, 24, 25, 21, 17, 16, 16, 14, 13, 11, 13, 11, 13, 11, 12, 10, 11, 12, 10, 11, 10, 7, 10, 6, 7, 6, 7, 10]
run7=[69, 69, 45, 42, 34, 28, 27, 28, 27, 22, 27, 18, 24, 23, 20, 24, 22, 20, 19, 17, 15, 14, 13, 18, 18, 14, 12, 9, 12, 10, 12, 10, 10, 14, 11, 8, 7, 7, 5, 5, 5, 4, 3, 2, 2, 3, 2, 2, 2, 2, 1, 2, 2, 1, 1, 2, 2, 3, 3]
run8=[69, 69, 48, 38, 40, 37, 31, 34, 32, 32, 29, 28, 29, 24, 24, 22, 26, 19, 23, 22, 21, 20, 18, 20, 21, 16, 19, 16, 18, 17, 18, 15, 11, 12, 12, 15, 13, 13, 15, 12, 10, 10, 12, 11, 11, 10, 9, 9, 8, 9, 10, 6, 6, 5, 7, 6, 4, 7, 3]

#mutation 0.4
run9=[68, 68, 43, 44, 51, 45, 45, 45, 47, 44, 39, 42, 37, 37, 33, 34, 32, 27, 34, 31, 28, 28, 27, 20, 26, 21, 20, 16, 15, 16, 16, 16, 20, 15, 11, 12, 14, 12, 11, 10, 11, 12, 12, 12, 10, 10, 9, 7, 7, 10, 9, 8, 5, 4, 6, 7, 5, 5, 7]
run10=[69, 69, 45, 42, 47, 46, 42, 39, 39, 38, 43, 36, 37, 38, 35, 29, 30, 29, 28, 30, 31, 31, 28, 27, 24, 19, 18, 20, 18, 21, 19, 20, 16, 17, 12, 11, 10, 6, 7, 7, 5, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
run11=[69, 69, 57, 48, 45, 46, 43, 33, 40, 32, 37, 27, 30, 27, 26, 24, 22, 23, 20, 18, 11, 15, 11, 10, 13, 10, 6, 8, 9, 9, 7, 5, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
run12=[69, 69, 49, 45, 38, 47, 37, 46, 46, 44, 45, 44, 44, 36, 31, 34, 37, 30, 33, 35, 31, 31, 31, 26, 24, 14, 17, 14, 15, 13, 12, 9, 8, 10, 9, 7, 3, 3, 3, 3, 3, 3, 2, 3, 2, 3, 2, 2, 1, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2]

#mutation 0.6
run13=[69, 69, 60, 64, 59, 59, 47, 53, 50, 46, 46, 48, 39, 45, 47, 40, 47, 48, 41, 44, 39, 39, 36, 31, 27, 28, 31, 26, 25, 23, 23, 23, 19, 19, 17, 19, 18, 13, 12, 14, 10, 9, 9, 6, 8, 8, 8, 7, 5, 5, 5, 5, 5, 3, 3, 3, 3, 4, 4]
run14=[68, 68, 59, 57, 58, 59, 57, 55, 54, 45, 48, 48, 46, 44, 42, 37, 37, 35, 30, 33, 33, 32, 33, 29, 28, 25, 25, 22, 23, 17, 17, 18, 17, 18, 15, 14, 11, 8, 8, 9, 5, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
run15=[69, 69, 62, 59, 60, 59, 44, 48, 49, 44, 48, 43, 40, 43, 43, 41, 39, 41, 37, 37, 35, 31, 23, 25, 25, 22, 22, 23, 22, 21, 19, 18, 17, 19, 17, 13, 14, 12, 11, 10, 5, 5, 6, 6, 4, 4, 3, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
run16=[68, 68, 59, 60, 58, 53, 55, 51, 49, 47, 46, 42, 44, 42, 39, 31, 35, 35, 29, 28, 26, 25, 23, 19, 16, 13, 11, 9, 6, 8, 7, 8, 7, 4, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0]


runTMP=[]
for i in range(len(run1)):
    runTMP.append(run1[i]+run2[i]+run3[i]+run4[i])
    runTMP[i]/=4.0

runTMP2=[]
for i in range(len(run1)):
    runTMP2.append(run5[i]+run6[i]+run7[i]+run8[i])
    runTMP2[i]/=4.0

                    
runTMP4=[]
for i in range(len(run1)):
    runTMP4.append(run9[i]+run10[i]+run11[i]+run12[i])
    runTMP4[i]/=4.0


runTMP3=[]
for i in range(len(run1)):
    runTMP3.append(run13[i]+run14[i]+run15[i]+run16[i])
    runTMP3[i]/=4.0


    
plt.subplot(111)

x=[i for i in range(1,len(run3)+1)]



plt.plot(x, runTMP3,label='$p = %.1f$' % 0.6)
plt.plot(x, runTMP4,label="$p = %.1f$" % 0.4)
plt.plot(x, runTMP2,label='$p = %.1f$' % 0.2)
plt.plot(x, runTMP,label="$p = %.1f$" % 0.0)

plt.legend()

plt.ylabel("Nombre de parent a l'origine des genomes vivants")
plt.xlabel("Temps (minutes)")

plt.show() 

x=[i for i in range(20,len(run3))]
print len(x)
print len(runTMP3[10:])

plt.plot(x, runTMP3[20:],label='$p = %.1f$' % 0.6)
plt.plot(x, runTMP4[20:],label="$p = %.1f$" % 0.4)
plt.plot(x, runTMP2[20:],label='$p = %.1f$' % 0.2)
plt.plot(x, runTMP[20:],label="$p = %.1f$" % 0.0)

plt.legend()

plt.ylabel("Nombre de parent a l'origine des genomes vivants")
plt.xlabel("Temps (minutes)")

plt.show() 

#========================================================================================   
##STATISTIQUE SUR PARENTS
#robot=[[] for i in range(69)]
#for i in range(59):
#    f=0
#    for file in test:
#        tmp=file.readline()
#        robot[f].append(int(tmp))
#        f+=1
#
#toRet=[]
#yep=dict()
#for i in range(59):
#    tmp=[j[i] for j in robot]
#    final={}.fromkeys(set(tmp),0)
#    for k in tmp:
#        final[k]+=1
#    if -1 in final.keys() : del final[-1]
#    toRet.append(len(final))
#
#print toRet
#    
##mutation 0
#run1=[69, 69, 32, 20, 16, 13, 11, 11, 11, 10, 10, 10, 10, 8, 8, 7, 7, 7, 7, 7, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4]
#run2=[69, 69, 36, 22, 18, 13, 12, 11, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7]
#run3=[69, 69, 33, 23, 22, 19, 16, 11, 9, 8, 8, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
#run4=[69, 69, 36, 28, 19, 18, 18, 17, 15, 14, 13, 11, 8, 8, 7, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
#
##mutation 0.2
#run5=[69, 69, 34, 23, 20, 18, 16, 16, 15, 15, 13, 13, 13, 12, 10, 10, 9, 8, 8, 7, 7, 7, 7, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#run6=[69, 69, 38, 30, 25, 22, 17, 14, 13, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
#run7=[69, 69, 31, 20, 18, 16, 12, 10, 10, 9, 9, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1]
#run8=[69, 69, 37, 28, 21, 17, 13, 12, 11, 9, 8, 7, 5, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
#
#    
##mutation 0.4
#run9=[69, 69, 39, 30, 27, 23, 20, 16, 15, 13, 13, 12, 10, 10, 7, 6, 6, 6, 6, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]
#run10=[69, 69, 33, 23, 18, 15, 15, 13, 12, 11, 11, 9, 9, 7, 6, 6, 6, 6, 6, 6, 6, 5, 5, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1]
#run11=[69, 69, 36, 24, 19, 17, 16, 12, 12, 12, 10, 9, 8, 8, 7, 7, 7, 6, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1]
#run12=[69, 69, 28, 20, 14, 11, 10, 10, 10, 10, 9, 8, 7, 6, 6, 6, 6, 5, 5, 4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
#
#    
##mutation 0.6
#        
#run13=[69, 69, 36, 26, 19, 16, 12, 11, 10, 9, 9, 8, 8, 8, 8, 8, 8, 6, 5, 5, 5, 5, 5, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0]
#run14=[69, 69, 34, 24, 18, 17, 15, 13, 11, 11, 11, 10, 9, 9, 8, 8, 6, 6, 5, 5, 5, 4, 4, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#run15=[69, 69, 33, 22, 19, 18, 15, 13, 12, 10, 10, 9, 8, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 3, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
#run16=[69, 69, 35, 24, 21, 17, 14, 13, 12, 11, 10, 9, 8, 7, 7, 7, 7, 7, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#
#
#
#runTMP=[]
#for i in range(len(run1)):
#    runTMP.append(run1[i]+run2[i]+run3[i]+run4[i])
#    runTMP[i]/=4.0
#
#runTMP2=[]
#for i in range(len(run1)):
#    runTMP2.append(run5[i]+run6[i]+run7[i]+run8[i])
#    runTMP2[i]/=4.0
#
#                    
#runTMP4=[]
#for i in range(len(run1)):
#    runTMP4.append(run9[i]+run10[i]+run11[i]+run12[i])
#    runTMP4[i]/=4.0
#
#
#runTMP3=[]
#for i in range(len(run1)):
#    runTMP3.append(run13[i]+run14[i]+run15[i]+run16[i])
#    runTMP3[i]/=4.0
#
#
#    
#plt.subplot(111)
#
#x=[i for i in range(1,len(run3)+1)]
#
#
#
#plt.plot(x, runTMP3,label='$p = %.1f$' % 0.6)
#plt.plot(x, runTMP4,label="$p = %.1f$" % 0.4)
#plt.plot(x, runTMP2,label='$p = %.1f$' % 0.2)
#plt.plot(x, runTMP,label="$p = %.1f$" % 0.0)
#
#plt.legend()
#
#plt.ylabel("Nombre de parent a l'origine des genomes vivants")
#plt.xlabel("Temps (minutes)")
#
#plt.show() 
#
#x=[i for i in range(10,len(run3))]
#print len(x)
#print len(runTMP3[10:])
#
#plt.plot(x, runTMP3[10:],label='$p = %.1f$' % 0.6)
#plt.plot(x, runTMP4[10:],label="$p = %.1f$" % 0.4)
#plt.plot(x, runTMP2[10:],label='$p = %.1f$' % 0.2)
#plt.plot(x, runTMP[10:],label="$p = %.1f$" % 0.0)
#
#plt.legend()
#
#plt.ylabel("Nombre de parent a l'origine des genomes vivants")
#plt.xlabel("Temps (minutes)")
#
#plt.show() 
#
#        
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

##mutation 66
##run1=[0, 0, 0, 2, 4, 7, 11, 12, 18, 22, 23, 26, 35, 44, 49, 54, 57, 60, 62, 64, 67, 70, 74, 78, 81, 90, 90, 90, 90, 90, 91, 93, 93, 93, 96, 96, 96, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
##run2=[0, 0, 0, 3, 9, 15, 19, 23, 31, 41, 46, 51, 56, 63, 67, 70, 73, 75, 79, 79, 81, 82, 83, 86, 86, 90, 92, 92, 92, 93, 93, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 95, 96, 97, 97, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
##run3=[0, 0, 1, 6, 12, 16, 26, 33, 36, 41, 47, 54, 63, 67, 70, 77, 78, 82, 83, 83, 87, 88, 88, 91, 91, 95, 97, 97, 97, 97, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
##run4=[0, 0, 1, 4, 11, 19, 21, 25, 32, 36, 43, 47, 51, 56, 66, 70, 75, 75, 77, 78, 81, 85, 85, 88, 88, 93, 93, 93, 93, 93, 93, 95, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
##run5=[0, 0, 2, 9, 13, 22, 25, 29, 37, 44, 49, 54, 57, 62, 67, 71, 75, 76, 79, 81, 83, 84, 84, 87, 91, 97, 97, 97, 97, 97, 97, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
##run6=[0, 0, 1, 3, 6, 12, 17, 27, 38, 45, 50, 51, 57, 62, 64, 68, 72, 73, 77, 79, 83, 85, 87, 90, 90, 94, 94, 94, 95, 95, 95, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99, 99]
#
## run1 = [0, 0, 1, 1, 2, 3, 4, 8, 10, 12, 17, 22, 23, 23, 26, 27, 30, 33, 36, 38, 38, 39, 39, 39, 41, 41, 43, 43, 44, 45, 48, 50, 50, 52, 52, 53, 53, 53, 53, 54, 54, 56, 57, 59, 60, 60, 63, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67]
## run2 = [0, 0, 0, 2, 3, 3, 5, 7, 10, 14, 15, 17, 19, 22, 28, 29, 30, 32, 36, 38, 39, 40, 40, 41, 42, 43, 44, 47, 48, 49, 51, 52, 55, 55, 56, 62, 62, 63, 63, 63, 65, 65, 65, 67, 67, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69]
## run3 = [0, 0, 0, 1, 2, 6, 8, 9, 12, 15, 16, 17, 19, 19, 19, 21, 24, 24, 25, 26, 27, 30, 31, 31, 34, 37, 37, 42, 45, 46, 46, 46, 46, 50, 52, 53, 53, 53, 55, 55, 59, 59, 59, 61, 63, 63, 63, 63, 63, 63, 63, 64, 64, 65, 67, 69, 69, 69, 69]
## run4 = [0, 0, 0, 3, 6, 6, 7, 10, 13, 17, 18, 21, 23, 25, 26, 28, 30, 31, 34, 35, 37, 38, 38, 38, 39, 40, 41, 43, 45, 49, 51, 51, 56, 59, 60, 63, 63, 63, 66, 66, 66, 66, 66, 67, 67, 67, 67, 67, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69]
## run5 = [0, 0, 0, 5, 6, 8, 11, 14, 16, 17, 19, 20, 21, 25, 27, 27, 30, 33, 34, 36, 37, 37, 39, 41, 44, 47, 51, 53, 60, 60, 62, 63, 63, 63, 63, 63, 65, 65, 65, 66, 66, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 67, 69, 69, 69]
## run6 = [0, 0, 0, 1, 1, 3, 3, 4, 5, 6, 7, 10, 11, 11, 13, 16, 17, 18, 20, 22, 26, 27, 27, 28, 29, 32, 35, 37, 38, 40, 40, 41, 43, 45, 47, 47, 51, 51, 53, 54, 57, 61, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 66]
#
#run1 = [0, 0, 0, 2, 5, 7, 7, 8, 9, 11, 13, 14, 14, 15, 16, 19, 21, 21, 22, 22, 23, 27, 30, 30, 34, 35, 37, 37, 37, 38, 40, 40, 44, 45, 45, 49, 49, 49, 49, 50, 51, 51, 52, 52, 52, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54, 54]
#run2 = [0, 0, 0, 1, 2, 2, 4, 6, 6, 8, 9, 9, 9, 11, 11, 12, 14, 16, 17, 21, 27, 29, 32, 33, 35, 41, 44, 46, 47, 49, 51, 52, 52, 52, 52, 54, 54, 60, 60, 62, 63, 63, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 64, 65, 65, 65, 65, 65]
#run3 = [0, 0, 1, 3, 3, 5, 8, 10, 11, 12, 13, 16, 17, 18, 18, 20, 20, 22, 23, 25, 27, 29, 34, 36, 38, 42, 44, 44, 47, 50, 52, 54, 55, 56, 58, 58, 58, 58, 58, 58, 58, 59, 60, 60, 61, 62, 65, 66, 67, 67, 67, 69, 69, 69, 69, 69, 69, 69, 69]
#run4 = [0, 0, 0, 3, 4, 5, 6, 6, 7, 7, 10, 11, 13, 14, 15, 16, 16, 16, 17, 18, 21, 25, 28, 28, 30, 32, 34, 36, 39, 40, 42, 42, 44, 45, 49, 50, 50, 50, 50, 51, 51, 53, 53, 54, 55, 56, 56, 58, 59, 59, 61, 61, 63, 63, 63, 63, 63, 63, 63]
#run5 = [0, 0, 0, 2, 3, 4, 7, 9, 11, 13, 14, 16, 20, 20, 21, 22, 23, 25, 29, 30, 32, 32, 34, 37, 38, 41, 45, 48, 51, 54, 55, 58, 58, 59, 59, 59, 59, 59, 59, 61, 63, 63, 63, 64, 65, 67, 67, 67, 67, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69]
#run6 = [0, 0, 0, 2, 3, 9, 13, 14, 18, 18, 19, 21, 26, 28, 29, 31, 34, 35, 36, 41, 43, 45, 49, 49, 49, 54, 58, 58, 61, 62, 62, 64, 66, 66, 67, 67, 67, 67, 67, 67, 67, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69]
#
#
###mutation 0.2
##run7=[0, 0, 0, 4, 6, 10, 12, 17, 19, 22, 24, 26, 27, 34, 37, 40, 42, 44, 47, 47, 49, 51, 51, 54, 54, 58, 58, 60, 60, 60, 61, 64, 66, 67, 68, 72, 74, 74, 75, 75, 78, 78, 79, 79, 80, 80, 80, 81, 83, 84, 85, 86, 86, 86, 87, 87, 87, 87, 87]
##run8=[0, 0, 0, 6, 9, 9, 9, 10, 14, 17, 19, 21, 23, 31, 35, 37, 38, 40, 41, 45, 50, 52, 52, 56, 59, 65, 65, 65, 66, 66, 67, 70, 71, 71, 74, 74, 76, 77, 77, 77, 79, 79, 81, 85, 90, 91, 92, 94, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95]
##run9=[0, 0, 0, 4, 8, 8, 8, 8, 9, 11, 14, 15, 18, 22, 27, 33, 33, 33, 35, 35, 39, 40, 41, 44, 44, 48, 48, 50, 50, 51, 52, 56, 56, 56, 56, 57, 57, 57, 58, 58, 59, 59, 62, 62, 62, 62, 65, 66, 67, 69, 71, 75, 75, 76, 76, 77, 79, 81, 83]
##run10=[0, 0, 0, 3, 8, 9, 14, 16, 20, 24, 25, 31, 34, 39, 45, 51, 53, 54, 56, 59, 63, 65, 67, 72, 73, 77, 77, 77, 77, 77, 77, 79, 79, 79, 79, 79, 79, 79, 79, 80, 80, 80, 81, 81, 81, 81, 81, 81, 81, 81, 81, 81, 82, 82, 82, 82, 82, 83, 84]
#
## run7 = [0, 0, 0, 1, 1, 2, 2, 5, 6, 7, 11, 11, 13, 13, 15, 16, 16, 17, 21, 24, 25, 26, 27, 27, 28, 29, 31, 33, 38, 42, 42, 43, 45, 48, 51, 52, 52, 54, 57, 57, 59, 59, 59, 59, 59, 60, 63, 64, 64, 64, 64, 64, 64, 65, 67, 69, 69, 69, 69]
## run8 = [0, 0, 0, 0, 1, 2, 3, 4, 4, 4, 6, 7, 12, 15, 15, 15, 16, 21, 26, 27, 28, 28, 29, 30, 32, 33, 36, 36, 37, 37, 37, 40, 43, 44, 45, 46, 46, 48, 49, 52, 55, 56, 57, 59, 62, 65, 65, 65, 66, 66, 67, 67, 69, 69, 69, 69, 69, 69, 69]
## run9 = [0, 0, 0, 0, 0, 0, 0, 2, 4, 4, 4, 9, 12, 13, 15, 16, 16, 22, 23, 27, 28, 29, 30, 31, 32, 34, 35, 38, 41, 42, 44, 45, 45, 46, 48, 49, 50, 50, 53, 53, 55, 56, 58, 62, 65, 65, 65, 67, 67, 67, 67, 67, 67, 67, 67, 69, 69, 69, 69]
## run10 = [0, 0, 0, 1, 1, 4, 5, 9, 14, 17, 24, 29, 30, 33, 37, 39, 43, 45, 51, 51, 51, 52, 52, 53, 56, 56, 57, 58, 62, 63, 63, 64, 65, 66, 66, 66, 66, 66, 67, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69]
#
#
#run7 = [0, 0, 0, 0, 2, 2, 4, 6, 7, 9, 10, 14, 16, 17, 17, 18, 21, 23, 24, 26, 27, 29, 33, 34, 36, 37, 38, 39, 41, 44, 44, 46, 47, 49, 50, 51, 53, 53, 53, 55, 57, 60, 60, 60, 62, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65, 65]
#run8 = [0, 0, 0, 1, 2, 4, 4, 5, 5, 5, 6, 6, 8, 8, 10, 12, 12, 14, 14, 18, 18, 20, 21, 23, 27, 29, 32, 32, 33, 38, 38, 39, 40, 42, 42, 43, 47, 48, 50, 54, 55, 56, 56, 56, 56, 57, 58, 58, 59, 61, 61, 61, 61, 61, 64, 65, 66, 67, 67]
#run9 = [0, 0, 2, 3, 4, 4, 7, 9, 9, 13, 13, 16, 19, 21, 24, 27, 29, 30, 30, 30, 31, 31, 31, 31, 31, 31, 31, 31, 32, 32, 33, 33, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 34, 36, 36, 36, 36, 36, 36, 36, 37, 43, 43, 43, 43, 43, 43, 44]
#run10 = [0, 0, 1, 3, 5, 8, 10, 11, 12, 14, 14, 16, 18, 19, 22, 23, 25, 26, 26, 27, 30, 31, 32, 32, 33, 34, 36, 36, 38, 40, 40, 40, 41, 43, 43, 43, 44, 44, 46, 46, 49, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 53, 55, 55, 56, 58, 58, 58]
#
#
###mutation 0.4
##run11=[0, 0, 0, 1, 3, 7, 8, 10, 11, 16, 20, 23, 25, 31, 36, 40, 41, 45, 51, 51, 55, 57, 59, 64, 66, 71, 74, 74, 74, 74, 75, 77, 78, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 80, 82, 82, 82, 82, 82, 84, 85, 85, 85, 88, 88, 88, 88, 88]
##run12=[0, 0, 0, 4, 7, 9, 10, 12, 16, 21, 23, 24, 26, 32, 34, 38, 41, 41, 43, 43, 47, 48, 49, 56, 60, 66, 67, 70, 70, 72, 73, 75, 79, 79, 79, 80, 81, 81, 81, 81, 82, 86, 88, 88, 90, 92, 92, 94, 94, 94, 94, 94, 95, 95, 95, 95, 95, 95, 95]
##run13=[0, 0, 0, 4, 8, 9, 10, 12, 14, 17, 21, 23, 29, 34, 38, 44, 47, 48, 49, 50, 52, 54, 54, 57, 59, 64, 65, 66, 67, 70, 72, 76, 77, 82, 84, 84, 87, 87, 88, 88, 90, 90, 90, 92, 92, 92, 92, 92, 93, 93, 97, 97, 99, 99, 99, 99, 99, 99, 99]
##run14=[0, 0, 0, 2, 5, 8, 9, 10, 12, 18, 19, 22, 24, 29, 32, 35, 36, 38, 40, 41, 45, 48, 52, 55, 55, 59, 60, 60, 61, 62, 63, 67, 68, 68, 68, 69, 69, 70, 71, 72, 73, 73, 75, 79, 80, 80, 80, 82, 87, 88, 90, 90, 90, 90, 93, 94, 94, 94, 94]
#
## run11 = [0, 0, 2, 2, 2, 2, 3, 6, 8, 10, 14, 14, 15, 18, 21, 22, 23, 23, 25, 29, 31, 33, 34, 37, 37, 37, 39, 41, 43, 45, 47, 47, 47, 47, 49, 50, 50, 52, 55, 57, 57, 57, 59, 59, 59, 59, 59, 59, 60, 60, 61, 61, 63, 63, 63, 63, 63, 63, 63]
## run12 = [0, 0, 3, 5, 6, 6, 8, 11, 13, 17, 18, 21, 23, 25, 26, 28, 32, 33, 35, 36, 39, 39, 39, 40, 44, 46, 47, 48, 49, 50, 51, 52, 52, 55, 55, 55, 56, 56, 56, 56, 58, 59, 60, 60, 61, 61, 65, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69, 69]
## run13 = [0, 0, 0, 0, 1, 2, 4, 6, 8, 8, 8, 8, 9, 10, 10, 11, 11, 12, 14, 16, 18, 19, 22, 24, 24, 27, 28, 29, 30, 31, 35, 37, 38, 41, 43, 44, 46, 52, 56, 56, 57, 58, 59, 59, 59, 59, 59, 59, 62, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
## run14 = [0, 0, 0, 0, 1, 2, 4, 6, 8, 8, 8, 8, 9, 10, 10, 11, 11, 12, 14, 16, 18, 19, 22, 24, 24, 27, 28, 29, 30, 31, 35, 37, 38, 41, 43, 44, 46, 52, 56, 56, 57, 58, 59, 59, 59, 59, 59, 59, 62, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
#
#run11 = [0, 0, 0, 2, 2, 4, 5, 5, 6, 8, 11, 13, 15, 17, 19, 19, 23, 25, 25, 28, 30, 31, 31, 31, 32, 33, 33, 34, 34, 36, 36, 39, 42, 44, 47, 48, 48, 48, 52, 53, 54, 54, 54, 54, 54, 54, 59, 59, 60, 60, 60, 60, 60, 60, 60, 61, 62, 62, 62]
#run12 = [0, 0, 1, 2, 2, 4, 4, 6, 7, 8, 9, 11, 13, 14, 15, 16, 17, 17, 18, 19, 19, 22, 26, 28, 29, 29, 31, 33, 34, 34, 35, 35, 36, 37, 38, 38, 38, 40, 41, 45, 46, 47, 50, 51, 51, 51, 54, 54, 57, 59, 60, 60, 61, 63, 63, 63, 63, 63, 64]
#run13 = [0, 0, 0, 3, 3, 5, 8, 10, 12, 16, 17, 20, 27, 27, 27, 28, 30, 35, 39, 41, 44, 47, 48, 48, 48, 49, 49, 49, 49, 50, 51, 51, 51, 51, 52, 52, 53, 53, 55, 57, 57, 57, 57, 57, 57, 57, 58, 61, 61, 61, 61, 62, 64, 65, 65, 65, 66, 66, 66]
#run14 = [0, 0, 0, 2, 2, 6, 10, 11, 16, 20, 22, 27, 31, 34, 37, 39, 41, 44, 45, 47, 47, 48, 49, 49, 51, 52, 52, 53, 53, 53, 53, 53, 53, 53, 53, 54, 55, 55, 56, 57, 58, 59, 61, 62, 63, 64, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66, 66]
#
###mutation=0
##run15=[0, 0, 0, 1, 6, 9, 9, 9, 10, 13, 17, 19, 21, 25, 30, 35, 37, 41, 43, 46, 50, 54, 56, 60, 61, 67, 67, 67, 69, 69, 71, 73, 73, 73, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 75, 76, 77, 77, 77, 77, 77, 78, 78]
##run16=[0, 0, 0, 2, 5, 5, 5, 5, 8, 12, 15, 19, 23, 28, 31, 33, 33, 34, 37, 37, 39, 40, 40, 43, 43, 47, 47, 47, 47, 47, 47, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49, 49]
##run17=[0, 0, 1, 2, 4, 4, 5, 6, 9, 13, 14, 16, 17, 21, 23, 25, 25, 25, 26, 26, 28, 29, 29, 32, 32, 36, 36, 36, 36, 36, 36, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38]
##run18=[0, 0, 1, 4, 9, 10, 12, 13, 15, 17, 20, 21, 22, 26, 29, 31, 32, 32, 33, 33, 35, 36, 36, 40, 40, 44, 44, 44, 44, 44, 44, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46, 46]
#
## run15 = [0, 0, 0, 3, 5, 8, 12, 14, 16, 18, 19, 24, 27, 28, 28, 28, 28, 29, 32, 32, 32, 34, 34, 34, 35, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 36, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38, 38]
## run16 = [0, 0, 1, 3, 4, 8, 8, 10, 11, 12, 15, 16, 18, 19, 20, 27, 27, 27, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 29, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
## run17 = [0, 0, 0, 3, 7, 7, 10, 12, 16, 17, 17, 19, 20, 22, 22, 23, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24]
## run18 = [0, 0, 0, 1, 1, 5, 9, 9, 14, 16, 16, 17, 18, 20, 23, 25, 25, 25, 26, 27, 27, 27, 27, 27, 27, 27, 27, 27, 28, 28, 28, 28, 28, 28, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30]
#
#run15 = [0, 0, 0, 2, 2, 3, 4, 4, 4, 7, 8, 8, 10, 10, 10, 11, 13, 15, 17, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24, 24]
#run16 = [0, 0, 0, 3, 5, 8, 8, 9, 9, 10, 10, 13, 15, 16, 16, 16, 16, 18, 18, 18, 18, 20, 20, 20, 20, 20, 20, 20, 21, 21, 21, 21, 21, 21, 21, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22, 22]
#run17 = [0, 0, 0, 1, 2, 6, 6, 6, 6, 8, 9, 9, 10, 10, 10, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 12, 13, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15, 15]
#run18 = [0, 0, 0, 0, 1, 2, 5, 8, 10, 11, 12, 16, 16, 17, 19, 19, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20, 20]
#
#
#runTMP4=[]
#for i in range(len(run1)):
#   runTMP4.append(run15[i]+run16[i]+run17[i]+run18[i])
#   runTMP4[i]/=4
#
#
#runTMP3=[]
#for i in range(len(run1)):
#   runTMP3.append(run11[i]+run12[i]+run13[i]+run14[i])
#   runTMP3[i]/=4
#
#
#
#runTMP2=[]
#for i in range(len(run1)):
#   runTMP2.append(run7[i]+run8[i]+run9[i]+run10[i])
#   runTMP2[i]/=4
#
#
#
#runTMP=[]
#for i in range(len(run1)):
#   runTMP.append(run1[i]+run2[i]+run3[i]+run4[i]+run5[i]+run6[i])
#   runTMP[i]/=6
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
#plt.plot(x, runTMP3,label='$p = %.1f$' % 0.4)
#plt.plot(x, runTMP2,label='$p = %.1f$' % 0.2)
#plt.plot(x, runTMP4,label='$p = %.1f$' % 0.0)
#
#
#plt.legend()
#
#plt.ylabel("Nombre de robots morts")
#plt.xlabel("Temps (minutes)")
#
#plt.show()