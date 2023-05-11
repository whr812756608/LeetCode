class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # 生成 n x n 矩阵
        # 里面的括号[0 for _ in range(n)]控制列的数量
        # 外面的大括号[[0 for _ in range(n)] for _ in range(n)] 控制行的数量
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        left = 0
        right = n-1
        top = 0
        bottom = n-1

        nums = 1
        target = n*n
        # 循环结束条件 填充的数 == target
        while nums <= target:
            for j in range(left,right+1):
                matrix[top][j] = nums
                nums +=1
            top +=1
            for i in range(top,bottom+1):
                matrix[i][right] = nums
                nums +=1
            right-=1
            for j in range(right,left-1,-1):
                matrix[bottom][j] = nums
                nums +=1
            bottom -=1
            for i in range(bottom,top-1,-1):
                matrix[i][left] = nums
                nums+=1
            left +=1
        return matrix
