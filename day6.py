# Write a function that takes a positive integer num and calculates how many dots exist in a pentagonalshape around the center
# dot on the Nth iteration.

# In the image below you can see the first iteration is only asingle dot. On the second, thereare 6 dots. On the third, there are
#  16 dots, and on the fourth there are 31 dots.

# ? 1 => 1
# ? 2 => 6
# ? 3 => 16
# ? 4 => 31
# ? 8 => 141

# Return the number of dots that exist in the whole pentagon on the Nth iteration.


n = int(input())
count = 1

if n == 1:
    print(n)
else:
    for i in range(1, n):
        count = count + 5*i

print(count)
