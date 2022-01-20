def extract_duplicate(nums):
    nums_list = []
    duplicate = []
    for index in range(len(nums)):
        if nums[index] not in nums_list:
            nums_list.append(nums[index])
        else:
            duplicate.append(nums[index])
    return duplicate


def find_duplicate(nums):
    duplicate = []
    if nums:
        duplicate = extract_duplicate(nums)
        for num in duplicate:
            if len(duplicate) > 0 and num > -1:
                return num
            return False
    return False

# Para montar a lógica deste algoritmo
# foram consultadas as seguintes fontes:
# https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
