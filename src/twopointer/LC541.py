class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        def reverse(s):
            left = 0
            right = len(s)-1
            while left < right:
                s[left],s[right] = s[right],s[left]
                left  +=1
                right -=1
            return s
        s= list(s)

        # for i in range(0,len(s),2*k):
        #     s[i:i+k] = reverse(s[i:i+k])

        #for i in range(0,len(s), 2*k):
        #    s[i:i+k] = s[i:i+k][::-1]

        for i in range(0,len(s),2*k):
            if i + k <= len(s):              # check between i+k and len(s)
                                             # exclusive len(s), so we can write <=
                                             # if its inclusive, can't write =
                s[i:i+k] = reverse(s[i:i+k]) # modify on the slice
            else:
                s[i:] = reverse(s[i:])
        return "".join(s)
