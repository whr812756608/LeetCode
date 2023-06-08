class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        path = []
        res = []

        def backtracking(n,k,start_idx,cur_sum):
            if cur_sum > n:
                return          
            if len(path) == k and cur_sum == n:
                res.append(path[:])
                return res
            
            for i in range(start_idx,9+1+1-(k-len(path))):
                path.append(i)
                cur_sum += i
                backtracking(n,k,i+1,cur_sum)
                cur_sum -= i 
                path.pop()
        cur_sum = 0
        start_idx = 1
        backtracking(n,k,start_idx,cur_sum)
        return res
