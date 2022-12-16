
# ? Thousands separator

# ? Write a function named format_number that takes a non-negative number as its only parameter.
# ? Your function should convert the number to a string and add commas as a thousands separator.
# ? For example, calling format number (1000000) should return "1,000,000"


def format_number(n):
    string = str(n)[::-1]
    lst = []
    count = 0
    for i in string:
        count += 1
        lst.append(i)
        if count % 3 == 0:
            lst.append(',')

    new_string = "".join(lst[::-1])
    print(new_string)


format_number(1000000)
