def get_second_element(mylist):
    if len(mylist) > 1:
        return mylist[1]
    else:
        return 'List was too small'

o = get_second_element([1, 2, 3])
print(o)
o = get_second_element([1])
print(o)