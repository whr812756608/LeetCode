class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip() # 删除首尾空格
        i, j = len(s)-1, len(s)-1
        res = []

        while i >= 0:
            while i >= 0 and s[i] != " ":
                i -=1
            res.append(s[i+1:j+1])

            while i>= 0 and s[i] == " ":
                i -=1
            j = i 
    
        print(res)
        return " ".join(res)
