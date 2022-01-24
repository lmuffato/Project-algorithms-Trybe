def find_duplicate(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            return False
        for index in range(len(nums)):
            if i != index and nums[i] == nums[index]:
                return nums[i]
    return False
