import random
class Solution(object):

    def __init__(self, nums):
        self.orig = nums[:]
        self.array = nums[:]
        

    def reset(self):
        self.array = self.orig[:]
        return self.array
    

    def shuffle(self):
        random.shuffle(self.array)
        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()