""" The scroller works by replacing the current text string with a similar text string, but 
with the first letter shifted to the end; this simulates movement. Your father is far 
too busy with the business to worry about such details, so, naturally, he's making you 
come up with the text strings. Create a function named rotate() that accepts a string 
argument and returns an array of strings with each letter from the input string being 
rotated to the end. rotate("Hello") // => ["elloH", "lloHe", "loHel", "oHell", "Hello"]
Note: The original string should be included in the output array. The order matters. 
Each element of the output array should be the rotated version of the previous element. 
The output array SHOULD be the same length as the input string. The function should 
return an empty array with a 0 length string, '', as input. """


# def rotate(str_):
#     rotation = []
#     count = 0
#     rot = str_
#     while count < len(str_):
#         rot = rot[1:] + rot[0]
#         rotation.append(rot)
#         count += 1
#     return rotation  
    
# print(rotate("Hello"))

##--

# def rotate(str_):
#     return [str_[i + 1:] + str_[:i + 1] for i in range(len(str_))]

# print(rotate("Hello"))

##--

# rotate = lambda s: [s[-i:]+s[:-i] for i in range(len(s))][::-1]
# print(rotate("Hello"))

##---

""" In this kata you will create a function that takes in a list and returns a list with the reverse order.

Examples (Input -> Output)

* [1, 2, 3, 4]  -> [4, 3, 2, 1]
* [9, 2, 0, 7]  -> [7, 0, 2, 9] """

# def reverse_list(l):
#     'return a list with the reverse order of l'
#     return l[::-1]   
    
# l = [1, 2, 3, 4]
# print(reverse_list(l))

##---

""" Your team is writing a fancy new text editor and you've been tasked with implementing the line numbering.
Write a function which takes a list of strings and returns each line prepended by the correct number.
The numbering starts at 1. The format is n: string. Notice the colon and space in between.
Examples: (Input --> Output)

[] --> []
["a", "b", "c"] --> ["1: a", "2: b", "3: c"] """

# lines = ["a", "b", "c"]

# def number(lines):
#     new_array = []
#     for i in lines:
#         new_array.append(f"{lines.index(i)+1}: {i}")
#     return new_array

# print(number(lines))

##--

# lines = ["a", "b", "c"]
# number = map(lambda x: f"{x[0]+1}: {x[1]}", enumerate(lines))
# print(list(number))

##--

# lines = ["a", "b", "c"]

# def number(lines):
#     new_array = []
#     for index, value in enumerate(lines, 1):
#         new_array.append(f"{index}: {value}")
#     return new_array
    
# print(number(lines))

##--

# lines = ["a", "b", "c"]

# def number(lines):
#     new_array = []
#     index = 1
#     for i in lines:
#         new_array.append(f"{index}: {i}")
#         index += 1
#     return new_array

# print(number(lines))

##--

# lines = ["a", "b", "c"]
# number = list(map(lambda x: f"{x[0]+1}: {x[1]}", enumerate(lines)))
# print(number)

##---

""" Create a function that accepts a string and a single character, and 
returns an integer of the count of occurrences the 2nd argument is found in the first one.
If no occurrences can be found, a count of 0 should be returned.

("Hello", "o")  ==>  1
("Hello", "l")  ==>  2
("", "z")       ==>  0
str_count("Hello", 'o'); // returns 1
str_count("Hello", 'l'); // returns 2
str_count("", 'z'); // returns 0 """

# def str_count(strng, letter):
#     count = 0
#     for i in strng:
#         if letter in strng:
#             count += 1
#     return count

##--

# def str_count(strng, letter):
#     count = 0
#     for i in strng:
#         if i == letter:
#             count += 1
#     return count

# print(str_count("Hello", 'o'))

##--

# def strCount(string, letter):
#     return string.count(letter)

# print(strCount("Hello", 'o'))

##---

""" The Story:
Bob is working as a bus driver. However, he has become extremely popular amongst the city's residents. 
With so many passengers wanting to get aboard his bus, he sometimes has to face the problem of not enough 
space left on the bus! He wants you to write a simple program telling him if he will be able to fit all 
the passengers.
Task Overview:
You have to write a function that accepts three parameters:
cap is the amount of people the bus can hold excluding the driver.
on is the number of people on the bus excluding the driver.
wait is the number of people waiting to get on to the bus excluding the driver.
If there is enough space, return 0, and if there isn't, return the number of passengers he can't take.
Usage Examples:
cap = 10, on = 5, wait = 5 --> 0 # He can fit all 5 passengers
cap = 100, on = 60, wait = 50 --> 10 # He can't fit 10 of the 50 waiting """

# def enough(cap, on, wait):
#     if wait <= (cap - on):
#         return 0
#     else:
#         return wait - (cap - on)

##--



