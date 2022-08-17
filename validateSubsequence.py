array = [5,1,22,25,6,-1,8,10]
sequence = [1,6,-1,10]


def validateSequence(array, sequence):

    arrayindx = 0
    seqindx = 0

    while arrayindx < len(array) and seqindx < len(sequence):
        if array[arrayindx] == sequence[seqindx]:
            seqindx += 1
        arrayindx += 1

    return seqindx == len(sequence)



print(validateSequence([5,1,22,25,6,-1,8,10], [1,6,-1,10]))

# O(N)  - Time 
# O(1)  - space 