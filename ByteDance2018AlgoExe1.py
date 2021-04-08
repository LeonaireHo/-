'''
P为给定的二维平面整数点集。定义 P 中某点x，如果x满足 P 中任意点都不在 x 的右上方区域内（横纵坐标都大于x），则称其为“最大的”。
求出所有“最大的”点的集合。（所有点的横坐标和纵坐标都不重复, 坐标轴范围在[0, 1e9) 内）
'''

def pref(p1,p2):
    if p1[0]>=p2[0] and p1[1]>=p2[1]:
        return True
    return False

n = int(input())
liste = [list(map(int,input().split()))]
for _ in range(n-1):
    p2 = list(map(int,input().split()))
    aux = True
    for i in range(len(liste)-1,-1,-1):
        if pref(p2,liste[i]):
            liste.remove(liste[i])
        elif pref(liste[i],p2):
            aux = False
    if aux:
        liste.append(p2)
liste.sort()
for p in liste:
    print(p[0],p[1])

'''
Input:
10
298498081 747278511
427131847 460128162
939984059 817455089
911902081 683024728
474941318 6933274
140954425 607811211
336122540 629431445
208240456 458323237
646203300 469339106
106410694 436340495
output:
939984059 817455089
'''