# NumPy Fundamentals — Task 3 Write-up
Question 1: Creating an Array and Printing Its Attributes

Aim
To create a NumPy array and display its shape, number of dimensions, size, and data type.

Code
import numpy as np
a = np.array([3, 6, 9, 12, 15])
print("Array:", a)
print("Shape:", a.shape)
print("Dimensions:", a.ndim)
print("Size:", a.size)
print("Data type:", a.dtype)

Output
text
Array: [ 3  6  9 12 15]
Shape: (5,)
Dimensions: 1
Size: 5
Data type: int64

Explanation
np.array() creates a NumPy array. 
The shape attribute gives the size along each dimension 
ndim gives the number of dimensions, 
size gives the total number of elements 
and dtype gives the element data type.

Question 2: Creating Arrays of Zeros, Ones, and a Fixed Value
Aim
To create arrays using NumPy's zeros(), ones(), and full() functions.

Code
import numpy as np
a = np.zeros((3, 2))
b = np.ones((2, 4), dtype=int)
c = np.full((2, 3), 7)
print("Zeros:\n", a)
print("Ones:\n", b)
print("Filled with 7:\n", c)

Output

Zeros:
 [[0. 0.]
  [0. 0.]
  [0. 0.]]
Ones:
 [[1 1 1 1]
  [1 1 1 1]]
Filled with 7:
 [[7 7 7]
  [7 7 7]]

Explanation
np.zeros() creates an array filled with zeros, 
np.ones() creates an array filled with ones, and 
np.full() fills an array of the specified shape with a chosen value. 
The dtype=int argument makes the ones array contain integers.


Question 3: Generating Random Arrays

Aim
To create arrays containing random floating-point numbers and random integers using NumPy.

Code
import numpy as np
rng = np.random.default_rng()
a = rng.random((3, 3))
b = rng.integers(0, 10, size=(2, 5))
c = np.random.randint(1, 101, size=(4, 4))
print("Random floats:\n", a)
print("Random integers from 0 to 9:\n", b)
print("Random integers from 1 to 100:\n", c)

Output
The arrays contain random values, so the exact output will vary each time the program runs. One possible output is:
Random floats:
Random floats:
 [[0.75465118 0.75911365 0.75058817]
 [0.75021123 0.27237918 0.02218198]
 [0.65078194 0.89724304 0.08154945]]
Random integers from 0 to 9:
 [[0 9 8 0 2]
 [5 6 6 7 5]]
Random integers from 1 to 100:
 [[ 62 100  39  19]
 [  4  95  17  65]
 [ 19  38   3  94]
 [ 56  24  34   4]]

Explanation
np.random.default_rng() creates a random-number generator. 
rng.random((3, 3)) creates a 3 × 3 array of random floats between 0 and 1. 
rng.integers(0, 10, size=(2, 5)) creates integers from 0 through 9. 
np.random.randint(1, 101, size=(4, 4)) creates integers from 1 through 100 because the upper bound is excluded.


Question 4: Comparing Memory Usage of int8 and int64

Aim
To create arrays with `int8` and `int64` data types and compare their memory usage.

Code
import numpy as np
a = np.arange(10, dtype=np.int8)
b = np.arange(10, dtype=np.int64)
print("int8 array:", a)
print("int8 nbytes:", a.nbytes)
print("int64 array:", b)
print("int64 nbytes:", b.nbytes)

Output
int8 array: [0 1 2 3 4 5 6 7 8 9]
int8 nbytes: 10
int64 array: [0 1 2 3 4 5 6 7 8 9]
int64 nbytes: 80

Explanation
np.arange(10) creates integers from 0 to 9. 
The dtype argument sets the data type. 
nbytes reports the memory occupied by the array's elements. 
Each int8 element uses 1 byte, while each int64 element uses 8 bytes.


Question 5: Accessing Rows and Columns

Aim
To access a particular row, column, last row, and last column using NumPy indexing.

Code
import numpy as np
a = np.arange(1, 36).reshape(5, 7)
print("Array:\n", a)
print("Third row:", a[2])
print("Fourth column:", a[:, 3])
print("Last row:", a[-1])
print("Last column:", a[:, -1])

Output
Array:
 [[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]
 [15 16 17 18 19 20 21]
 [22 23 24 25 26 27 28]
 [29 30 31 32 33 34 35]]
Third row: [15 16 17 18 19 20 21]
Fourth column: [ 4 11 18 25 32]
Last row: [29 30 31 32 33 34 35]
Last column: [ 7 14 21 28 35]

Explanation
np.arange(1, 36) creates values from 1 to 35, and reshape(5, 7) arranges them into five rows and seven columns. Python indexing starts at 0, so the third row has index 2 and the fourth column has index 3. -1 selects the last row or column. The colon : selects all entries along that axis.


Question 6: Slicing Elements and a 2 × 3 Block

Aim
To use NumPy slicing to select every second element of a row and a 2 × 3 block from an array.

Code
import numpy as np
a = np.arange(1, 36).reshape(5, 7)
print("Every second element of first row:", a[0, ::2])
print("2x3 block:\n", a[1:3, 2:5])

Output
Every second element of first row: [1 3 5 7]
2x3 block:
 [[10 11 12]
 [17 18 19]]

Explanation
a[0, ::2] selects the first row and takes every second element. 
In a[1:3, 2:5], rows with indices 1 and 2 and columns with indices 2, 3, and 4 are selected. The ending index in a slice is excluded.

Question 7: Indexing a Three-Dimensional Array
Aim
To access specific elements and a row in a three-dimensional NumPy array using positive and negative indices.

Code
import numpy as np
arr = np.arange(1, 13).reshape(2, 2, 3)
print("Array:\n", arr)
print("Element 6:", arr[0, 1, 2])
print("First row of second block:", arr[1, 0])
print("Last element:", arr[-1, -1, -1])

Output
Array:
 [[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
Element 6: 6
First row of second block: [7 8 9]
Last element: 12

Explanation
reshape(2, 2, 3) creates an array with two blocks, two rows per block, and three columns per row. The expression arr[0, 1, 2] accesses the value 6. arr[1, 0] selects the first row of the second block. Negative indices count from the end, so arr[-1, -1, -1] returns 12.


Question 8: Filtering Values Using Boolean Masks
Aim
To filter array elements using conditions for values greater than 10, even values, and values between 10 and 30 inclusive.

Code
import numpy as np
arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
print("Values greater than 10:", arr[arr > 10])
print("Even values:", arr[arr % 2 == 0])
print("Values from 10 to 30:", arr[(arr >= 10) & (arr <= 30)])

Output
Values greater than 10: [15 23 42 16 30]
Even values: [ 4  8 42 16 30]
Values from 10 to 30: [15 23 16 30]

Explanation
A Boolean mask is created by a condition such as arr > 10. Using the mask inside selects the values where the condition is true. arr % 2 == 0 identifies even values. The & operator combines the two range conditions, each condition is enclosed in parentheses.


Question 9: Finding Indices with `nonzero()` and `where()`
Aim
To find the indices of array elements greater than 15 using np.nonzero() and np.where().

Code
import numpy as np
arr = np.array([4, 15, 8, 23, 42, 16, 7, 30])
indices1 = np.nonzero(arr > 15)[0]
indices2 = np.where(arr > 15)[0]
print("Using nonzero:", indices1)
print("Using where:", indices2)

Output
Using nonzero: [3 4 5 7]
Using where: [3 4 5 7]

Explanation
arr > 15 creates a Boolean condition. np.nonzero() returns the indices of nonzero/true entries, while np.where() returns the indices where the condition is true when used with one argument. [0] extracts the index array for this one-dimensional input.

Question 10: Filtering Marks and Counting Students by Subject
Aim
To display marks of 60 or above and count the number of students scoring at least 40 in each subject.

Code
import numpy as np
marks = np.array([
    [45, 80, 67],
    [90, 55, 72],
    [38, 60, 85]
])
print("Marks greater than or equal to 60:")
print(marks[marks >= 60])
count = np.sum(marks >= 40, axis=0)
print("Students scoring 40 or more per subject:", count)

Output
Marks greater than or equal to 60:
[80 67 90 72 60 85]
Students scoring 40 or more per subject: [2 3 3]

Explanation
marks >= 60 creates a Boolean mask that selects marks of 60 or above. marks >= 40 creates a Boolean array in which qualifying marks are True. np.sum(..., axis=0) counts the `True` values column-wise, giving the number of students who scored at least 40 in each subject.

Question 11: Using `np.searchsorted()`
Aim
To find the insertion positions of values in a sorted NumPy array using `np.searchsorted()`.

Code
import numpy as np
s = np.array([2, 5, 8, 11, 14])
print(np.searchsorted(s, 9))
print(np.searchsorted(s, [1, 12, 5]))

Output
3
[0 4 1]

Explanation
np.searchsorted() returns the index at which a value can be inserted into a sorted array while maintaining its order. By default, it returns the position before an existing equal value. The function can accept a list of values in one call.

Question 12: Understanding a View and a Copy
Aim
To observe how changing a view affects the original array and how changing a copy leaves the original array unchanged.

Code
import numpy as np
a = np.arange(1, 9)
b = a[2:6]
b[0] = 99
print("After modifying the view:", a)
b = a[2:6].copy()
b[0] = 50
print("After modifying the copy:", a)

Output
After modifying the view: [ 1  2 99  4  5  6  7  8]
After modifying the copy: [ 1  2 99  4  5  6  7  8]

Explanation
Basic slicing such as a[2:6] usually returns a view that shares data with the original array. Therefore, changing b[0] also changes a[2]. Calling .copy() creates independent data, so modifying the copy does not affect a. The second operation starts with the already-modified original array.

Question 13: Comparing flatten() and ravel()
Aim
To compare `flatten()` and `ravel()` by modifying their results and observing the effect on the original array.
Code
import numpy as np
x = np.array([[1, 2, 3], [4, 5, 6]])
f = x.flatten()
r = x.ravel()
f[0] = 100
r[1] = 200
print("Original array:\n", x)
print("Flattened array:", f)
print("Raveled array:", r)

Output
Original array:
 [[  1 200   3]
 [  4   5   6]]
Flattened array: [100   2   3   4   5   6]
Raveled array: [  1 200   3   4   5   6]

Explanation
flatten() always returns a copy, so changing `f` does not affect `x`. `ravel()` returns a view when possible; in this example, `r` shares data with `x`, so changing r[1] changes the original array.


Question 14: Reshaping an Array
Aim
To reshape a one-dimensional array into different shapes and display the shape of each result.

Code
import numpy as np
a = np.arange(1, 13)
a1 = a.reshape(3, 4)
a2 = a.reshape(2, 6)
a3 = a.reshape(2, 3, 2)
a4 = a.reshape(4, -1)
print("Shape 1:", a1.shape)
print("Shape 2:", a2.shape)
print("Shape 3:", a3.shape)
print("Shape 4:", a4.shape)

Output
Shape 1: (3, 4)
Shape 2: (2, 6)
Shape 3: (2, 3, 2)
Shape 4: (4, 3)

Explanation
np.arange(1, 13) creates 12 elements. reshape() changes the dimensions without changing the number of elements. In reshape(4, -1), -1 tells NumPy to calculate the missing dimension automatically; 12 elements arranged in 4 rows require 3 columns.

Question 15: Creating Row and Column Vectors
Aim
To convert a one-dimensional array into row and column vectors using np.newaxis and np.expand_dims().

Code
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
row1 = a[np.newaxis, :]
col1 = a[:, np.newaxis]
row2 = np.expand_dims(a, axis=0)
col2 = np.expand_dims(a, axis=1)
print("Row using newaxis:\n", row1)
print("Column using newaxis:\n", col1)
print("Row using expand_dims:\n", row2)
print("Column using expand_dims:\n", col2)
print("Row shape:", row1.shape)
print("Column shape:", col1.shape)

Output
Row using newaxis:
 [[1 2 3 4 5 6]]
Column using newaxis:
 [[1]
  [2]
  [3]
  [4]
  [5]
  [6]]
Row using expand_dims:
 [[1 2 3 4 5 6]]
Column using expand_dims:
 [[1]
  [2]
  [3]
  [4]
  [5]
  [6]]
Row shape: (1, 6)
Column shape: (6, 1)

Explanation
np.newaxis and np.expand_dims() add a dimension to an array. axis=0 adds a dimension at the beginning, producing a row vector with shape (1, 6). axis=1 adds a dimension after the first axis, producing a column vector with shape (6, 1).


Question 16: Flipping a Two-Dimensional Array
Aim
To reverse a NumPy array along all axes, along rows, and along columns using `np.flip()`.
Code
import numpy as np
a = np.arange(1, 13).reshape(3, 4)
print("Original:\n", a)
print("Flip all axes:\n", np.flip(a))
print("Flip axis 0:\n", np.flip(a, axis=0))
print("Flip axis 1:\n", np.flip(a, axis=1))

Output
Original:
 [[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]
Flip all axes:
 [[12 11 10  9]
 [ 8  7  6  5]
 [ 4  3  2  1]]
Flip axis 0:
 [[ 9 10 11 12]
 [ 5  6  7  8]
 [ 1  2  3  4]]
Flip axis 1:
 [[ 4  3  2  1]
 [ 8  7  6  5]
 [12 11 10  9]]

Explanation
np.flip() reverses the order of elements along the specified axis. For a two-dimensional array, axis=0 reverses the rows, while axis=1 reverses the columns. Omitting axis reverses both dimensions.

Question 17: Stacking and Concatenating Arrays
Aim
To combine two arrays vertically and horizontally using vstack(), hstack(), and concatenate().

Code
import numpy as np
a1 = np.array([[1, 1], [2, 2]])
a2 = np.array([[3, 3], [4, 4]])
print("Vertical stack:\n", np.vstack((a1, a2)))
print("Horizontal stack:\n", np.hstack((a1, a2)))
print("Concatenate axis 1:\n", np.concatenate((a1, a2), axis=1))

Output
Vertical stack:
 [[1 1]
 [2 2]
 [3 3]
 [4 4]]
Horizontal stack:
 [[1 1 3 3]
 [2 2 4 4]]
Concatenate axis 1:
 [[1 1 3 3]
 [2 2 4 4]]

Explanation
np.vstack() stacks arrays vertically, increasing the number of rows. np.hstack() joins the two-dimensional arrays horizontally, increasing the number of columns. np.concatenate(..., axis=1) explicitly joins the arrays along the column axis, producing the same result as hstack() for these arrays.

Question 18: Splitting Arrays into Parts
Aim
To split a two-dimensional array into equal parts, split it at specified column positions, and divide a one-dimensional array into four parts.
Code
import numpy as np
x = np.arange(1, 25).reshape(2, 12)
parts1 = np.split(x, 3, axis=1)
print("Three equal parts:")
for part in parts1:
    print(part)
parts2 = np.split(x, [3, 4], axis=1)
print("Split at positions 3 and 4:")
for part in parts2:
    print(part)
parts3 = np.array_split(np.arange(1, 7), 4)
print("Four parts:", parts3)

Output
Three equal parts:
[[ 1  2  3  4]
 [13 14 15 16]]
[[ 5  6  7  8]
 [17 18 19 20]]
[[ 9 10 11 12]
 [21 22 23 24]]
Split at positions 3 and 4:
[[ 1  2  3]
 [13 14 15]]
[[ 4]
 [16]]
[[ 5  6  7  8  9 10 11 12]
 [17 18 19 20 21 22 23 24]]
Four parts: [array([1, 2]), array([3, 4]), array([5]), array([6])]

Explanation
np.split(x, 3, axis=1) divides the 12 columns into three equal sections. np.split(x, [3, 4], axis=1) uses the specified column boundaries, producing sections of widths 3, 1, and 8. np.array_split() allows sections to have unequal sizes, which is useful when the elements cannot be divided equally.


Question 19: Finding Unique Values, Counts, and First Indices
Aim
To find the unique values in an array, count their occurrences, and identify the first index of each value.
Code
import numpy as np
a = np.array([
    11, 11, 12, 13, 14, 15, 16, 17,
    12, 13, 11, 14, 18, 19, 20
])
values, first_indices, counts = np.unique(
    a,
    return_index=True,
    return_counts=True
)
print("Unique values:", values)
print("Counts:", counts)
print("First indices:", first_indices)

Output
Unique values: [11 12 13 14 15 16 17 18 19 20]
Counts: [3 2 2 2 1 1 1 1 1 1]
First indices: [ 0  2  3  4  5  6  7 12 13 14]

Explanation
np.unique() returns the distinct values in sorted order. return_counts=True returns the frequency of each unique value, while return_index=True returns the first position at which each value appears in the original array. The counts and indices correspond to the order of the unique values.

Question 20: Set Operations on NumPy Arrays
Aim
To perform union, intersection, difference, and symmetric difference operations on two arrays.
Code
import numpy as np
a = np.array([1, 2, 3, 4, 5])
b = np.array([4, 5, 6, 7])
print("Union:", np.union1d(a, b))
print("Intersection:", np.intersect1d(a, b))
print("Difference (a - b):", np.setdiff1d(a, b))
print("Symmetric difference:", np.setxor1d(a, b))

Output
Union: [1 2 3 4 5 6 7]
Intersection: [4 5]
Difference (a - b): [1 2 3]
Symmetric difference: [1 2 3 6 7]

Explanation
np.union1d() returns all unique values from both arrays. np.intersect1d() returns values common to both arrays. np.setdiff1d(a, b) returns values present in a but not in b. np.setxor1d() returns values present in either array but not in both. These functions return sorted unique results.


Question 21: Broadcasting Addition Across Rows and Columns

Aim
To use NumPy broadcasting to add a row vector to every row and a column vector to every column of a matrix.
Code
import numpy as np
m = np.arange(1, 10).reshape(3, 3)
row = np.array([10, 20, 30])
column = np.array([[100], [200], [300]])
print("Original matrix:\n", m)
print("Add row to every row:\n", m + row)
print("Add column to every column:\n", m + column)

Output
Original matrix:
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Add row to every row:
 [[11 22 33]
 [14 25 36]
 [17 28 39]]
Add column to every column:
 [[101 102 103]
 [204 205 206]
 [307 308 309]]

Explanation
Broadcasting allows arrays of compatible shapes to participate in element-wise operations. The row array has shape (3,), so its values are added to each row. The column array has shape (3, 1), so each value is added to every element in its corresponding row.


Question 22: Checking Broadcasting Compatibility
Aim
To test broadcasting for different array shapes and display the result shape or an error when the shapes are incompatible.
Code
import numpy as np
cases = [
    ((4, 3), (3,)),
    ((4, 3), (4,)),
    ((4, 3), (4, 1)),
    ((2, 3, 4), (3, 1))
]
for shape1, shape2 in cases:
    a = np.ones(shape1)
    b = np.ones(shape2)
    try:
        result = a + b
        print(shape1, "+", shape2, "=", result.shape)
    except ValueError as e:
        print(shape1, "+", shape2, "= Error:", e)

Output
(4, 3) + (3,) = (4, 3)
(4, 3) + (4,) = Error: operands could not be broadcast together with shapes (4,3) (4,) 
(4, 3) + (4, 1) = (4, 3)
(2, 3, 4) + (3, 1) = (2, 3, 4)

Explanation
np.ones() creates arrays filled with ones. The `try` block attempts to add each pair of arrays. If their shapes are incompatible, NumPy raises a `ValueError`, which is caught by the `except` block. Broadcasting compares dimensions from right to left; corresponding dimensions must be equal or one of them must be 1.

Question 23: Statistical Calculations and Aggregation
Aim
To calculate statistical measures for a random 3 x 4 array and find column sums, row maxima, and the index of the overall maximum.

Code
import numpy as np
rng = np.random.default_rng()
a = rng.random((3, 4))
print("Array:\n", a)
print("Sum:", np.sum(a))
print("Mean:", np.mean(a))
print("Minimum:", np.min(a))
print("Maximum:", np.max(a))
print("Standard deviation:", np.std(a))
print("Product:", np.prod(a))
print("Column sums:", np.sum(a, axis=0))
print("Row maxima:", np.max(a, axis=1))
print("Index of overall maximum:", np.argmax(a))

Output
Array:
 [[0.85501402 0.75422737 0.96390105 0.42502442]
 [0.47575295 0.30079898 0.50064716 0.6127692 ]
 [0.43686065 0.37886621 0.89971472 0.72044027]]
Sum: 7.324016984430051
Mean: 0.6103347487025043
Minimum: 0.3007989797364694
Maximum: 0.9639010456663217
Standard deviation: 0.21319376266121318
Product: 0.0012443426615955293
Column sums: [1.76762761 1.43389257 2.36426292 1.75823389]
Row maxima: [0.96390105 0.6127692  0.89971472]
Index of overall maximum: 2

Explanation
`np.sum()`, `np.mean()`, `np.min()`, `np.max()`, `np.std()`, and `np.prod()` calculate the sum, mean, minimum, maximum, standard deviation, and product of the array elements. `axis=0` calculates column sums, while `axis=1` calculates row maxima. `np.argmax()` returns the flattened index of the first occurrence of the maximum value.

Question 24: Element-wise Product, Matrix Product, and Determinant

Aim
To calculate the element-wise product and matrix product of two matrices and find the determinant of a matrix.

Code
import numpy as np
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("Element-wise product:\n", A * B)
print("Matrix product:\n", np.matmul(A, B))
print("Determinant of A:", np.linalg.det(A))

Output
Element-wise product:
 [[ 5 12]
 [21 32]]
Matrix product:
 [[19 22]
 [43 50]]
Determinant of A: -2.0000000000000004

Explanation
The * operator multiplies corresponding elements. np.matmul(A, B) performs matrix multiplication by taking dot products of rows of A and columns of B. np.linalg.det(A) calculates the determinant. For the matrix A, the determinant is (1 x 4) - (2 x 3) = -2.

Question 25: Calculating Mean Squared Error
Aim
To calculate the mean squared error between predicted values and actual labels using NumPy in one expression.
Code
import numpy as np
predictions = np.array([2.5, 0.0, 2.1, 7.8])
labels = np.array([3.0, -0.5, 2.0, 8.0])
mse = np.mean((predictions - labels) ** 2)
print("Mean Squared Error:", mse)

Output
Mean Squared Error: 0.1375

Explanation
Mean squared error (MSE) is the average of the squared differences between predictions and actual values. predictions - labels calculates the errors element-wise, ** 2 squares each error, and np.mean() calculates their average. MSE is commonly used to evaluate regression models.
