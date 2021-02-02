print(">>> age = 20")
age = 20
print()

print("conditional statement if age>=18 and age<21")
if age >=18 and age < 21:
  print('At least you can vote.')
  print('Poker will have to wait.')
print()

print("nested conditional if age>=18, then if age>=21")
if age >= 18:
  print('You can vote.')
  if age >= 21:
    print('You can play poker.')
