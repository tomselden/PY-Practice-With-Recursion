# Write code for algorithm 2 below
#funtion part 4 submission


# Write a Python function called max_num()to find the maximum of three numbers.

from re import X


def max_num(x, y, z):
    if x > y and x > z:
        return x, 'is the maximum'
    elif y > x and y > z:
        return y, 'is the maximum'
    elif z > x and z > y:
        return z, 'is the maximum'
    elif z == x and z > y:
        return z, " and ", x, 'are the maximum'
    elif y == x and y > z: 
        return y, " and ", x, 'are the maximum'
    elif z == y and z > x:
        return y, " and ", z, 'are the maximum'
    else:
        return x, y, z, 'are all equal. There is no maximum'


print(max_num(3, 3, 3))
print(max_num(10, 4, 3))
print(max_num(3, 9, 5))
print(max_num(1, 3, 6))
print(max_num(3, 3, 1))
print(max_num(8, 1, 8))
print(max_num(3, 5, 5))

# Write a Python function called mult_list() to multiply all the numbers in a list.

def multiply_list(num_list):  
    total = 1
    for x in num_list:
        total *= x  
    return total, " is the product of the list"  
print(multiply_list((7, 8, 1, 3, 4)))

# Write a Python function called rev_string() to reverse a string.

def reverse_string(string):
    print("This is the original string: " + string)
    reverse = string[::-1]
    return "This the the reversed string: " + reverse

print(reverse_string("ayo"))
print(reverse_string("tacocat"))

def num_within(x, y, z):
    if x > z:
        return 'x should be the starting range(lowest number), and z should be the ending range(highest number). check the input again'
    if x > y:
        return str(y) + ' is below the range provided'
    if z < y:
        return str(y) + ' is above the range provided'
    else:
        return str(y) + ' is in range of ' + str(x) +' and ' + str(z)

print(num_within(7, 2, 5))
print(num_within(4, 3, 7))
print(num_within(2, 6, 3))
print(num_within(5, 5, 5))
print(num_within(1, 2, 3))

# pascal's triangle

triangle = [[1],[1,1]]
def pascal(n):
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2

    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      length = len(row_prev) + 1
      for i in range(length):
        if i == 0:
          row.append(1)
        elif i > 0 and i < length - 1:
          row.append(triangle[row_number - 1][i - 1] + triangle[row_number - 1][i])
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    for row in triangle:
      print(row)


pascal(6)


