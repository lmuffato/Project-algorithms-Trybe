def find_duplicate(nums):
    nums.sort()
    nums_len = len(nums)
    for index in range(nums_len - 1):
        if isinstance(nums[index], int) and nums[index] < 0:
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]

    return False
