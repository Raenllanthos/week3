# Find Even Numbers
# -----------------
# Create a function that, given a list as a parameter, 
# finds the even numbers inside the list. 
# The function should then return a list.
# Example:
# Input: [2, 7, 10, 11, 12]
# Output: [2, 10, 12]

def evenFinder(List):
    new = [number for number in List if number % 2 == 0]
    # for number in List:
    #     if number % 2 == 0:
    #         new.append(number)
    return new

List = [2, 7, 11, 10, 12]
print(evenFinder(List))
print("\U0001F525")