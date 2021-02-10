# Addition
# Create two nested lists, X and Y, to store the values
X = [[1,2,3],[4,5,6],[7,8,9]]
Y = [[10,11,12],[13,14,15],[16,17,18]]

# Initialize a 3 x 3 zero matrix called result as a placeholder
result = [[0,0,0], [0,0,0], [0,0,0]] 

# Implement the algorithm by iterating through the cells and columns
# iterate through rows
for i in range(len(X)):  
# iterate through columns 
  for j in range(len(X[0])): 
    result[i][j] = X[i][j] + Y[i][j] 
    
print(result)

# Subtraction
X = [[10,11,12],[13,14,15],[16,17,18]]
Y = [[1,2,3],[4,5,6],[7,8,9]]

# Initialize a result placeholder
result = [[0,0,0], [0,0,0], [0,0,0]] 

# iterate through rows 
for i in range(len(X)):  
# iterate through columns 
  for j in range(len(X[0])): 
    result[i][j] = X[i][j] - Y[i][j] 
    
print(result)