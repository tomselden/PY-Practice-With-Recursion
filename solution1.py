# Write code for algorithm 1 below


# def recursive(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         recursive(n - 1)

# n = 6
# recursive(n)

import string


def natural_numbers(x,i=1):
	#base case
  if i > x:
    return
  #recursive case
  else:
    print(i)
    natural_numbers(x,i+1)
natural_numbers(3)

def name_args(**kwargs):
  for k in kwargs:
    print(f"{k}:{kwargs[k]}")

name_args(name="Tom", weather="raining",location="Allenhurst",time=7)

# one_true - Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.

def one_true(iter):
    y = any(iter)
    return y

my_list = [True, False, False]
my_list2 = [False, False, False]
print(one_true(my_list2))
print(one_true(my_list))

# All true

def all_true(iter):
  return all(iter)

print(all_true([True,True,True]))
print(all_true((True, True, False)))

# recursive_factorial - Uses recursion to find the factorial of an integer

def recur_factorial(n):
    if (n == 1 or n == 0):
        return n
    else:
        return n*recur_factorial(n-1)

num = -3

if num < 0:
    print("Factorial doesn't exist for negative number")
elif num == 0:
    print("The factorial is 1")
else:
    print("The factorial of ", num, " is ", recur_factorial(num))


# recursive_deduplicate - Recursively removes all adjacent duplicate letters from a string.
# Input: AABBCCDD
# Output: ABCD

def recurs_deduplicate(string):
    if not string:
        return ""
    if len(string) == 1:
        return string
    elif string[0] == string[1]:
        return recurs_deduplicate(string[1:])
    return string[0] + recurs_deduplicate(string[1:])
print(recurs_deduplicate("yooooooooo"))
print(recurs_deduplicate("aaaayyyyyoooo"))
print(recurs_deduplicate("AABBCCDD"))
print(recurs_deduplicate(""))
print(recurs_deduplicate("A"))