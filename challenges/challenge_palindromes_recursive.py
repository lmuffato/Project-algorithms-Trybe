def is_palindrome_recursive(word, low_index, high_index):
    numberOne = 1

    if(word.isalpha()):
        if(high_index < low_index):
            return True
        else:
            if(word[low_index] == word[high_index]):
                return is_palindrome_recursive(
                    word, low_index + numberOne, high_index - numberOne
                )
            else:
                return False
         
    return False
