#TASK
""" Write a function that accepts a string and returns the longest possible palindromic substring of the string.
NB: you can assume that there will be only one longest palindromic substring. """

#---

# # PSEUDO CODE
# # check if 2 consecutive same characters are present
# # if so, the center of the possible palindrome is in between them
# # switch paths depending on whether the potential palindrome has a letter in its centre or not
# # loop through the letters of a string from the centre to the left and to the right adding same numbers to consecutive arrays
# # join the letters from arrays to print the palindrome string

# # INPUT
# string = "wrtfawmnoonmz"

# # CODE
# def check_same_char(string):
#     for i in range(0, len(string) - 1):
#         if string[i] == string[i + 1]:
#             return check_even_pal(string, i)
#         elif string[i] == string[i + 2]:
#             return check_uneven_pal(string, i)
#     return ""

# def check_even_pal(string, i):                              # left_side = string[i] and right_side = string[i + 1]
#     left_array = []
#     right_array = []
#     current_index = i
#     while current_index >= 0 and i + 1 < len(string):
#         if string[current_index] == string[i + 1]:
#             left_array.append(string[current_index])
#             right_array.append(string[i + 1])
#             current_index -= 1
#             i += 1
#         else:
#             break
#     left_word = ''.join(left_array[::-1])
#     right_word = ''.join(right_array)
#     word = left_word + right_word
#     return word

# def check_uneven_pal(string, i):                            # left_side = string[i] and right_side = string[i + 2]   
#     center = string[i + 1]
#     left_array = []
#     right_array = [center]
#     current_index = i
#     while current_index >= 0 and i + 2 < len(string):
#         if string[current_index] == string[i + 2]:
#             left_array.append(string[current_index])
#             right_array.append(string[i + 2])
#             current_index -= 1
#             i += 1
#         else:
#             break
#     left_word = ''.join(left_array[::-1])
#     right_word = ''.join(right_array)
#     word = left_word + right_word
#     return word

# print(check_same_char(string))

#---

# string = "wrtfawmnoonmz"                                                        ## Input string

# def lngst_pal_str(string):
#     lngst_pal = ""                                                              ## Define final longest palindorme

#     for i in range(len(string)):
#         pal_odd = exp_centr(string, i, i)                                       ## Search for odd palindrome 
#         pal_even = exp_centr(string, i, i + 1)                                  ## Search for even palindrome

#         if len(pal_odd) > len(lngst_pal):
#             lngst_pal = pal_odd                                                 ## Check if the longest is odd palindrome
#         if len(pal_even) > len(lngst_pal):
#             lngst_pal = pal_even                                                ## Check if the longest is even palindrome

#     return lngst_pal                                                            ## Return final longest palindrome

# def exp_centr(string, left, right):
#     while left >= 0 and right < len(string) and string[left] == string[right]:  ## Expand palindrome around the centre
#         left -= 1
#         right += 1

#     return string[left + 1:right]                                               ## Return the palindrome string found

# string = "wrtfawmnoonmz"
# print(lngst_pal_str(string))                                                    ## Call the function lngst_pal_str to start the search process for string input

#---