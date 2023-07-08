""" 1. Convert radians into degrees
Write a function in Python that accepts 
one numeric parameter. This parameter will 
be the measure of an angle in radians. 
The function should convert the radians 
into degrees and then return that value.
While you might find a Python library to 
do this for you, you should write the 
function yourself. One hint you get is 
that you’ll need to use Pi in order to 
solve this problem. You can import the 
value for Pi from Python’s math module. """

""" shift + option + A """

# import math

# PI = math.pi

# user_input = input("Provide a numeric value of an angle. / 0 - 3PI (approx. 9.42)")
# angle_rad = float(user_input)
# angle_degrees = angle_rad * 180/PI

# print(f"Your angle value in DEGREES is : {angle_degrees}")

""" Create a function in Python that accepts two parameters. 
The first will be a list of numbers. The second parameter 
will be a string that can be one of the following values: 
asc, desc, and none.
If the second parameter is “asc,” then the function should 
return a list with the numbers in ascending order. If it’s 
“desc,” then the list should be in descending order, and if 
it’s “none,” it should return the original list unaltered. """

# list_numbers = [2, 4, 8, 3, 10, 25, 1, 64, 99]

# list_asc = sorted(list_numbers)
# list_desc = reversed(list_asc)

# def function (list_numbers, sorting):
#     if sorting == "asc":
#         new_list = sorted(list_numbers, reverse = False) 
#     elif sorting == "desc":
#         new_list = sorted(list_numbers, reverse = True)
#     else:
#         new_list = list_numbers
#     return new_list
    

# print(f"The list {list_numbers} in ascending order is: {function(list_numbers,'asc')}\n")
# print(f"The list {list_numbers} in descending order is: {function(list_numbers, 'desc')}\n")  
# print(f"The list {list_numbers} without any order assigned is {function(list_numbers, 'none')}\n")      
    
""" Write a function in Python that accepts a decimal number 
and returns the equivalent binary number. To make this simple, 
the decimal number will always be less than 1,024, so the 
binary number returned will always be less than ten digits long. """

# def binary(number, places):
#     decimal_input = int(float(user_input))
#     binary_output = bin(decimal_input)
#     return binary_output

# user_input = input(f"Write a decimal less than 1.024. Format: xx.xxx\t")
# binary(user_input, 2)

# print(f"Decimal number after conversion to binary is: {binary(user_input, 2)}")

""" Create a function in Python that accepts a single word and returns the number of 
vowels in that word. In this function, only a, e, i, o, and u will be counted as 
vowels — not y. """

# count = 0
# vowels = ["a", "e", "i", "o", "u"]

# def count_vowels(word, vowels, count):
#     for i in word:
#         if i in vowels:
#             count += 1
#         else:
#             count == count
#     return count

# def print_vowels():
#     word = input("Type an word of prefference.")
#     print(f"Chosen word has {count_vowels(word, vowels, count)} vowels.")
    
# print_vowels()

""" Write a function in Python that accepts a credit card number. 
It should return a string where all the characters are hidden with an asterisk 
except the last four. For example, if the function gets sent “4444444444444444”, 
then it should return “4444”. """

# def hide_number(card_input):
#     symbol = "*"
#     output_list = []
#     count = -1
#     for i in iter(card_input):
#         count += 1
#         if count < len(card_input)-4:
#             ele = symbol
#             output_list.append(ele)
#         else:
#             ele = i
#             output_list.append(ele)
#     return output_list

# def print_message():
#     card_input = input("Type a card number. The form shall be: XXXXXXXXXXXXXXXX\t ")
#     output_list = hide_number(card_input)
#     output_number = "".join(output_list)
#     message = f"Your card number is: {output_number}"
#     return message

# print_message()





