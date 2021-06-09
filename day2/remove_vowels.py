# Remove vowels

# Write a function that will remove all vowels from a given string. The function should return a string.
# Example:
# Input: ‘Joel’
# Output: ‘Jl’


    # ALEX'S SOLUTION
def rem_vowel(str):
    newStr = ""
    vowel = ("a,e,i,o,u,A,E,I,O,U")
    for x in str:
        if x not in vowel:
            newStr += x
    return newStr
print(rem_vowel('Joel'))

# MY SOLUTION WHICH DOESN'T WORK
# def rem_vowel(string):
#     newList = ('a','e','i','o','u','A','E','I','O','U')
#     for x in string:
#         if x in newList:
#             noVowel = string.split(x)
#             noVowel += string.split()
#             print(noVowel)
# print(rem_vowel("Joel"))
