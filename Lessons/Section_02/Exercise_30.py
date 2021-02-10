# dictionary methods
# create dictionary
orders = {'apple':5, 'orange':3, 'banana':2}
#print dictionary values
print(orders.values())
print(list(orders.values()))
# print dictionary keys
print(list(orders.keys()))
# convert dictionary items to tuples
for tuple in list(orders.items()):
  print(tuple)