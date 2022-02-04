def test_nums(nums):
    if nums == str or len(nums) == 0:
        return False

    return True


def find_duplicate(nums):
    if test_nums(nums):

        duplicated = None
        passed = set()

        for num in nums:
            if num in passed:
                duplicated = num
            else:
                passed.add(num)

        if not duplicated:
            return False

        return duplicated
