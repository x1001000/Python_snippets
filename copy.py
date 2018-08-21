x = 'python'
y = x     # y is a copy of x (call by value)
x = 1001000
print(x, y)
############################################
x = [['python']]
y = x           # y is x (call by reference)
x[0][0] = 1001000
print(x, y)
############################################
import copy
############################################
x = [['python']]
y = copy.copy(x)  # y is a shallow copy of x
x[0][0] = 1001000
print(x, y)
############################################
x = [['python']]
y = copy.deepcopy(x) # y is a deep copy of x
x[0][0] = 1001000
print(x, y)
