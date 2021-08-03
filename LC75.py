'''
给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
示例 1：

输入：nums = [2,0,2,1,1,0]
输出：[0,0,1,1,2,2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-colors
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
def f75(nums):
    n = len(nums)
    d = 0
    f = n - 1
    i = 0
    while i <= f:
        while i <= f and nums[i] == 2:
            nums[i], nums[p2] = nums[f], nums[i]
            f -= 1
        if nums[i] == 0:
            nums[i], nums[d] = nums[d], nums[i]
            d += 1
        i += 1
