class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        # s.reverse()

        # s[:] = s[::-1]
        
        # s = s[::-1] 报错， 会创建一个新s并把翻转的值赋给新的s

        #双指针 
        left = 0
        right = len(s)-1
        while left <= right:
            s[left],s[right] = s[right],s[left]
            left  +=1
            right -=1
