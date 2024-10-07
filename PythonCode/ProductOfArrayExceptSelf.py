class Solution(object):
    def productExceptSelf(self, nums:list[int]) -> list[int]:
        left_products = [1] * len(nums)
        right_products = [1] * len(nums)
        answer = []

        for i in range(1, len(nums)):
            left_products[i] = left_products[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            right_products[i] = right_products[i+1] * nums[i+1]

        for i in range(len(nums)):
            answer.append(left_products[i] * right_products[i])

        print(left_products)
        print(right_products)
        return answer