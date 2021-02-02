print(">>> age = 20")
age = 20

print()
print("if... else checking for age less than 18")
if age < 18:
  print('You aren\'t old enough to vote.')
else:
  print('Welcome to our voting program.')
print()

print('if... else checking for age greater or equal to 18')
if age >= 18:
  print('Welcome to our voting program.')
else:
  print('You aren\'t old enough to vote.')
print()

# elif statement
print('elif')
if age <= 10:
  print('Listen, learn, and have fun.')
elif age<= 19:
  print('Go fearlessly forward.')
elif age <= 29:
  print('Seize the day.')
elif age <= 39:
  print('Go for what you want.')
elif age <= 59:
  print('Stay physically fit and healthy.')
else:
  print('Each day is magical.')
print()

# while look
print('while loop')
i = 1
while i <= 10:
  print(i)
  i += 1
print()

# break
# Find first number greater than 100 and divisible by 17.
x = 100
while x >= 100:
  x += 1
  if x % 17 == 0:
    print('', x, 'is the first number greater than 100 that is divisible by 17.')
    break
