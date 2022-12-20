# This problem was asked by Airbnb.

# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
# For example, [[2, 4, 6, 2, 5]] should return[13], since we pick 2, 6, and 5
# [5, 1, 1, 5] should return 10, since we pick 5 and 5


array = [int(i) for i in input().split(' ')]
if len(array) == 0:
    print(0)
elif len(array) == 1:
    print(array[0])
else:
    maxSum = array[:2]
maxSum[1] = max(maxSum[0], maxSum[1])

for i in range(2, len(array)):
    curSum = max(maxSum[1], maxSum[0] + array[i])
    maxSum[0] = maxSum[1]
    maxSum[1] = curSum

print(maxSum[1])
