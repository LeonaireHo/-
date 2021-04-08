aux =list(map(int,input().split()))
nbcxy = aux[0]
nbpm = aux[1]
nbjob = aux[2]
listjob = []
for _ in range(nbjob):
    listjob.append(list(map(int,input().split())))
def distibu(jobs):
    idx = 0
    for i in range(1,len(jobs)):
        if jobs[i][2]>jobs[idx][2]:
            break
        if jobs[i][2]<jobs[idx][2]:
            idx = i
            break
        if jobs[i][3]>jobs[idx][3]:
            break
        if jobs[i][3]<jobs[idx][3]:
            idx = i
            break
        if jobs[i][1] > jobs[idx][1]:
            break
        if jobs[i][1] < jobs[idx][1]:
            idx = i
            break
        if jobs[i][0]>jobs[idx][0]:
            break
        if jobs[i][0]<jobs[idx][0]:
            idx = i
            break
    return idx

copie = listjob.copy()
listjob.sort(key = lambda x:x[1])
listwait = []
listjobtemp=[0]*nbjob
temp = 0
wroking=[0]*nbcxy
while listjob or listwait:
    #depose idee
    while True:
        if listjob and temp >= listjob[0][1]:
            listwait.append(listjob[0])
            listjob.pop(0)
        else:
            break
    for i in range(len(wroking)):
        if(wroking[i] <= 0)and listwait != []:
            idx = distibu(listwait)
            wroking[i] = listwait[idx][3]
            # print(listwait[idx])
            # print(listjob)
            listjobtemp[copie.index(listwait[idx])] = temp + listwait[idx][3]
            listwait.pop(idx)
        wroking[i] -= 1
    temp += 1
for i in listjobtemp:
    print(i)
'''
input:
2 2 5
1 1 1 2
1 2 1 1
1 3 2 2
2 1 1 2
2 3 5 5
output:
3
4
5
3
9
'''
