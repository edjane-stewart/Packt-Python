# create two lists
items = ['apple', 'orange', 'banana']
quantity = [5,3,2]

# use the zip() function to combine both lists
orders = zip(items,quantity)
print(orders)

# turn the zip object into a list
orders = zip(items,quantity)
print(list(orders))

# turn the zip object into a tuple
orders = zip(items,quantity)
print(tuple(orders))

# turn the zip object into a dictionary
orders = zip(items,quantity)
print(dict(orders))