"""
给定n个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
"""

def f(list):
    hmax = max(list)
    res = 0
    for h in range(hmax,0,-1):
        brush = 0
        flag = False
        for i in list:
            if i >= h:
                flag = True
                res += brush
                brush = 0
            elif flag:
                brush += 1
    return res

print(f([0,1,0,2,1,0,1,3,2,1,2,1]))
