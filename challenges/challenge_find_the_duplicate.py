# REF course trybe;
def do_sort(array):
    has_swapped = True
    num_of_iterations = 0

    while has_swapped:
        has_swapped = False

        for i in range(len(array) - num_of_iterations - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        num_of_iterations += 1

    return array


def find_duplicate(nums):
    if len(nums) == 0 or len(nums) == 1:
        return False
    result = False
    ordered_nums = do_sort(nums)
    for i in range(0, len(ordered_nums) - 1):
        if type(ordered_nums[i]) != int or ordered_nums[i] < 0:
            return False
        if ordered_nums[i] == ordered_nums[i + 1]:
            result = ordered_nums[i]
            return result
    return result
