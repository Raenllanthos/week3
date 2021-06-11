# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Output: Because nums[0] + nums[1] == 9, we return [0, 1].
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

def numbers(list1, target):
    newlist = []
    for x in range(len(list1)):
        for y in range(len(list1)):
            if list1[x] + list1[y] == target:
                newlist.append(x)
                newlist.append(y)
                return newlist

# SHOHA'S ANSWER

def function1(nums, target):
    d = {}
    for i, n in enumerate(nums):
        print("index: ",i," element: ", n)
        difference = target - n
        if difference in d:
            return [d[difference], i]
        d[n] = 1
    return

list1 = [2,15,11,7]
print(numbers(list1, 9))

list2 = [4,2,3]
function1(list1, 9)