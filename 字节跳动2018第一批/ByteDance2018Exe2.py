'''
给定一个数组序列, 需要求选出一个区间, 使得该区间是所有区间中经过如下计算的值最大的一个：

区间中的最小数 * 区间所有数的和最后程序输出经过计算后的最大值即可，不需要输出具体的区间。如给定序列  [6 2 1]则根据上述公式, 可得到所有可以选定各个区间的计算值:
'''
n = int(input())
l = list(map(int,input().split()))
max = 0
for i in range(n):
    aux = 0
    for j in range(i-1,-1,-1):
        print(j)
        if(l[j]<l[i]):
            break
        aux += l[j]
    for j in range(i,n):
        print(j)
        if(l[j]<l[i]):
            break
        aux += l[j]
    if max < aux * l[i]:
        max = aux * l[i]
print(max)

"""
input:
10
81 87 47 59 81 18 25 40 56 0
output:
16685
"""