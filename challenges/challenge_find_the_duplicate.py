def find_duplicate(nums):
    if not nums:
        return False

    array = nums.copy()
    array.sort()

    for i in range(1, len(array)):
        first = array[i]
        second = array[i - 1]
        if first == second and min(first, second) > 0:
            return first

    return False
