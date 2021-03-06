## Variables and The Console

---
"""

print((((1+2)*3)/4)**5)

name = "Bruke"
print("hello "+ name)

color = "azul"
thing = "the sky"
print(color + " is the color of " + thing)

print(4,"5")

print("H"+"b")

print(type('a'))
print(type(2))
print(type(2.5))

"""##defining Functions in Python"""

base = 5
height = 3
area = base*height/2

def area_triangle(height,base):
  return base*height/2

area_a = area_triangle(9,7)
area_b = area_triangle(4,6)
sum = area_a + area_b

print('the area of the tirangle is: ' + str(sum))

total = 2048 + 4357 + 97658 + 125 + 8
files = 5
average = total / files
print("The average size is: " + str(average))

print(1+1.3)

def greeting(name):
  print('welcome, ' + name)

greeting('kloe')

def print_seconds(hours, minutes, seconds):
    print(hours*3600 + minutes*60 + seconds)

print_seconds(1,2,3)

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a + amount_b
print(result)

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = seconds + hours * 3600 // 60
  total_seconds = seconds + hours * 3600 + minutes*60
  return hours, minutes, total_seconds

hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)

def month_days(month, days):

    print(month + ' has ' + str( days) + ' days')

month_days('june',30)
month_days('july',31)

def rectangle_area(base, height):
	area = base * height
	print("The area is " + str(area))
rectangle_area(5,6)

# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
  km = miles * 1.6  # approximately 1.6 km in 1 mile
  return km
my_trip_miles = convert_distance(55)

my_trip_km = my_trip_miles


print("The distance in kilometers is " + str(my_trip_km))

print("The round-trip in kilometers is " + str(my_trip_km*2))

"""## Comparing Things"""

print(10>1)
print('cat' == 'dog')
print(1!=2)
print(1 == '1')
print(2 != '2') #WTF
print("cat" > "Cat")

"""Logical Operators (and, or, and not)"""

print("Yellow" > "Cyan" and "Brown" > "Magenta")

print(25 > 50 or 1!=2)

print(not 42 == 'Answer')

"""## **Branching** with if Statements

"""

def hint_username(username):
  if int(username):
    print("Numbers are not abalible")
    exit()
  else:
     print("Success")
     exit()
  if len(username) <  3:
    print("Invalid username. Must be al least 3 characters long")
    exit()

hint_username(input())

def is_positive(number):
  if int(number) > 0 :
    return(True) # I can create a True or false Output condition
  else:
    return False

is_positive(12)

def is_even(number):
  if number % 2 == 0:
    return True
  return False

def hint_usernam(usernameR):
  if len(usernameR) < 3:
    print("Numbers are not abalible")
  elif len(usernameR) > 15:
    print("Invalid username")
  else:
     print("Valid username")

hint_usernam("mskdjenfllVEVeweWEW")

def greeting(name):
  if (name) == "Taylor":
    return "Welcome back Taylor!"
  else:
    return "Hello there, " + name

print(greeting("Taylor"))
print(greeting("John"))

number =10
if number > 11: 
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

def calculate_storage(filesize):
    block_size = 4096
  
    full_blocks = filesize // block_size

    partial_block_remainder = filesize % block_size

    block_rem = (1 + full_blocks)*block_size

    if partial_block_remainder > 0:
        return block_rem
    return block_size*(full_blocks)

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192

def color_translator(color):
	if color == "red":
		hex_color = "#ff0000"
	elif color == "green":
		hex_color = "#00ff00"
	elif color == "blue":
		hex_color = "#0000ff"
	else:
		hex_color = "unknown"
	return hex_color
  
print(color_translator("blue")) # Should be #0000ff
print(color_translator("yellow")) # Should be unknown
print(color_translator("red")) # Should be #ff0000
print(color_translator("black")) # Should be unknown
print(color_translator("green")) # Should be #00ff00
print(color_translator("")) # Should be unknown

print("big" > "small") # Prinf True or false depending on the len() of the variables

def exam_grade(score):
	if score > 95:
		grade = "Top Score"
	elif score >= 60 < 95:
		grade = "Pass"
	else:
		grade = "Fail"
	return grade

print(exam_grade(65)) # Should be Pass
print(exam_grade(55)) # Should be Fail
print(exam_grade(60)) # Should be Pass
print(exam_grade(95)) # Should be Pass
print(exam_grade(100)) # Should be Top Score
print(exam_grade(0)) # Should be Fail

print(11 % 5)

def format_name(first_name, last_name):
	empty_string = ""
	if first_name and last_name:
		string = "Name: " + str(last_name) + ', ' + str(first_name)
	elif first_name or last_name:
		string = "Name: " + str(last_name) + str(first_name)
	else:
		return empty_string
	return string 

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string

print((10 >=6*2) and (10 <= 5*2))

def sum(x, y):
		return(x+y)
print(sum(sum(1,2), sum(3,4)))

def longest_word(word1, word2, word3):
	if len(word1) >= len(word2) and len(word1) >= len(word3):
		word = word1
	elif len(word2) >= len(word1) and len(word2) >= len(word3):
		word = word2
	else:
		word = word3
	return(word)

print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

"""## More complex functions"""

def fractional_part(numerator, denominator):
	if denominator == 0:
		return 0
	fractional = (numerator / denominator)-(numerator // denominator)
	return fractional

	# Operate with numerator and denominator to 
# keep just the fractional part of the quotient

print(fractional_part(5, 5)) # Should be 0
print(fractional_part(5, 4)) # Should be 0.25
print(fractional_part(5, 3)) # Should be 0.66...
print(fractional_part(5, 2)) # Should be 0.5
print(fractional_part(5, 0)) # Should be 0
print(fractional_part(0, 5)) # Should be 0

"""## While loops"""

x = 0
while x < 5:
  print('Not ther yet, x = '+ str(x))
  x = x + 1
print('x = '+str(x))

def attempts(n):
  x = 1
  while x <= n:
    print('attempt ' + str(x))
    x += 1
  print('Done')

attempts(5)

x = "infine_loop_if_x=0"
while x % 2 == 0:
  x = x / 2
  print(x)

# if x !=0:
  # while x % 2 == 0:
 # x = x / 2

#while True:
# do_something_cool()
  #if input():
# BREAK

while x != 0 and x % 2 == 0:
  x = X / 2

def print_range(start, end):
  n = start
  while n <= end:
    print(n)
    n += 1
print_range(1,5)

def print_prime_factors(number):
  factor = 2
  while factor <= number:
     if number % factor == 0:
        print(factor)
        number = number / factor
     else:
        factor+=1
  return "Done"

print_prime_factors(100)

def print_prime_factors(number):
  factor = 2 
  while factor <= number: 
    if number % factor == 0:     
       print(factor)
       number = number / factor 
    else:
      factor=+1
  return "Done"

print_prime_factors(100)
# Should print 2,2,5,5
# DO NOT DELETE THIS COMMENT

def is_power_of_two(n):
  while n % 2 == 0 and n != 0:
    n = n / 2
    if n == 1:
      return True
  return False
  

print(is_power_of_two(0)) # Should be False
print(is_power_of_two(1)) # Should be True
print(is_power_of_two(8)) # Should be True
print(is_power_of_two(9)) # Should be False

def multiplication_table(number):
	multiplier = 1
	while multiplier <= 5:
		result = number * multiplier
		if result > 25 :
			break
		print(str(number) + "x" + str(multiplier) + "=" + str(result))
		multiplier += 1

multiplication_table(3) 
multiplication_table(5) 
multiplication_table(8)

def sum_divisors(n):
  # Return the sum of all divisors of n, not including n
  return sum([i for i in range(1, n)
                if n % i == 0])
                
print(sum_divisors(0))
# 0
print(sum_divisors(3)) # Should sum of 1
# 1
print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# 55
print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# 114

print(3//2)

"""## Fr loops"""

for z  in range(5):

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += n*n   
        print(sum) 
    return sum
  

print(sum_squares(10)) # Should be 285

friends =  ['Gale', 'Kayle', 'Gislayne', 'Rudeus', 'Rugierd', 'Roxi', 'Sylphie', 'Norn', 'Rinia', 'Pursena', 'Eris']
for friend in friends:
  print('Hi, '+ friend+'!')

values = [23, 52, 59, 37, 48 ]
sum = 0
lenght = 0
for value in values:
  sum += value
  lenght += 1

print('Total sum: '+ str(sum) + ' - Avarage ' + str(sum/lenght))
