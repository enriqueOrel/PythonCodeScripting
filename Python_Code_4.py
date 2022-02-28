## Indexing string method
"""

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
newfilenames = []
for string in filenames:
  if '.hpp' in string:
    position = string.index('.hpp')
    new_string = string[0:position]+'.h'
    newfilenames.append(new_string)
  else:
    newfilenames.append(string)
print(newfilenames)



# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

def pig_latin(text):
  new_text = text.split()
  say = ""
  for wordp in new_text:
    new_word = wordp[1:len(wordp)]+ wordp[0] + 'nya '
    say += new_word
  return say

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"

def octal_to_string(octal):
    result = ""
    value_letters = [(4,"r"),(2,"w"),(1,"x")]
    # Iterate over each of the digits in octal
    for lista in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if lista >= value:
                result += letter
                lista -= value
            else:
                result += '-'
    return result
    
print(octal_to_string(755)) # Should be rwxr-xr-x
print(octal_to_string(644)) # Should be rw-r--r--
print(octal_to_string(750)) # Should be rwxr-x---
print(octal_to_string(600)) # Should be rw-------

def group_list(group, users):
  members = ''
  for ind in users:
    members += ind+', '
  return '{}: {} '.format(group,members)

print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"

def guest_list(guests):
	for person in guests:
		name, age, ocuppation = person
		print('{} is {} years old and works as {}'.format(name,age,ocuppation))



guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])

#Click Run to submit code
"""
Output should match:
Ken is 30 years old and works as Chef
Pat is 35 years old and works as Lawyer
Amanda is 25 years old and works as Engineer
"""



def first_and_last(message):
    if len(message) == 0:
        return True
    elif message[0] == message[-1]:
        return True
    

    return False

print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

"""## DICTIONARIES


"""

file_counts = {'jpg': 10, 'txt' : 14, 'csv' : 2, 'py' : 23}
print(file_counts)
print(type(file_counts))

print(file_counts['txt'])

print('jpg' in file_counts)

file_counts['cfg'] = 8 
print(file_counts)

file_counts['txt'] = 28
print(file_counts)

file_counts['page'] = 5

# Del method keyword
del file_counts['cfg']
print(file_counts)

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc['Epilogue'] = 39 # Epilogue starts on page 39
toc['Chapter 3'] = 24 # Chapter 3 now starts on page 24
print(toc)# What are the current contents of the dictionary?
print('Chapter 5' in toc) # Is there a Chapter 5?

file_counts = {'jpg':10, 'txt':14, 'csv':2, 'py':23}
for extension in file_counts:
  print(extension)

# Items method
for ext , amount in file_counts.items():
  print('there are {} files with the .{} extention'.format(amount, ext))

b = {'jpg':[10,20,30], 'txt':14, 'csv':2, 'py':23}
for values in b.values():
  print(values)   # Only values

for keys in b.keys(): # Only keys
  print(keys)
b.get('jpg')

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for keys , elements in cool_beasts.items():
    print("{} have {}".format(keys, elements))

def count_letters(text):
  result = {}
  space = ' '
  b = ' ' in result
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  del result[' ']
  return 'There are {}'.format(result)
  


count_letters('This is a long string with a lot of tipes of letters inside')

lis = ['a' ,  'b' , 'b', 'c ']
listas = ['d','e', 'e', 'e']

dic = {}

for lis in listas:
  dic[lis] = listas
print(dic)

a = ' a '
b = ' '
a == b

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for llaves in wardrobe.keys():
	for valores in wardrobe[llaves]:
		print("{} {}".format(valores,llaves))
  
   emails.___

def email_list(domains):
	emails = []
	for users in domains.keys():
	  for user in domains[users]:
	    emails.append(user+'@'+users)
	return emails

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups in group_dictionary.keys():
		# Now go through the users in the group
		for users in group_dictionary[groups]:
			user_groups[users] = groups
			# Now add the group to the the list of
# groups for this user, creating the entry
# in the dictionary if necessary
	return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] }))

def groups_per_user(group_dictionary):
	user_groups = {}
	# Go through group_dictionary
	for groups in group_dictionary.keys():
		# Now go through the users in the group
		for users in group_dictionary[groups]:
			if users in user_groups:
				user_groups[users].append(groups)
			else:
				user_groups[users] = [groups]
	return user_groups


print(groups_per_user({"local": ["admin", "userA"],
		"public":  ["admin", "userB"],
		"administrator": ["admin"] , 'grv': ["userB"] }))

"""## Slice of a string"""

# It goes from the character 1 to the 4
color = 'Orenge'
print(color[1:4])
# It goes from the character 0 the 4
beta = 'Yellows'
print(color [:4])
# It goes from the character 4 to the last
tester = 'GrandefAuto'
print(color[4:])

"""Creating new strings"""

message = 'A kong string with a silly typo'
# message[2] = 'l' (this will result in an error)
# It's not possinle to modify the content of a string

new_message = message[0:2] + 'l' +  message[3:]
print(new_message)

# But it's possible to assigne new values to a variable

message = "This is a new string"
print(message)

message = "And another one"
print(message)

# wich character to chance 

pets = "Cats && Dogs"

# Is possible to acces to a simble in a string using the 
# Method with a specific class 

pets.index("&")
 
# I retuns the index of the sub string in others words the position
# of the fist character in the substring

pets.index("C")
pets.index("Dogs")

word = "supercalifragilisticexpialidocious"
print(word.index("x"))

# This is how is posible to know if a subbstring is cointein in a string
print("Dragons" in pets )
print("Cats" in pets  )

"""Real solving problem"""

# This is a funtion that replace the old domain of a email adress for a new one

def replace_domain(email, old_domain, new_domain):
  if "@" + old_domain in email:
    index = email.index("@" + old_domain)
    print(index)
    new_email = email[:index] + "@" + new_domain
    return new_email
  return email

replace_domain('enrrique@hormail.com', 'hormail.com', 'ermail.com')

print('Montains'.upper() + ' and its opposite '   'Montains'.lower())
# Mayusculas y minusculas

answer  = 'YES'
if answer.lower() == 'yes':
  print('User said yes')

'yes '.strip()
#strip metod removed spaces, tabs and new lines characters

' Yeah '.lstrip()
# eliminate spaces to the left 

' Yeah '.rstrip()
# eliminate spaces to the rigth

'The number of times e accurs in this string is 4'.count('e')
#Count how many times the letter appears in to the string

'Forest'.endswith('rest')
# returns  wethers the strig ends up  witd a certain sub string

mas = ['this', 'is', 'a','phrase', 'joined', 'by', 'spaces']
', '.join(mas) 
# Retuns the  countent of the dictinary with a space betwen evwry substrib
# Becouse of the space in the initial calling string

'.....'.join(['this', 'is', 'a','phrase', 'joined', 'by', 'dots']) 
# Retuns the  countent of the dictionary

"""## THE FORMAT METHOD


"""

name = 'Manny' 
number = len(name) * 3
print('Hello {}, you luky number is {}'.format(name,number))

print('Your luky number is {number},{name}'.format(name=name, number=len(name)*3))

def student_grade(name, grade):
	return "{} received {}% on the exam".format(name, grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

price = 7.5
with_tax = price * 1.09
print('Base price: ${:.2f}. with tax: ${:.2f}'.format(price,with_tax))
# this '{:.2f}' is a format funtion there are more of them to chek uot an use if needed
# : .2f = afther the. of the number as imput 2 decimal of float type class

Weather = "Rainfall"

print(Weather[:4])

def convert_distance(miles):
	km = miles * 1.6 
	result = "{:} miles equals {:.1f} km".format(miles,km)
	return result

print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

def nametag(first_name, last_name):
	return("{} {}.".format(first_name,last_name[0]))

print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G."

def replace_ending(sentence, old, new):
	end_of_string = sentence.split()
	if end_of_string[-1] == old:  
		i = sentence[:-len(old)]
		new_sentence = i + new
		return new_sentence
	return sentence
	
print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

def is_palindrome(input_string):
  new_string = ''
  reverse_string = ''
  for letter in input_string:

    return letter
  return False

print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

"""## LIST OF ELEMENTS"""

x = ['now', 'we', 'are', 'cooking!']
print(type(x))
print(x)
print(len(x))

# To check if a list cointain an element, the 'in' keyword is used
print('are' in x, 'today ' in x)
# The resul of this opetation is a Boolean, so is posible to use on brancing or looping

# Indexing
print(x[0:len(x)])

#Slicing
print(x[1:3])

def get_word(sentence, n):
	# Only proceed if n is positive 
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words 
		if n <= len(words):
			return(words[n-1])
	return("")

print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing

# Append metod add new elements at the end of the list 
fruits =  ['Pineapple', 'Banana', 'Apple', 'Melon']
fruits.append('Kiwi')
print(fruits)

# Inset an element in a position of the list
fruits.insert(0,'orange') # Using the insert method 'insert(position, 'string')'
print(fruits)

#Adding an element larger than the lengt of the list
fruits.insert(25,'Peach') 
print(fruits)

fruits.remove ('orange') # Using the method 'remove( 'string')'
print(fruits)

# Remove the string in the list by the given index position
fruits.pop (3) # Using the method 'pop( index )'
print(fruits)

# changing by asigning

fruits[2] = 'strawberry' # asigne the conten in the position 2
print(fruits)

def skip_elements(elements):
  new_list = []
  lenght = len(elements)
  growth = 0
  count = 0
  for growth in elements[0:lenght:2]:
    count += 2
    new_list.insert(count,growth)
  return new_list

    


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []

"""## TUPLA"""

# Tuples are sequences of elements of any type that are immutable. We write tuples in parentheses instead of square brackets.

# In other words, when using tuples the position of the elements inside the tuple have meaning.

def file_size(file_info):
	name, typE, bytes= file_info
	return("{:.2f}".format(bytes / 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

"""## Iterating over Lists and Tuples"""

animals = ['lion', 'zebra', 'dolphin','monkey']
chars = 0
for animal in animals:
  chars += len(animal)

print('Total character : {}, Avarage length: {}'.format(chars,chars/len(animals)))

winners = ['ashley', 'dylan', 'reese']
for index, person in enumerate(winners):
  print('{}: {}'.format(index+1, person))
#The enumerate function returns a tuple for each element in the list

def skip_elements(elements):
	new_list = elements
	lista = []
	lista += new_list[0:len(new_list):2]
	return lista
  		
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

"""def skip_elements(elements):
	new_list = elements
	lista = []
	count = 0
	for strings in enumerate(new_list):
		count += 1
		if count%2 == 1:
			lista += new_list[0:len(new_list):2]
			break
	return lista
			
		
			
print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

"""

a = 'this is another example'.split()
print(a)
# split the content (taking the spaces) of a string, and then creaing a spit of strings



def initials(phrase):
    words = phrase.split()
    result = ""
    for word in words:
        result += word[0].upper()
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
print(initials("Operating system Omem Losvus Portrait Loasf Oka")) # Should be: OS

"""
## List Comprehensions
"""

def odd_numbers(n):
	a = n
	return [x for x in range(1,a+1,2)]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

"""### **STRINGS**"""

def double_word(word):
    a = str(word * 2)
    b = str(a) + str(len(a))
    return b

print(double_word("hello")) # Should return hellohello10
print(double_word("abc"))   # Should return abcabc6
print(double_word(""))      # Should return 0
