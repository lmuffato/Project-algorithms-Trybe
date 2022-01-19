def find_duplicate(nums):
    counter = {}
    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
        if number in counter:
            return number
        counter[number] = True
    return False
