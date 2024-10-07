def twoSum(nums:list[int], target:int) -> list[int]:
    hash_map = {}
    for i, value in enumerate(nums):
        delta = target - value
        if delta in hash_map.keys():
            return [hash_map[delta], i]
        hash_map[value] = i
    return