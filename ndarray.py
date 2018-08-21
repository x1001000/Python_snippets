import numpy

x = [
    [ [ [10,20,30], [0,0,0] ],[ [0,0,0], [0,0,0] ] ],
    [ [ [0,0,0], [0,0,0] ],[ [0,0,0], [0,0,0] ] ]
    ]
print(type(x))
print(len(x),len(x[0]),len(x[0][0]),len(x[0][0][0]))

# ndarray == tensor

y = numpy.array(x, numpy.int8)
print(type(y))
print(y.shape)
