def sum_of_numbers(*args):
    total = 0
    for number in args:
        total += number
    return total
print(sum_of_numbers(1,3,2,5,4))

def person_details(**kwargs):
    print("Personal Details")
    for key, value in kwargs.items():
        print("{} : {}".format(key,value))

person_details(firstName = "Jason", lastName = "Scott", country = "US")
print()
person_details(name = "Ratan", country = "India", age = 23)
print()
input_dict = {'name' : 'Vikas Singh' , 'gender' : 'Male'}
person_details(**input_dict)
