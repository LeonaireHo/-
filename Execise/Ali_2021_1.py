"""给你一个由小写字母组成的字符串s，和一个整数k。

请你按下面的要求分割字符串：

首先，你可以将s中的部分字符修改为其他的小写英文字母。
接着，你需要把s分割成k个非空且不相交的子串，并且每个子串都是回文串。
请返回以这种方式分割字符串所需修改的最少字符数。

"""
l = list(input().split())
s = str(l[0])
k = int(l[1])

def cpt(s):
    long = len(s)
    cpt = 0
    for i in range(int(long/2)):
        if s[i] != s[long - i - 1]:
            cpt += 1
    return cpt

def minChange(s,k):
    long = len(s)
    minv = float('inf')
    if k == 1:
        return cpt(s)
    if len(s) <= k:
        return 0
    for i in range(long - k + 1):
        minv = min(minv,cpt(s[:i+1])+minChange(s[i+1:],k-1))
    return minv

print(minChange(s,k))

"""
##leetcode动态规划题解
class Solution {
    public int palindromePartition(String s, int K) {

        int len = s.length();
        // cache[i][j] 表示 s 中索引 i 到 j 构成回文串的最小步数
        int[][] cache = new int[len][len];
        // 填充
        for (int i = len-1; i > 0; i--) {
            for (int j = i-1; j < len-1; j++) {
                // 状态转移
                cache[i-1][j+1] = cache[i][j] + (s.charAt(i-1) == s.charAt(j+1) ? 0 : 1);
            }
        }
        // dp[i][k] 表示划分为 k 个时，s 中 0~i 构成回文串的所需最小步数
        int[][] dp = new int[len][K];
        // 初始化
        for (int i = 1; i < len; i++) {
            dp[i][0] = cache[0][i];
        }

        for (int i = 1; i < len; i++) {
            for (int k = 1; k < K; k++) {
                 // 初始化
                dp[i][k] = Integer.MAX_VALUE;
                for (int j = i; j >= k; j--) {
                    // 状态转移
                    dp[i][k] = Math.min(dp[i][k], dp[j-1][k-1] + cache[j][i]);
                }
            }
        }

        return dp[len-1][K-1];
    }
}
"""


"""
input : accbbbee 2

output : 1
"""