# 一只蚂蚁坐在由白色和黑色方格构成的无限网格上。开始时，网格全白，蚂蚁面向右侧。每行走一步，蚂蚁执行以下操作。
#
# (1) 如果在白色方格上，则翻转方格的颜色，向右(顺时针)转 90 度，并向前移动一个单位。
# (2) 如果在黑色方格上，则翻转方格的颜色，向左(逆时针方向)转 90 度，并向前移动一个单位。
#
# 编写程序来模拟蚂蚁执行的前 K 个动作，并返回最终的网格。
#
# 网格由数组表示，每个元素是一个字符串，代表网格中的一行，黑色方格由 'X' 表示，白色方格由 '_' 表示，蚂蚁所在的位置由 'L', 'U', 'R', 'D' 表示，分别表示蚂蚁 左、上、右、下 的朝向。只需要返回能够包含蚂蚁走过的所有方格的最小矩形。
def printKMoves(K: int):
    orient = [[0,1],[1,0],[0,-1],[-1,0]]#RDLU
    orient_Lettre = ['R','D','L','U']
    grid = {}
    grid["0-0"] = 1
    grid_taille = [0,0,0,0]
    pos_ant = [0,0]
    orient_ant = 0 # index in list orient
    for _ in range(K):
        pos_id = str(pos_ant[0])+"-"+str(pos_ant[1])
        #turn
        if grid[pos_id]:
            orient_ant = (orient_ant+1)%4
        else:
            orient_ant = (orient_ant - 1) % 4
        print(pos_ant,orient_ant)
        #change color
        grid[pos_id] = (grid[pos_id]+1)%2
        pos_ant[0]+=orient[orient_ant][0]
        pos_ant[1]+=orient[orient_ant][1]
        #move
        pos_id = str(pos_ant[0])+"-"+str(pos_ant[1])
        #update pos
        print(pos_id)
        try:
            grid[pos_id]
        except:
            grid[pos_id] = 1
        grid_taille[0] = min(pos_ant[0],grid_taille[0])
        grid_taille[1] = max(pos_ant[0],grid_taille[1])
        grid_taille[2] = min(pos_ant[1],grid_taille[2])
        grid_taille[3] = max(pos_ant[1],grid_taille[3])
    print(grid,pos_ant,grid_taille)
    for l in range(grid_taille[0],grid_taille[1]+1):
        phs = ""
        for c in range(grid_taille[2], grid_taille[3]+1):
            pos_id = str(l) + "-" + str(c)
            try:
                v = grid[pos_id]
            except:
                v = 1
            if pos_ant == [l,c]:
                phs += orient_Lettre[orient_ant]
            elif v:
                phs += '_'
            else:
                phs += 'X'
        print(phs)
printKMoves(5)


# class Solution:
#     def printKMoves(self, K: int) -> List[str]:
#         # 定义状态 和方向
#         state, direction = 0, [(0, 1, 'R'), (1, 0, 'D'), (0, -1, 'L'), (-1, 0, 'U')]
#         net = dict()
#         # 记录当前位置，和最小 最大坐标
#         pos, min_, max_ = (0, 0), (0, 0), (0, 0)
#
#         for _ in range(K):
#             if net.get(pos, '_') == '_':
#                 net[pos] = 'X'
#                 # 顺时针
#                 state = (state + 1) % 4
#             else:
#                 net[pos] = '_'
#                 # 逆时针
#                 state = (state - 1) % 4
#             # 向前移动
#             pos = (pos[0] + direction[state][0], pos[1] + direction[state][1])
#             # 记录两边界坐标
#             min_ = (min(min_[0], pos[0]), min(min_[1], pos[1]))
#             max_ = (max(max_[0], pos[0]), max(max_[1], pos[1]))
#         net[pos] = direction[state][2]
#
#         ans = [''.join([net.get((i, j), '_') for j in range(min_[1], max_[1] + 1)])
#                for i in range(min_[0], max_[0] + 1)]
#
#         return ans