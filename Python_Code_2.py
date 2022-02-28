### Loops Error examples
"""

def group_list(group, users):M
  members = []
  for ind in users:
    members.append(ind)
  return '{}: {} '.format(group,', '.join(members))

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

# 
def is_palindrome(input_string):
  d = str(input_string.lower())
  stringlength = len(input_string) # calculate length of the list
  slicedString = d[stringlength::-1].replace(" ", "")
  b = d.replace(" ", "")
  if slicedString == b:
    return True
  else:
    return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True



x = 1
sum = 0
while x < 10:
  print(sum)
  sum += x
  x += 1
print(str(sum))

def count_down(start_number):
  current = 3
  while (current > 0):
    print(current)
    current -= 1
  print("Zero!")

count_down(3)

def digits(n):
  a = str(n)
  return len(a)
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

print(len('1000'))

for x in range(1, 10, 3):
    print(x)



def multiplication_table(start, stop):
	for x in range(start,stop+1):
		for y in range(start,stop+1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above

def decade_counter(year):
	while year < 50:
		year += 10
	return year

decade_counter(1)

a = str(4)
len(a) < 1

for x in range(10):
    for y in range(x):
        print(y)

def even_numbers(maximum):
  y = maximum + 1
  return_string = ""
  for x in range(2,y,2):
	  return_string += str(x) + " "
  return return_string.strip('3 5 7 9')

print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10)) # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

