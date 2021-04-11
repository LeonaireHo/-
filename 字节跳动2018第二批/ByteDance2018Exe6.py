'''
字符串S由小写字母构成，长度为n。定义一种操作，每次都可以挑选字符串中任意的两个相邻字母进行交换。
询问在至多交换m次之后，字符串中最多有多少个连续的位置上的字母相同？
'''
from collections import defaultdict
s, m = input().split()
m = int(m)
dictChar = defaultdict(list)
for i,ch in enumerate(s):
    dictChar[ch].append(i)
res = 0
for ch,l in dictChar.items():
    dp = [[0] * len(l) for _ in range(len(l))]
    for i in range(1, len(l)):
        dp[i - 1][i] = l[i] - l[i - 1] - 1
    for k in range(2, len(l)):
        for i in range(len(l) - k):
            left, right = i, k + i
            dp[left][right] = dp[left + 1][right - 1] + (l[right] - l[left] - 1) - (right - left - 1)
    for i in range(len(l)):
        for j in range(i, len(l)):
            if dp[i][j] <= m:
                res = max(res, j - i + 1)

print(res)

'''
input:
abcbaa 2

output:
2
'''