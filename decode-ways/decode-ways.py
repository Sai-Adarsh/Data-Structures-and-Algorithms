class Solution:
    def numDecodings(self, s: str) -> int:
        
        ascii_arr = [_ for _ in range(1, 27)]
        
        
        memo = {}
        def backTracking(i):
            if i in memo:
                return memo[i]
            if i == len(s):
                return 1
            
            res = 0
            for j in range(i + 1, len(s) + 1):
                if len(str(int(s[i:j]))) ==len(s[i:j]):
                    if int(s[i:j]) in ascii_arr:
                        res += backTracking(j)
            memo[i] = res
            return memo[i]
        
        return backTracking(0)