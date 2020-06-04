#Lists exercise 9
matrix1 = [[1, 3], [2, 4]]
matrix2 = [[5, 2], [1, 0]]
# Created an empty matrix in order to append (add) the calculated elements
matrix3 = []

# I want mResults = [[6, 5], [3, 4]]]
# mResults.append([6, 5])
# mResults.append([3, 4])

# This is going to locate the element each time it loops
element1 = [0, 1]
# This is going to locate the index each time it loops
index1 = [0, 1]

# Range(2) limits the loop to 2 elements from list
for element1 in range(2):
    # Created an empty element to append to final list (matrix3).
    tempList = []
    # Range(2) limits the loop to 2 indices from matrix1 and matrix2
    for index1 in range(2):
        # Appending the calculated indices to tempList[]
        tempList.append((matrix1[element1][index1]) + (matrix2[element1][index1]))
    # Appending the calculated elements of tempList to empty list of matrix3     
    matrix3.append(tempList)

print(matrix3)
