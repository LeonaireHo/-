'''
给定一个包含非负整数的 m x n 网格 grid ，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。
输入：grid = [[1,3,1],[1,5,1],[4,2,1]]
输出：7
解释：因为路径 1→3→1→1→1 的总和最小。
'''
def minPathSum(grid):
    dp_total = []
    nb_col = len(grid)
    nb_lig = len(grid[0])
    dp = [grid[0][0]]
    for i in (grid[0][1:]):
        dp.append(i + dp[-1])
    dp_total.append(dp)
    for i in range(1,len(grid)):
        dp = [dp_total[-1][0]+grid[i][0]]
        for j in range(1,len(grid[0])):
            dp.append(min(dp[-1],dp_total[-1][j])+grid[i][j])
        dp_total.append(dp)
    return dp_total[-1][-1]


print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))