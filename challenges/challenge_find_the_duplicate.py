def find_duplicate(nums):
    if len(nums) == 1:
        return False
    nums.sort()
    mid = 0
    start = 0
    end = len(nums)
    while start <= end:
        mid = (start + end) // 2
        try:
            if not isinstance(nums[mid], int) or nums[mid] < 0:
                return False
            if nums[mid] == nums[mid - 1] or nums[mid] == nums[mid + 1]:
                return nums[mid]
            else:
                start += 1
        except IndexError:
            return False
