from collections import Counter
class Solution(object):
    def removeKdigits(self, num, k):
        stack = []
        del_num = k
        if len(num) <= k:
            return "0"
        
        for i in range(len(num)):
            while True:
                if not stack or del_num == 0:
                    break
                if int(stack[-1]) > int(num[i]):
                    stack.pop()
                    del_num -= 1
                else:
                    break
            stack.append(num[i])
        while del_num:
            stack.pop()
            del_num -= 1
        res = "".join(stack).lstrip('0')
        res_counter = Counter(res)
        if res_counter["0"] == len(res):
            return "0"
        return res