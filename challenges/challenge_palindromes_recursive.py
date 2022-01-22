def is_palindrome_recursive(word, low_index, high_index):
    if(word==''): return False

    output = True and (word[low_index] == word[high_index])
    low_index +=1
    high_index -=1

    if(low_index>high_index or low_index==high_index):
      return output

    return is_palindrome_recursive(word, low_index, high_index)

# print(is_palindrome_recursive("ANA", 0, 2))
# print(is_palindrome_recursive("SOCOS", 0, 4))
# print(is_palindrome_recursive("REVIVER", 0, 6))
# print(is_palindrome_recursive("COXINHA", 0, 6))
# print(is_palindrome_recursive("AGUA", 0, 3))
