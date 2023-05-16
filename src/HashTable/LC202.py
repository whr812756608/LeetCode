class Solution:
    def isHappy(self, n: int) -> bool:
        def calculate_sum (n):
            cur_sum = 0
            while n:
                # 从个位开始依次取，平方求和
                cur_sum += (n%10)**2
                n = n //10
                # 除以10，向下取整
                # 从个位到十位到百位
                # example： 198%10 = 8   198//10 = 19
                # 19%10 = 9， 19//10 = 1
                # 1%10 = 1    1//10 = 0

            return cur_sum
        record = set()

        while True:
            n = calculate_sum(n)
            if n == 1:
                return True
            # 如果中间结果重复出现，说明陷入死循环了，该数不是快乐数
            if n in record:
                return False
            else:
                record.add(n)
