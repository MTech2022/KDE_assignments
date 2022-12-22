import numpy as np
from numpy import linalg as LA
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~START~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("i. Create multi-dimensional arrays and find its shape and dimension\n---------------------------------------------------");
A = np.array([
        [18, 19, 20],
        [21, 22, 23],
        [21, 22, 23],
        [24, 25, 26]], dtype='float')

m, n = A.shape
print (f"Shape of array is {m} x {n}")
print("---------------------------------------------------");
A = np.array([1, 2, 3])
x = A.ndim
print("Example 1 :  Below is the array");
print(A)
print(f"Number of array dimensions is {x}");

A = np.zeros((2, 3, 3))
y = A.ndim

print("\nExample 2 :  Below is the array");
print(A)
print(f"Number of array dimensions is {y}");

print("\n\nii. Create a matrix full of zeros and ones\n---------------------------------------------------");
A = np.zeros((3, 3),  dtype=int)
print("\nExample 1 :  Below is the array of zeros");
print(A)
print("---------------------------------------------------");

A = np.ones((3, 3),  dtype=int)
print("\nExample 1 :  Below is the array of ones");
print(A)
print("---------------------------------------------------");


print("\n\niii. Reshape and flatten data in the array\n--------------------------------------");
A = np.arange(9).reshape((3, 3))
print(A)
z = A.flatten();
print(f"\nAbove array is flatten................... as {z}");

print("\n\niv. Append data vertically and horizontally\n---------------------------------------------------");
A = np.append([1, 2, 3], [[4, 5, 6], [7, 8, 9]])
print(A);

print("---------------------------------------------------");
A = np.append([[1, 1, 1], [2, 2, 2]], [[3, 3, 3]], axis=0)
print(f"{A}");

print("\n\nv. Apply indexing and slicing on array\n---------------------------------------------------")
# Slicing in Python refers to extracting a subset or specific part of the
# sequence list, tuple, or string in a specific range.
# While indexing refers to accessing a single element from an array, it is used to get slices of arrays.
A = np.array([
        [18, 19, 20],
        [21, 22, 23],
        [24, 25, 26]], dtype='int')
print("Example 1 : -----------------------slice(0,1,1)----------------------------");
s = slice(0,1,1)
print(A[s])
print("\nExample 2 : ----------------------slice(0,2,1)-----------------------------");
#s = slice(0,2,1) below is equal
B = A[0:2:1]
print(B)

print("\n\nvi. Dot and matrix product of two arrays\n---------------------------------------------------");
arr1 = [[1, 1],
     [1, 1]]
arr2 = [[4, 1],
     [2, 2]]
A = np.dot(arr1, arr2);
print(f"Matrix Dot of \n{arr1} x \n{arr2} is =")
print(A);

print("\n|-------------------Multiplication matrix--------------------------------")
arr1 = np.array([[1, 2, 3], [4, 5, 6],[7, 8, 9]])
arr2 = np.array([[11, 12, 13], [14, 15, 16],[17, 18, 19]])
matrix_product = np.matmul(arr1, arr2)
print(f"Matrix Product of \n{arr1} x \n{arr2} is =")
print("------------------")
print(matrix_product)
print("------------------")
print()
arr1 = np.array([[2,2],[3,3]])
arr2 = np.array([[1,2,3],[4,5,6]])
matrix_product = np.matmul(arr1, arr2)
print(f"Matrix Product of \n{arr1} x \n{arr2} is =")
print("------------------")
print(matrix_product)
print("------------------")
print()
arr1 = np.array([[100,200],[300,400]])
arr2 = np.array([[1,2],[4,6]])
matrix_product = np.matmul(arr1, arr2)
print(f"Matrix Product of \n{arr1} x \n{arr2} is =")
print("------------------")
print(matrix_product)

print("\n\nvii. Compute the Eigen values of a matrix\n---------------------------------------------------")
print("Example 1-------------------")
A = np.array([[1, 2], [4, 5]])
eigvals = LA.eigvals(A)
print("Input pmatrix : \n",A)
print("Eigen value \n",eigvals)
print("Example 2-------------------")
A = np.array([[1, 0], [0, 1]])
print("Input pmatrix : \n",A)
eigvals = LA.eigvals(A)
print("Eigen value \n",eigvals)

print("\n\nviii. Compute the multiplicative inverse of a matrix\n---------------------------------------------------")
A = np.array([[1, 2], [3, 4]])
ainv = LA.inv(A)
print("Input pmatrix : \n",A)
print("Inverse : \n", ainv)

print("\n\nix. Compute the rank of a matrix\n---------------------------------------------------")
A = np.array([[1, 2], [3, 4]])
rank = LA.matrix_rank(A)
print("Input pmatrix : \n", A)
print("Rank : " , rank)

print("\n\nx. Compute the length of a vector\n---------------------------------------------------")
A = np.array([[ 1, 2, 3],
          [-1, 1, 4]])
vectorLength = LA.norm(A)
print("Input pmatrix : \n", A)
print("length of a vector : " , vectorLength)

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~END~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")