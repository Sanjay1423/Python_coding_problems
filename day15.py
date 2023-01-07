# Highest Index (With a Twist)

# Given a name, return the letter with the highest index in alphabetical order, with its
# corresponding index, in the form of a string. You are prohibited to use max() nor is
# reassigning a value to the alphabet list allowed.

# Examples

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
#              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# alphabet_index(alphabet, "Flavio") - "22v"
# alphabet_index(alphabet, "Andrey") - "25y"
# alphabet_index(alphabet, "Oscar") - - "19s"

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
             'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

name = input().lower()


def alphabet_index(name):

    max_num = 0
    max_letter = ''

    for i in name:
        num = alphabets.index(i)
        if num > max_num:
            max_num = num
            max_letter = i

    print(f'{max_num+1}{max_letter}')


alphabet_index(name)
