# For loops and functions

produc = 1
for n in range(1,10):
  produc = produc  * n

print(produc)



def factorial(n):
    result = 1
    for i in range(1,n):
        print(i)
        result +=  result * i 
    return result

# four (4!) is equal to 1*2*3*4=24.

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

def to_celsius(x):
  return(x-32)*5/9
print('difference', str(to_celsius(x)))

for x in range(0,101,10):
  print(x, to_celsius(x))

for left in range (7):
  for right in range(left,7):
    print('['+str(left)+'/'+str(right)+']', end=' ' )
  print()

teams = ['Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_teams in teams:
    if home_team != away_teams:
      print(home_team + ' Vs ' + away_teams)

def greet_friends(friends):
  for friend in friends:
    print('Hi '+ friend)
  
greet_friends(['Taylor', 'Luisa', 'Jaamal', 'Eklo'])

greet_friends('Barry')

def validate_users(users):
  for user in users:
    if  len(user) > 3:
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(["purplecat"])

def factorial(n):
    result = 1
    for x in range(1,n):
        if n == 0:
            return 1
        else:
            result +=  result * x 
    return result

for n in range(0,10):
    print(n, factorial(n))

for x in range(0,101):
  if (x/7) - int(x/7) == 0 :
    print(x)

def retry(operation, attempts):
  for n in range(attempts):
    if operation():
      print("Attempt " + str(n) + " succeeded")
      break
    else:
      print("Attempt " + str(n) + " failed")

#retry(create_user, 3)
#retry(stop_service, 5)

print(14/7 - int(14/7))

def factorial(n):
  if n < 2:
    print('Factotrial called with ' + str(n))
    return 1
  result =  n * factorial(n-1)
  print('Retuning ' + str(result) + ' for factorial of ' + str(n))
  return result


factorial(10)

def sum_positive_numbers(n):
    # The base case is n being smaller than 1
    if n < 1:
        return int()
        pritn('Base Case')
    # The recursive case is adding this number to 
    # the sum of the numbers smaller than this one.
    print(n)
    return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

def is_power_of(number, base):
  # Base case: when number is smaller than base.
  if number < base:
    # If number is equal to 1, it's a power (base**0).
    return number == 1

  # Recursive case: keep dividing number by base.
  return is_power_of(number/base, base)

print(is_power_of(8,2)) # Should be True
print(is_power_of(64,4)) # Should be True
print(is_power_of(70,10)) # Should be False

def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      count += count_users(member) - 1 
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18
