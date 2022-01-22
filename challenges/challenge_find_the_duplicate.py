from challenges.merge_sort import merge_sort


def array_tsts(arr):
    if(len(arr) < 2):
        raise ValueError('Pelo menos dois números')
    for x in arr:
        if(x < 1):
            raise ValueError('Algum valor negativo')
        if(type(x) != int):
            raise TypeError('Devem ser números inteiros')


def it_1(obj, x):
    if(x is None):
        obj["current_num"] = x
        obj["repeated_value"] = x


def it_2(obj, x):
    if(obj["current_num"] == x):
        obj["current_sum"] += 1
        obj["repeated_value"] = x
    else:
        if(obj["current_sum"] > obj["max_sum"]):
            obj["max_sum"] = obj["current_sum"]
        obj["current_num"] = x
        obj["current_sum"] = 1


def find_duplicate(nums):
    try:
        array_tsts(nums)
    except (ValueError, TypeError):
        return False

    cpp = nums.copy()
    # max_sum = 0
    # current_num = None
    # current_sum = 0
    # repeated_value = None

    obj = {
      "max_sum": 0,
      "current_num": None,
      "current_sum": 0,
      "repeated_value": None
    }

    merge_sort(cpp)

    for x in cpp:
        it_1(obj, x)
        it_2(obj, x)

    if(obj["max_sum"] == 1):
        return False

    return obj["repeated_value"]

# print(find_duplicate([1, 3, 4, 2, 2]))
# print(find_duplicate( [3, 1, 3, 4, 2]))
# print(find_duplicate([1, 1]))
# print(find_duplicate([1, 1, 2]))
# print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))
