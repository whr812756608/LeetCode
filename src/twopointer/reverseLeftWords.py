class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # 时间复杂度：O(n)
        # 空间复杂度：O(n)，python的string为不可变，需要开辟同样大小的list空间来修改
        s = list(s)
        left  = 0
        right = n-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1
                  
        left = n
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1
        
        left = 0
        right = len(s)-1
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -=1   
        return "".join(s)
        
        # space complexity O(N)
        # return  s[n:] + s[:n] 
