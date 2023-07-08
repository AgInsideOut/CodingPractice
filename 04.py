# # A function that accumulates (sums) all numbers in the array.

# arr = [1, 2, 3, 4, 5]
# # Should return 15

# def accumulate(arr):
#     arr_sum = 0
#     for i in range(0, len(arr)):
#         arr_sum = arr_sum + arr[i];
#     return arr_sum
    
# if isinstance(arr, list):    
#     print(accumulate(arr))
# else:
#     print("Wrong data type. Try again")

#---

# # A function that gets the most frequent word from a sentence.

# # * Usage:
# sentence = "apple apple orange apple banana banana apple"

# # * Output: "apple"

# def freq_word(sentence):
#     words = sentence.split()
#     max_occurrence = 0
#     most_frequent_word = ""
        
#     for word in words:
#         occurrence = words.count(word)
#         if occurrence > max_occurrence:
#             max_occurrence = occurrence
#             most_frequent_word = word
        
#         return most_frequent_word
    
# result = freq_word(sentence)
# print(result)

#---

# # A function that finds the youngest person from an array of objects.
# array = [{ "name": "John", "age": 20 }, { "name": "Jane", "age": 19 }]
# # Output: "Jane"

# min_age = float("inf")                              # initialise min age
# min_age_pers = ""                                   # initialise min age person

# for person in array:                                # loop through array        
#     age = person["age"]                             # save age values from "age" key
#     if age < min_age:                                       
#         min_age = age                               # loop through age values to save the lowest
#         min_age_pers = person                       # find person being of min age

# print(min_age_pers["name"])                         # print person name

#---








