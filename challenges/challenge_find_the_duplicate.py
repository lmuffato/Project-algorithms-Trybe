# Merge sort algorith
# https://www.geeksforgeeks.org/merge-sort/

def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        i = 0
        j = 0
        
        # Iterator for the main list
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              # The value from the left half has been used
              myList[k] = left[i]
              # Move the iterator forward
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1

def array_tsts(arr):
    if(len(arr) < 2):
      raise ValueError('Pelo menos dois números')
    for x in arr:
      if(x < 1): raise ValueError('Algum valor negativo')
      if(type(x) != int): raise TypeError('Devem ser números inteiros')

def find_duplicate(nums):
    try:
      array_tsts(nums)
    except (ValueError, TypeError):
      return False

    cpp = nums.copy()
    max_sum = 0
    current_num = None
    current_sum = 0
    repeated_value = None
    merge_sort(cpp)
    for x in cpp:
      if(x is None): 
        current_num = x
        repeated_value = x
      if(current_num == x):
        current_sum += 1
        repeated_value = x
      else:
        if(current_sum > max_sum):
          max_sum = current_sum
        current_num = x
        current_sum = 1

    if(max_sum == 1):
      return False

    return repeated_value

# print(find_duplicate([1, 3, 4, 2, 2]))
# print(find_duplicate( [3, 1, 3, 4, 2]))
# print(find_duplicate([1, 1]))
# print(find_duplicate([1, 1, 2]))
# print(find_duplicate([3, 1, 2, 4, 6, 5, 7, 7, 7, 8]))
