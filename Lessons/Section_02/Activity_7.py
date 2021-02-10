# create a list named employees
employees = [ {"name":"John Mckee", "age":38, "department":"Sales"}, {"name":"Lisa Crawford", "age":29, "department":"HR"}, {"name":"Sujan Patel", "age":33, "department":"HR"} ]
print(employees)
for employee in employees:
  print("Name:",employee['name'])
  print("Age:", employee['age'])
  print("Department:", employee['department'])
  print("-"*20)
print()
print("Name:",employees[2]['name'])
print("Age:", employees[2]['age'])
print("Department:", employees[2]['department'])