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

def is_anagram(first_string, second_string):
    if(len(first_string)==0 or len(second_string)==0): return False

    str1 = [*first_string]
    str2 = [*second_string]
    output = True

    merge_sort(str1)
    merge_sort(str2)

    for x, y in zip(str1, str2):
      output = output and (x == y)

    return output


print(is_anagram('amor', 'roma'))
# print(is_anagram('pedra', 'perda'))
# print(is_anagram('coxinha', 'empada'))

first_string = (
            "Lorem ipsum dolor sit amet, consectetur "
            "adipiscing elit, do sed eiusmod tempor "
            "incididunt ut labore et dolore magna aliqua."
        )

second_string = (
    "Lorem ipsum dolor sit amet, consectetur "
    "adipiscing elit, do sed eiusmod tempor "
    "incididunt ut labore et dolore magna aliqua."
)

# print(is_anagram(first_string, second_string))
