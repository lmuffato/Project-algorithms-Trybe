def find_duplicate(nums):
    nums_list = []
    duplicate = []
    if nums:
        for index in range(len(nums)):
            if nums[index] not in nums_list:
                nums_list.append(nums[index])
            else:
                duplicate.append(nums[index])
        for num in duplicate:
             if len(duplicate) > 0 and num > -1:
                return num
             return False
    return False
