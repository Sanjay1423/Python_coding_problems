
#? This problem was asked by Uber.
#? Given an array of integers, return a new array such that each element at index [i] of the new array is the product of all the numbers in the original array except the one at i
#? For example, if our input was
#? [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was
#? [3, 2, 1], the expected output would be [2, 3, 6]

array1 = [int(i) for i in input().split()]

array2 = []

for i in range(len(array1)):
    prod = 1
    array3 = [array1[j] for j in range(len(array1)) if j != i]
    for j in array3:
        prod *= j
    array2.append(prod)

print(array2)
