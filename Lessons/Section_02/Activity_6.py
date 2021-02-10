# Create a list and assign it to employees
employees = []
# Create three nested lists in employees to store the information of each employee, respectively
employees.append(["John McKee", 38, "Sales"]) # employee 1
employees.append(["Lisa Crawford", 29, "Marketing"]) # employee 2
employees.append(["Sujan Patel", 33, "HR"]) # employee 3
# Print the employees variable
print(employees)
print()
# Print the details of all employees in a presentable format
for employee in employees:
  print("Name:", employee[0])
  print("Age:", employee[1])
  print("Department:", employee[2])
  print("-"*25)
print()
# Print only the details of Lisa Crawford
print("Name:", employees[1][0])
print("Age:", employees[1][1])
print("Department:", employees[1][2])