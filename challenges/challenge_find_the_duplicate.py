def find_duplicate(nums):
    nums.sort()
    for index in range(len(nums) - 1):
        if isinstance(nums[index], int) and nums[index] < 0:
            return False
        if nums[index] == nums[index + 1]:
            return nums[index]

    return False
