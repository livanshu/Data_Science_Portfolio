    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        result = 0
        
    #Imagine a T-type conveyor belt and seperating 0's & 1's. Piling 1's and counting the numbers.
        for i in range(0,len(nums)):
            if (nums[i]==0):
                count = 0
            else:
                count += 1
                result = max(result,count)
        return result
