

def sortedSquaresArray(array):

    sortedSquares = [0 for _ in array]

    left = 0
    right = len(array) - 1

    for idx in reversed(range(len(array))):
        if abs(array[left]) > abs(array[right]):
            sortedSquares[idx] = array[left] * array[left]
            left += 1
        else:
            sortedSquares[idx] = array[right] * array[right]
            right -= 1

    return sortedSquares


print(sortedSquaresArray([-4,-2, 0,1,2]))