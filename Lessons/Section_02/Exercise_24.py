# Create two nested lists, X and Y
X = [[1, 2], [4, 5], [3, 6]]
Y = [[1,2,3,4],[5,6,7,8]]

# Create a zero-matrix placeholder to store the result
result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]] 

# Implement the matrix multiplication algorithm to compute the result
# iterating by row of X 
for i in range(len(X)): 
 
  # iterating by column by Y 
  for j in range(len(Y[0])): 
 
    # iterating by rows of Y
    for k in range(len(Y)): 
      result[i][j] += X[i][k] * Y[k][j] 

for r in result: 
  print(r)
