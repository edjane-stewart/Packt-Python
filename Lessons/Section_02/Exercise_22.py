print('>>> m = [[1, 2, 3], [4, 5, 6]]')
m = [[1, 2, 3], [4, 5, 6]]
print('>>> print(m[1][1])')
print(m[1][1])
print("loop through the matrix using range")
for i in range(len(m)):
  for j in range(len(m[i])):
    print(m[i][j])
print("loop through the matrix using in")
for row in m:
  for col in row:
    print(col)