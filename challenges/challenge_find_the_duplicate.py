def find_duplicate(nums):
    repeated_number = 0
    array = []
    for num in nums:
        if type(num) == str or num < 0:
            return False
        if num in array:
            repeated_number = num
        else:
            array.append(num)
    if repeated_number == 0:
        return False
    return repeated_number
