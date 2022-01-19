def initial_check(nums):
    if not nums or len(nums) == 1 or type(nums) == "string":
        return False

    for item in nums:
        if isinstance(item, str):
            return False
    return True


def sort_nums(nums):
    try:
        nums.sort()
    except TypeError:
        return False

    return nums


def find_duplicate(nums=None):
    if not initial_check(nums):
        return False

    sorted_nums = sort_nums(nums)

    for i in range(len(sorted_nums)-1):
        if sorted_nums[i] < 0:
            break
        if nums[i] == nums[i+1]:
            return nums[i]

    return False
