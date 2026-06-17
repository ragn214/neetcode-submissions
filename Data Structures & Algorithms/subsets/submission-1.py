class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # result = []
        # current = []
        result = [[] for _ in range(2**len(nums))]
        for i in range(len(result)):
            for j, num in enumerate(nums):
                if (i // 2**(j)) % 2 == 0:
                    result[i].append(nums[j])
        return result
        # for i in range(len(nums)):
            


        # i = 0
        # while i < len(nums):
        #     self.subsets(nums[i:])
        #     i++
        # if i
        # return 0