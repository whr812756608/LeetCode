class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)      # 行数  = m
        n = len(matrix[0])   # 列数 = n


        l = 0
        r = n-1
        t = 0
        b = m-1
        counts = 1
        target = m * n     
        result = []

        if m == 0 or n == 0:
            return []

        while counts <= target:
            for j in range(l,r+1):
                if counts <= target:     # 先判断是否满足条件再更新result和数组
                    result.append(matrix[t][j])
                    counts +=1
            t +=1
            

            for i in range(t,b+1):
                if counts <= target:
                    result.append(matrix[i][r])
                    counts +=1
            r -=1
            

            for j in range(r,l-1,-1):
                if counts <= target:
                    result.append(matrix[b][j])
                    counts +=1
            b -=1
        

            for i in range(b,t-1,-1):
                if counts <= target:
                    result.append(matrix[i][l])
                    counts +=1
            l +=1
 
        return result 
