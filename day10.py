# This problem was asked by Amazon.
# There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function
# that returns the number of unique ways you can climb the staircase. The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:

# • 1, 1, 1, 1
# • 2, 1, 1
# • 1, 2, 1
# • 1, 1, 2
# • 2,2


number = int(input())
num1 = 0
num2 = 1
sum = 0

for i in range(number):
    sum = num1+num2
    num1 = num2
    num2 = sum

print(sum)
