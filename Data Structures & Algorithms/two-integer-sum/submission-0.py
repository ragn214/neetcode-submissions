class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)-1):
        #     for j in range(len(nums)-i-1):
        #         print(i)
        #         print(j)
        #         print(i+j)
        #         if nums[i] + nums[i+j+1] == target:
        #             return [i, i+j+1]
        prevMap = {} # val : index
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            else:
                prevMap[n] = i

