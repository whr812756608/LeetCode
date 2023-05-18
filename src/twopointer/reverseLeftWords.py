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
        
        #取余法：
   class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        res = []
        for i in range(n,n+len(s)):       # 取余数，i%len（s）= i，python可以直接+
           res += s[i%len(s)]             # 当 i 小于 len（s）时，i=3，i=4，i%len（s）= i，余数为i，即对应下标，res【3】=s【3】，res【4】=s【4】
           print(res)                     # 当 i 大于 len（s）时，i =7，i=8
        return "".join(res)               # i%len（s）= i - len（s） 余数为 下标-长度，即res【7】=s【1】，res【8】=s【2】
