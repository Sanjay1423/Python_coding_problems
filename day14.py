# Vowel to Vowel Links

# Given a sentence as txt, return True if any two adjacent words have this property: One word ends with a vowel, while the word immediately after begins with a vowel (a e i o u).

# Examples

# vowel_links("a very large appliance") -> True
# vowel_links("go to edabit") → True
# vowel_links("an open fire") → False
# vowel_links("a sudden applause") → False

# Notes
# You can expect sentences in only lowercase, with no punctuation.

a = ['a', 'e', 'i', 'o', 'u']

input = input().split(" ")


def vowel_links(list):
    for i in range(len(list) - 1):
        if list[i][-1] in a and list[i+1][0] in a:
            print('True')
            break
    else:
        print('False')


vowel_links(input)
