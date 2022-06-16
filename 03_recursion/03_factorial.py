def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print(fact(5))

# python list comprehension
# return 1 if x == 1 else x * fact(x-1)