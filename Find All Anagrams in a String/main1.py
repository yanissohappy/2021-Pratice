from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        ret = []
        p_counter = Counter(p)
        p_len = len(p)
        if len(s) < len(p): return []
        
        for i in range(len(s)):
            if i + p_len - 1 == len(s):
                break
            s_counter = Counter(s[i: i + p_len])
            if s_counter == p_counter:
                ret.append(i)
                
        return ret