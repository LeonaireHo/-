def pref(p1,p2):
    if p1[0]>=p2[0] and p1[1]>=p2[1]:
        return True
    return False

n = int(input())
liste = [list(map(int,input().split()))]
for _ in range(n-1):
    p2 = list(map(int,input().split()))
    aux = True
    for p1 in liste:
        if pref(p2,p1):
            liste.pop(liste.index(p1))
        elif pref(p1,p2):
            aux = False
    if aux:
        liste.append(p2)

for p in liste:
    print(p[0],p[1])

'''
Input:
5
1 2
5 3
4 6
7 5
9 0
output:
4 6
7 5
9 0
'''