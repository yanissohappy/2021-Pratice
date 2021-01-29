import numpy as np
class Solution(object):

    def __init__(self, nums):
        self.orig = nums[:]
        self.array = nums[:]
        

    def reset(self):
        self.array = self.orig[:]
        return self.array

    def shuffle(self):
        length = len(self.array)
        for i in range(length):
            random_number = np.random.randint(i, length)
            self.array[i], self.array[random_number] = self.array[random_number], self.array[i]
        return self.array
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()