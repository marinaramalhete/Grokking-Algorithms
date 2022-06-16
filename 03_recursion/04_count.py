def count(arr):
    if not arr:
        return 0
    return 1 + count(arr[1:])

print(count([1, 10, 2, 4, 6]))

# python list comprehension
# return 1 + count(arr[1:]) if arr else 0
