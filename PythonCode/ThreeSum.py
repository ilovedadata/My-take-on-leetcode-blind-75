class Solution(object):
    def threeSum(self, nums:list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 

            l, r = i + 1, len(nums) - 1

            while l < r:
                threesum = nums[i] + nums[l] + nums[r]
                
                if threesum > 0:
                    r = r - 1
                
                elif threesum < 0:
                    l = l + 1 

                else: 
                    res.append([nums[i], nums[l], nums[r]])
                    l = l + 1
                    r = r - 1

                    while (nums[l] == nums[l - 1]) and l < r:
                        l = l + 1
                    while (nums[r] == nums[r - 1]) and l < r:
                        r = r - 1

        return res