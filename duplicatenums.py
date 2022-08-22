# Problem Statement#
# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
# The array has only one duplicate but it can be repeated multiple times. 
# Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

# Example 1:

# Input: [1, 4, 4, 3, 2]
# Output: 4
# Example 2:

# Input: [2, 1, 3, 3, 5, 4]
# Output: 3
# Example 3:

# Input: [2, 4, 1, 4, 4]
# Output: 4

def find_dup(nums):

    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

        else:

            i+=1
    
    for i in range(len(nums)):

        if nums[i] != i +1:
            return nums[i]
    

def main():
    print("the duplicate num is " + str(find_dup([1, 4, 4, 3, 2])))
    print("the duplicate num is " + str(find_dup([2, 1, 3, 3, 5, 4])))
    print("the duplicate num is " + str(find_dup([2, 4, 1, 4, 4])))

main()



# Similar Problem Statement#
# We are given an unsorted array containing n numbers taken from the range 1 to n. 
# The array has some numbers appearing twice, find all these duplicate numbers using constant space.

# Example 1:

# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]
# Example 2:

# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]


def find_alldup(nums):
    
    i = 0

    while i < len(nums):
        j = nums[i] - 1

        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]

        else:

            i+=1
    
    duplicates = []
    for i in range(len(nums)):

        if nums[i] != i +1:
            duplicates.append(nums[i])
    
    return duplicates
    

def main():
    print("the duplicate num is " + str(find_alldup([3, 4, 4, 5, 5])))
    print("the duplicate num is " + str(find_alldup([5, 4, 7, 2, 3, 5, 3])))

main()