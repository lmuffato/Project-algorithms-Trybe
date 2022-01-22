# Merge sort algorith
# https://www.geeksforgeeks.org/merge-sort/

def loop1(obj, left, right, myList):
    while obj['i'] < len(left) and obj['j'] < len(right):
        if left[obj['i']] <= right[obj['j']]:
            # The value from the left half has been used
            myList[obj['k']] = left[obj['i']]
            # Move the iterator forward
            obj['i'] += 1
        else:
            myList[obj['k']] = right[obj['j']]
            obj['j'] += 1
        # Move to the next slot
        obj['k'] += 1


def loop2(obj, left, right, myList):
    while obj['i'] < len(left):
        myList[obj['k']] = left[obj['i']]
        obj['i'] += 1
        obj['k'] += 1

    while obj['j'] < len(right):
        myList[obj['k']] = right[obj['j']]
        obj['j'] += 1
        obj['k'] += 1


def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        # Recursive call on each half
        merge_sort(left)
        merge_sort(right)

        # Two iterators for traversing the two halves
        # i = 0
        # j = 0
        # Iterator for the main list
        # k = 0

        obj = {
          "i": 0,
          "j": 0,
          "k": 0
        }

        loop1(obj, left, right, myList)

        # For all the remaining values
        loop2(obj, left, right, myList)
