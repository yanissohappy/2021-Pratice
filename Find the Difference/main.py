class Solution(object):
    def findTheDifference(self, s, t):
        ans = dict()
        for i in s:
            if i not in ans:
                ans[i] = 1
            else:
                ans[i] += 1
        
        for j in t:
            if j not in ans or ans[j] == 0:
                return j
            else:
                ans[j] -= 1        
            
        """
        # chech answer 
        for key, value in ans.items():
            if value == 1:
                return key
        """