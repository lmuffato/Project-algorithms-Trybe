def find_duplicate(nums):
    for gokuSSj in range(len(nums)):
        for vegetaSsj in range(len(nums)):
            if gokuSSj != vegetaSsj and nums[gokuSSj] == nums[vegetaSsj]:
                if nums[gokuSSj] > 0:
                    return nums[gokuSSj]
    return False
