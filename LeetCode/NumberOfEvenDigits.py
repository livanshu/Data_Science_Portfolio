    def findNumbers(self, nums: List[int]) -> int:
        a = map(str,nums)         #map(function,iterable)
        count = 0
        
        for i in a:
            if len(i) % 2 == 0:
                count +=1
        return count
