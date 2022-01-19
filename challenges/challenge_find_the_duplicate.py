def find_duplicate(nums):
    counter = {}
    for number in nums:
        try:
            assert isinstance(number, int)
            assert number >= 0
            if counter[number]:
                return number
        except AssertionError:
            return False
        except KeyError:
            counter[number] = True
    return False