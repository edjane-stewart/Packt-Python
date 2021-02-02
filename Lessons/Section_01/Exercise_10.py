# String interpolation: command separators and format

# Comma separators
# Similart to concactenantion, but adds space between values
print(">>> italian_greeting = 'Ciao'")
italian_greeting = 'Ciao'

print(">>> print('Should we greet people with', italian_greeting, 'in North Beach?')")
print('Should we greet people with', italian_greeting, 'in North Beach?')
print()

# Format
# Converts Python types (int, float) into strings
# 1. define variables
# 2. Use {} in string as placeholder for each variable
# 3. At end of string add . followed by format and list variables
print(">>> owner = 'Lawrence Ferlinghetti'")
owner = 'Lawrence Ferlinghetti'
print(">>> age = 100")
age = 100
print(">>> print('The founder of City Lights Bookstore, {}, is now {} years old.'.format(owner, age))")
print('The founder of City Lights Bookstore, {}, is now {} years old.'.format(owner, age))
print()

# len() function
print('>>> arabic_greeting = \'Ahlan wa sahlan.\'')
arabic_greeting = 'Ahlan wa sahlan.'
print(">>> len(arabic_greeting)")
print(len(arabic_greeting))
print()

print(">>> name = 'Corey'")
name = 'Corey'

print(">>> name.lower()")
print(name.lower())

print(">>> name.capitalize()")
print(name.capitalize())

print(">>> name.upper()")
print(name.upper())

print(">>> name.count('o')")
print(name.count('o'))
