# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.
# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.
# You can assume that the messages are decodable. For example, '001' is not allowed.


# ? 1 => 'a'
# ? 11 => 'a' + 'k'
# ? 111 => 'aaa' + 'ak' + 'ka'
# ? 1111 => 'aaaa' + 'aak' + 'kaa'  + 'aka' + 'kk'
# ? 11111 => 'aaaaa' + 'kaaa'+ 'akaa' + 'aaka' + 'aaak' + 'kka' + 'kak' + 'akk'
# ? 111111 => 'aaaaaa' + 'kaaaa' + 'akaaa' + 'aakaa' + 'aaaka' + 'aaaak' + 'akak' + 'kkaa' + 'kaak' + 'aakk' + 'kaka' + 'akak' + 'kkk'


# 1 => 1
# 2 => 2
# 3 => 3
# 4 => 5
# 5 => 8
# 6 => 13
# 7 => 21
# 8 => 34
# 9 => 55
# 10 => 89

num = len(input())

count1 = 1
count2 = 2

if num == 1:
    print(num)
if num == 2:
    print(num)
else:
    for i in range(0, num-3):
        count1, count2 = count2, count1 + count2

print(count1+count2)
