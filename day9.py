# A number is said to be Disarium if the sum of its digits raised to their respective positions is the number itself.
# Create a function that determines whether a number is a Disarium or not.

# Examples

# is_disarium (75) → False  7^1 + 5^2 = 7+ 25 = 32
# is_disarium (135) → True 1^1 + 3^2 + 5^3 = 1 + 9 + 125 = 135
# is_disarium (544) → False
# is_disarium (518) → True
# is_disarium (466) → False
# is_disarium (8) → True

import math
n = input()


def is_disarium(num):
    sum = 0
    count = 1
    for i in num:
        sum = sum + math.pow(int(i), count)
        count += 1

    if sum == int(num):
        print(True)
    else:
        print(False)


is_disarium(n)
