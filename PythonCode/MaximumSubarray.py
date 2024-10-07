def max_subarray(numbers):
    max_sum, cur_sum = float('-inf'), 0

    for num in numbers:
        cur_sum = max(cur_sum + num, num)
        max_sum = max(max_sum, cur_sum)
    
    return max_sum