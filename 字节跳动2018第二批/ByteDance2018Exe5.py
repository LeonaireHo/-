'''
作为一个手串艺人，有金主向你订购了一条包含n个杂色串珠的手串——每个串珠要么无色，要么涂了若干种颜色。
为了使手串的色彩看起来不那么单调，金主要求，手串上的任意一种颜色（不包含无色），在任意连续的m个串珠里至多出现一次（注意这里手串是一个环形）。
手串上的颜色一共有c种。现在按顺时针序告诉你n个串珠的手串上，每个串珠用所包含的颜色分别有哪些。请你判断该手串上有多少种颜色不符合要求。
即询问有多少种颜色在任意连续m个串珠中出现了至少两次。

第一行输入n，m，c三个数，用空格隔开。(1 <= n <= 10000, 1 <= m <= 1000, 1 <= c <= 50)
 接下来n行每行的第一个数num_i(0 <= num_i <= c)表示第i颗珠子有多少种颜色。
接下来依次读入num_i个数字，每个数字x表示第i颗柱子上包含第x种颜色(1 <= x <= c)
'''
l = list(map(int,input().split()))
n = l[0]
m = l[1]
c = l[2]
listBol = []
listErr=[]

for _ in range(m):
    listBol.append(list(map(int,input().split())))
for _ in range(n-m):
    listBol.append(list(map(int,input().split())))
    print(listBol)
    for j in range(1,len(listBol[-1])):
        aux = listBol[-1][j]
        for k in range(len(listBol)-m,len(listBol)-1):
            print(k)
            if aux in listBol[k][1:] and aux not in listErr:
                listErr.append(aux)
print(len(listErr))

'''
input:
5 3 3
3 1 2 3
0
2 2 3
1 2
1 3
output:
2
'''