
# ? This problem was asked by Stripe.

# ? Given an array of integers, find the first missing positive integer in linear time and constant space. In other words,
# ? find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# ? For example, the input [[3, 4, -1, 1]] should give [2]. The input [[1, 2, 0]] should give 3

array = [int(i) for i in input().split()]
for i in range(min(array), max(array)+1):
    if i not in array and i > 0:
        print(i)
        break
else:
    print(max(array)+1)
