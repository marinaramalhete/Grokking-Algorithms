def sum(list):
    if list == []:
        return 0
    return list[0] + sum(list[1:])


print(sum([1, 2, 3, 4]))

# python list comprehension
# return 0 if list == [] else list[0] + sum(list[1:])
