    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        #input = [1,0,2,0,3,0,4]
        arr2 = [i for i in arr]     #copy arr into another array
        i=0                         #index for arr
        j=0                         #index for arr2
                                    #using two index, one to handle zeroes, one to shift value to next
        
        while i < len(arr):
            if not arr2[j]:         #if arr2[j] is zero
                arr[i]= 0           #assinging 0 to array value
                i+=1                #increment index i to shift value
                if i<len(arr):         
                    arr[i]=0
            else:
                arr[i] = arr2[j] 
            j+=1
            i+=1
        return arr
