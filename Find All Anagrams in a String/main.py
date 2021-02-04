class Solution(object):
    def makeAllAnagram(self, p, string, _len, ret):
        for i in range(len(p)):
            string += p[i]
            if len(string) == _len:
                ret.append(string)
                return                
            self.makeAllAnagram(p[:i] + p[i + 1:], string, _len, ret)
            string = string[:-1]
            
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        p_len = len(p)
        anagrams = []
        ret = []
        self.makeAllAnagram(p, "", p_len, anagrams)
        #print(anagrams)
        
        for i in range(len(s)):
            if i + p_len - 1 > len(s) - 1:
                break
            segment = s[i: i + p_len]
            
            if segment in anagrams:
                ret.append(i)
        
        return ret
        