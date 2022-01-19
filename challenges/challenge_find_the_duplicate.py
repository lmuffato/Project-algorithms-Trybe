def find_duplicate(nums=None):
    if not nums or len(nums) == 1 or type(nums) == "string":
        return False

    try:
        nums.sort()
    except TypeError:
        return False

    for i in range(len(nums)-1):
        if isinstance(nums[i], str):
            break
        if nums[i] < 0:
            break
        if nums[i] == nums[i+1]:
            return nums[i]

    return False

""" print(find_duplicate(["a", "b"])) """

