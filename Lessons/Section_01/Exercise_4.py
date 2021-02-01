# display the current list of python keywords
import keyword
print('>>> import keyword')
print(keyword.kwlist)
print()

# bad variable name
print('1st_number = 1')
enter = input('What is the problem with the variable name above? Press enter to continue.' )
print('Python variable names cannot start with a number.')
print()

# good variable name
print('first_number = 1')
enter = input('What is the problem with the variable name above? Press enter to continue. ')
print('Nothing. All alpha characters are allowed')
print()

# bad variable name
print('my_$ = 1000.00')
enter = input('What is the problem with the variable name above? Press enter to continue. ')
print('$ is not a special character allowed in Python variable names')
print()

# good variable name
print('my_money = 1000.00')
enter = input('What is the problem with the variable name above? Press enter to continue. ')
print("Nothing. _ is a valid character for Python variable.")
print()

# good variable name
print('_test = "value"')
enter = input('What is the problem with the variable name above? Press enter to continue. ')
print("Nothing. _ is a valid character for Python variable and you can start a variable name using it")
