# Evaluating value of 12+3
eval('12 + 3')

print('Enter a number to see if it\'s a perfect square.')
number = input()
number =  eval(number)

i = -1
square = False

while number >= 0 and number%1 == 0 and i <= number**(0.5):
  i += 1
  if i*i == number: 
    square = True
    break

if square:
    print('The square root of', number, 'is', i, '.')
else:
    print('', number, 'is not a perfect square.')
