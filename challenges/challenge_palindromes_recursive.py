def is_palindrome_recursive(word, low_index, high_index):
    test = []
    word_reversed = ''
    if word:
        word_test = list(word)
        new_high_index = high_index
        new_low_index = low_index
        for char in word_test:
            if char == word_test[high_index] and high_index != -1:
                test.append(char)
                low_index += 1
                high_index -= 1
                new_high_index -= 1
                new_low_index += 1
                # print(low_index)
                # print(high_index)
                # print(new_low_index)
                # print(new_high_index)
                is_palindrome_recursive(word, new_low_index, new_high_index)
            # low_index += 1
            # high_index -= 1
        # print(word_reversed)
        word_reversed = "".join(test)
        if word == word_reversed:
            return True
        return False
    return False
