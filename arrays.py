import numpy as np
A = np.array([[1, 1, -1], [2, -4, 1], [4, -3, 6]])

mat = np.linalg.det(A)

if mat !=0:
    A_mat = np.linalg.inv(A)
else:
    A_mat = None

b = np.array([[-2, 4], [1, 7], [-4, 3]])

b_trans = b.T

c = np.array([4,3,-2])

d = np.array([5,-2,1])

print("а)1", 2*c + 5*d)
print("а)2", c-3*d)
print("b",b_trans )
print("d",mat, A_mat)
# Отлично
