def is_duplicated(nums):
    mid = 0
    start = 0
    end = len(nums)
    while start <= end:
        mid = (start + end) // 2
        if not isinstance(nums[mid], int) or nums[mid] < 0:
            return False
        if nums[mid] == nums[mid - 1] or nums[mid] == nums[mid + 1]:
            return nums[mid]

        start += 1


def find_duplicate(nums):
    if len(nums) == 1:
        return False
    nums.sort()
    try:
        return is_duplicated(nums)
    except IndexError:
        return False
