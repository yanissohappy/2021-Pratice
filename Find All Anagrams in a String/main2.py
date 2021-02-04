from collections import Counter
class Solution(object):
    def findAnagrams(self, s, p):
        ret = []
        p_len = len(p)
        p_counter = Counter(p)
        s_counter = Counter(s[0: p_len])
        if len(s) < len(p): return []
        
        for i in range(len(s)):   
            if s_counter == p_counter:
                ret.append(i)
            if i + p_len == len(s):
                break

            del_char = s[i]
            new_char = s[i + p_len]
            s_counter[new_char] += 1   
            s_counter[del_char] -= 1         
            if s_counter[del_char] == 0:
                del s_counter[del_char]
            
        return ret