def find_duplicate(nums):
    verified = []
    repeated = None

    for num in nums:
        if type(num) != int or num < 1:
            return False
        
        if num in verified:
            repeated = num
        verified.append(num)

    return repeated if repeated else False
