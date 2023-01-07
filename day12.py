# This problem was asked by Google.
# Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray
# of length k.
# For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

# • 10 = max(10, 5, 2)
# • 7 = max(5, 2, 7)
# • 8 = max(2, 7, 8)
# • 8 = max(7, 8, 7)

input_array = [int(i) for i in input().split(' ')]
output_array = []

for i in range(0, len(input_array)-2):
    temp_array = []

    for j in range(i, i+3):
        temp_array.append(input_array[j])

    output_array.append(max(temp_array))

print(output_array)
