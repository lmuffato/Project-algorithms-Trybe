def is_anagram(first_string, second_string):
    sumString = sum(map(ord, second_string))
    sumWword = sum(map(ord, first_string))
    result = False

    if(sumWword == sumString):
        for letter in second_string:
            if(len(first_string) == len(second_string)):
                if(first_string.__contains__(letter)):
                    result = True
                else:
                    result = False
            else:
                result = False

    return result
