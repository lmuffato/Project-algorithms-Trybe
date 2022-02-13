from challenges.challenge_anagrams import merge_sort


def find_duplicate(nums):
    start = 0
    end = len(nums) - 1

    merge_sort(nums, start, end)

    while len(nums) > 1:
        last_number = nums.pop()

        if type(last_number) is str:
            break

        if last_number < 0:
            break

        if (last_number == nums[-1]):
            return last_number
    return False
