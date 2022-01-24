def find_duplicate(nums):
    arr = nums

    for i in range(len(arr)):
        for prox in range(i + 1, len(arr)):
            if type(arr[i]) == str or arr[i] < 0:
                return False
            if arr[prox] == arr[i]:
                return arr[prox]

    return False
