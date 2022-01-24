def find_duplicate(nums):
    for i in range(len(nums)):
        for index in range(len(nums)):
            if i != index and nums[i] == nums[index]:
                return nums[i]
    return False
