# display the current list of python keywords
import keyword
print(keyword.kwlist)
print()

# bad variable name
print('1st_number = 1')
print('What is the problem with the variable name above? Press enter to continue.')
enter = input()
print('Python variable names cannot start with a number')

# good variable name
print('first_number = 1')
print('What is the problem with the variable name above? Press enter to continue.')
enter = input()
print('All alpha characters are allowed')

# bad variable name
print('my_$ = 1000.00')
print('What is the problem with the variable name above? Press enter to continue.')
enter = input()
print('$ is not a special character allowed in Python variable names')

# good variable name
print('my_money = 1000.00')
print('What is the problem with the variable name above? Press enter to continue.')
enter = input()
print("_ is a valid character for Python variable")

# good variable name
print('_test = "value"')
print('What is the problem with the variable name above? Press enter to continue.')
enter = input()
print("_ is a valid character for Python variable and you can start a variable name using it")
