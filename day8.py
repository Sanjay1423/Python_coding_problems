
array = list(input().split(' '))
input = input()
new_array = []

for i in array:
    if input in i:
        new_array.append(i)

print(new_array)
