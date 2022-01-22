def is_palindrome_iterative(word):
    if(len(word) == 0): return False
    li = 0
    hi = len(word)-1
    output = True
    while(li!=hi):
      output = True and (word[li] == word[hi])
      li +=1
      hi -=1
      if(li>hi):
        break
    return output

# print(is_palindrome_recursive("ANA", 0, 2))
# print(is_palindrome_recursive("SOCOS", 0, 4))
# print(is_palindrome_recursive("REVIVER", 0, 6))
# print(is_palindrome_recursive("COXINHA", 0, 6))
# print(is_palindrome_recursive("AGUA", 0, 3))
