import math
nums = [-3, -5, 1, 4] 
logisT = list(map(lambda x: 1 / (1 + math.exp(-x)), nums))
print(logisT)
