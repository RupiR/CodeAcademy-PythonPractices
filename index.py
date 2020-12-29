# We've defined the variable "meal" here to the name of the food we ate for breakfast!
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:")
print(meal)

# Now update meal to be lunch!

meal = "A sandwich"

# Printing out lunch
print("Lunch:")
print(meal)

# Now update "meal" to be dinner
meal = "Pasta"
# Printing out dinner
print("Dinner:")
print(meal)



# ***** Python *****
# Numbers
# Define the release and runtime integer variables below:
release_year = 1996
runtime = 5


# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = 2.5

# changing numbers
quilt_width = 8
quilt_length = 12

print(quilt_width * quilt_length)

quilt_length = 8

print(quilt_width * quilt_length)

# exponents
# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)

# 7x7 quilt
print(7 ** 2)

# 8x8 quilt
print(8 ** 2)

# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 * 6 * 6 * 6)


# modulo
#1. You’re trying to divide a group into four teams. All of you count off, and you get number 27. Find out your team by computing 27 modulo 4. Save the value to my_team.
my_team = 27 % 4

#2. Print out my_team. What number team are you on?
print(my_team)

#3. Food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams? (Optional Challenge Question)
my_team = 26 % 4

print(my_team)

my_team = 28 % 4

print(my_team)


# concatenation
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1 + string2 + string3 + string4 + string5 + string6

#print(message)
print(message)



#plus equals
total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:

total_price += nice_sweater
total_price += fun_books
print("The total price is", total_price)



# multi-line strings

# Assign the string here
to_you = """ Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""


print(to_you)



# what is a function
def sing_song():
      print("You may say I'm a dreamer")
  print("But I'm not the only one")
  print("I hope some day you'll join us")
  print("And the world will be as one")
  
# call sing_song() below:
sing_song()
sing_song()



# write a function

def loading_screen():
      print("This page is loading...")

loading_screen()


# whitespace 

def about_this_computer():
      print("This computer is running on version Everest Puma")
print("This is your desktop")

about_this_computer()



# keyword arguments

# Define create_spreadsheet():
def create_spreadsheet(title, row_count = 1000):
  print("Creating a spreadsheet called "+title+"with" +str(row_count)+"rows." )

# Call create_spreadsheet() below with the required arguments:
create_spreadsheet("Downloads")
create_spreadsheet("Applications", 10)




# returns

def calculate_age(current_year, birth_year):
      age = current_year - birth_year
  return age

my_age = calculate_age(2049, 1993)
dads_age = calculate_age(2049, 1953)
print("I am " + str(my_age) + " years old and my dad is " + str(dads_age) + " years old")




# multiple return values

def get_boundaries(target, margin):
      low_limit = target - margin
  high_limit = margin + target
  return low_limit, high_limit

low, high = get_boundaries(100, 20)





#scope

current_year = 2048

def calculate_age(birth_year):
  age = current_year - birth_year
  return age
  
print(current_year)
print(calculate_age(1970))



#f_to_cemp - 32) * 5/9
  return c_temp

f100_in_celsius = f_to_c(100)


#function to convert celsius to fahrenheit
def c_to_f(c_temp):
  f_temp = (c_temp * 9/5) + 32
  return f_temp

c0_in_farenheit = c_to_f(0)


#Force function
def get_force(mass, acceleration):
  return mass * acceleration

train_force = get_force(train_mass, train_acceleration)
print(train_force)

#Exercise 7
print("The GE train supplies "+str(train_force)+" Newtons of force")

#Energy and bomb function
def get_energy(mass,c=3*10**8):
  return mass*c**2
bomb_energy=get_energy(bomb_mass)
print("A 1kg bomb supplies "+str(bomb_energy)+" Joules.")

#Get work function
def get_work(mass,acceleration,distance):
  force=get_force(mass,acceleration)
  return force*distance
train_work=get_work(train_mass,train_acceleration,train_distance)
print("The GE train does "+str(train_work)+" Joules of work over "+str(train_distance)+" meters.")



#function to power

# Write your tenth_power function here:
def tenth_power(num):
  return num**10
# Uncomment these function calls to test your tenth_power function:
print(tenth_power(1))
# 1 to the 10th power is 1
print(tenth_power(0))
# 0 to the 10th power is 0
print(tenth_power(2))
# 2 to the 10th power is 1024


# function square root
# Write your square_root function here:
def square_root(num):
  result = num ** 0.5
  return result
# Uncomment these function calls to test your square_root function:
print(square_root(16))
# should print 4
print(square_root(100))
# should print 10




# Win Percentage

# Write your win_percentage function here:
def win_percentage(wins, losses):
  return wins / (wins + losses) * 100
# Uncomment these function calls to test your win_percentage function:
print(win_percentage(5, 5))
# should print 50
print(win_percentage(10, 0))
# should print 100




# Average function

# Write your average function here:
def average(num1, num2):
  return (num1 + num2) / 2
# Uncomment these function calls to test your average function:
print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0




# Remainder function - the python modulo operator

# Write your remainder function here:
def remainder(num1, num2):
  return (num1 * 2) % (num2 / 2)
# Uncomment these function calls to test your remainder function:
print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0



