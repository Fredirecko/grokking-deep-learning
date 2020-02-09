import numpy as np

aVector = np.array([0, 1, 2, 3, 4]) # A vector
bVector = np.array([5, 6, 7, 8, 9]) # Another vector
aMatrix = np.array([[0, 1, 2, 3, 4],[5, 6, 7, 8, 9]]) # A matrix

d = np.zeros((2,4)) # This creates a 2 x 4 matrix of zeros. Rows come first, then comlumns.
e = np.random.rand(2, 5) #This creates a random 2 x 5 matrix of numbers between 0 and 1

f = np.zeros((1,4))
g = np.zeros((4,3))

h = f.dot(g)


print("-----------------")
print(h.shape)
print("-----------------")
print(aVector)
print("-----------------")
print(bVector)
print("-----------------")
print(aMatrix)
print("-----------------")
print(d)
print("-----------------")
print(e)
print("-----------------")
print(aVector * 0.1)
print("-----------------")
print(aMatrix * 0.2)
print("-----------------")
print(aVector * bVector)
print("-----------------")
print(aVector * bVector * 0.2)
print("-----------------")
print(aVector * aMatrix)
print("-----------------")
print("-----------------")
