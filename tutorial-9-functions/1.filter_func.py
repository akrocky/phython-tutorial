# ----------------filter
# -----example 1
# iterable
# letters =['a','b','c','d','e','f']
# #function
# def filter_vowels(letter):
#     vowels=['a','e','i','o','u']
#     if (letter in vowels):
#         return True
#     else:
#         return False

# filered_vowels = filter(filter_vowels,letters)
# print(filered_vowels)
# print("The filer vowels are :")

# for vowel in filered_vowels:
#     print(vowel)

# ---example 2
random_list = [1, 0, "a", False, True, "0"]

filtered_list = filter(None, random_list)
print("Truthy values are")
for value in filtered_list:
    print(value)
