def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:])


print(count([1, 3, 6]))

# return 0 if list == [] else 1 + count(list[1:])
