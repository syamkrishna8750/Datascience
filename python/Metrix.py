import numpy as np

A = np.matrix([[1, 2, 3], [1, 1, 1], [1, 1, 1]])
B = np.matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Perform operations
print("\nA + B =\n", A + B)
print("A - B =\n", A - B)
print("A × B =\n", np.matmul(A, B))
print("2 × A =\n", 2 * A)
print("Transpose of A =\n", A.T)