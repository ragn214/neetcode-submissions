class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = int((len(nums)-1)/2)
        l = 0 # narrowing selection of the indexes
        r = len(nums)-1 # narrowing selection of the indexes
        while target != nums[index]:
            if target < nums[index]:
                r = index

                if index == int((r+l)/2):
                    return -1
                else:
                    index = int((r+l)/2)
                    
            else: # if the target is greater than the new number
                l = index + 1
                
                if index == int((r+l)/2):
                    return -1
                else:
                    index = int((r+l)/2)
                    
            
        return index

        #[-1, 0, 2, 4, 6, 8, 9,10,11,12,13,14,15] numbers
        #[ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12] index
        #                      [0, 1, 2, 3, 4, 5]
        # target = 12
        #length = 13
        #index = 6
        #newindex = 
