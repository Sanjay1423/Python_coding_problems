# This problem was asked by Amazon.
# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

input = input()
number = int(input())
string = ""
list = []
for i in input:
    string += i
    if len(set(string)) > number:
        m = string[0]
        string = string.replace(m, '')
    if len(set(string)) == number:
        list.append(string)
print(max(list, key=len))
