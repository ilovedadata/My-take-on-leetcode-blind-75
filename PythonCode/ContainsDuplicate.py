class Solution(object):
    def containsDuplicate(self, nums:list[int]) -> bool:
        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False