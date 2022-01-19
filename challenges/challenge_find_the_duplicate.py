def find_duplicate(nums=None):
    if not nums or len(nums) == 1 or type(nums) == "string":
        return False

    nums.sort()

    for i in range(len(nums)):
        if nums[i] < 0:
            break
        if nums[i] == nums[i+1]:
            return nums[i]

    return False


print(find_duplicate())

