def partition(word, low, high):
    center = (high - low) >> 1
    pivot = word[low + center]
    i = low
    j = high
    while True:
        while word[i] < pivot:
            i = i + 1
        while word[j] > pivot:
            j = j - 1
        if i >= j:
            break
        word[i], word[j] = word[j], word[i]
        i = i + 1
        j = j - 1
    word[i], word[high] = word[high], word[i]
    return i


def quick_sort(word, low, high):
    if low < high:
        pivot = partition(word, low, high)
        quick_sort(word, low, pivot-1)
        quick_sort(word, pivot, high)


def find_duplicate(nums):
    nums = [*nums]
    if len(nums) == 1:
        return False
    quick_sort(nums, 0, len(nums) - 1)
    for index in range(len(nums)):
        if isinstance(nums[index], str) or nums[index] < 0:
            return False
        if nums[index - 1] == nums[index]:
            return nums[index]
    return False
