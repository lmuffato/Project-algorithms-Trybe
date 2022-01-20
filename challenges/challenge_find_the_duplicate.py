def find_duplicate(nums):
    sorted_nums = sorted(nums)
    for index, num in enumerate(sorted_nums[:-1]):
        if sorted_nums[index] == sorted_nums[index+1] and num >= 0:
            return num
    return False
