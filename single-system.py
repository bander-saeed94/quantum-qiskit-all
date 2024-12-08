from numpy import array
from numpy import matmul

ket0 = array([1, 0])
ket1 = array([0, 1])

print(ket0 / 2 + ket1 / 2)

M1 = array([[1, 1], [0, 0]])
M2 = array([[1, 1], [1, 0]])

print(M1 / 2 + M2 / 2)


print(matmul(M1, ket1))
print(matmul(M1, M2))
print(matmul(M2, M1))