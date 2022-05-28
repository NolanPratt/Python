
from datetime import date


# defines a class to call the bold attribute from
class Props:
    Bold = '\033[1m'
    End = '\033[0m'


# calling today's date through the datetime import
date_call = date.today()
today = str(date_call)
year = int(today[0:4])

# Prompt the user for name
name = input("What is your name? ")
print(Props.Bold + str(name) + Props.End)

# Prompt the user for age
age = int(input("How old are you? "))
print(Props.Bold + str(age) + Props.End)

# Calculating user's age using today's date from datetime import
calc_age = year - age
# Print Name and Age in required format
print('Hello {a}! You were born in {b}.'.format(a=name, b=calc_age))
