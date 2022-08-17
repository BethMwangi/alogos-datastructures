array = [3, 5, -4, 8, 11, -1, 1, 6]

targetSum = 10

seen = {}

# def targetSumArray(array, targetSum):
#     for num in array:
#         if targetSum - num in seen:
#             return [targetSum-num, num]
#         else:

#             seen[num] = True
#     return []


# def targetArrayIndex(array, targetSum):
#     for i, num in enumerate(array):
#         if targetSum - num in seen:
#             return [seen[targetSum-num], i]
#         else:
#             seen[num] = i

#     return []


def targetArrayIndex(array, targetSum):
    for i in range(len(array)):
        if targetSum - array[i] in seen:
            return [seen[targetSum-array[i]], i]
        else:
            seen[array[i]] = i

    return []



print (targetArrayIndex([3, 5, -4, 8, 11, -1, 1, 6], 10))

