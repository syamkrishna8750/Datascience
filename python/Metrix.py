import numpy as np

print("Enter elements of Matrix A (3x3):")
A = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    A.append(row)

print("\nEnter elements of Matrix B (3x3):")
B = []
for i in range(3):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    B.append(row)

A = np.matrix(A)
B = np.matrix(B)

print("\nMatrix A:\n", A)
print("Matrix B:\n", B)

print("\nA + B =\n", A + B)
print("A - B =\n", A - B)
print("A × B =\n", np.matmul(A, B))
print("2 × A =\n", 2 * A)
print("Transpose of A =\n", A.T)
