# InvertMatrixMod (Operator)

## Name

`InvertMatrixMod` — Invert a matrix.

## Signature

`static void HOperatorSet.InvertMatrixMod(HTuple matrixID, HTuple matrixType, HTuple epsilon)`

`void HMatrix.InvertMatrixMod(string matrixType, double epsilon)`

## Description

The operator `InvertMatrixMod` computes the inverse of the
`Matrix` defined by the matrix handle *`matrixID`*.
The input matrix is overwritten with the result. Access to the
elements of the matrix is possible e.g., with the operator
[`GetFullMatrix`](get_full_matrix.md).

For *`epsilon`* = 0, the inverse is computed. The type of the
`Matrix` can be selected via *`matrixType`*. The
following values are supported: *"general"* for general,
*"symmetric"* for symmetric, *"positive_definite"* for
symmetric positive definite, *"tridiagonal"* for tridiagonal,
*"upper_triangular"* for upper triangular,
*"permuted_upper_triangular"* for permuted upper triangular,
*"lower_triangular"* for lower triangular, and
*"permuted_lower_triangular"* for permuted lower triangular
matrices.

*Example 1:*

*`matrixType`* = *"general"*,
*`epsilon`* = *0*
$$Matrix = \begin{bmatrix} 1.0 & 3.0 & 3.0 \\ 4.0 & 5.0 & 6.0 \\ 5.0 & 5.0 & 7.0 \\end{bmatrix}$$ ![figure](../assets/71e0ded32f75d48a.svg)
$$\Rightarrow \text{Matrix} = \begin{bmatrix}-1.25 & 1.50 & -0.75\\-0.50 & 2.00 & -1.50\\1.25 & -2.50 & 1.75\end{bmatrix}$$ ![figure](../assets/ccc362fac3406816.svg)

*Example 2:*

*`matrixType`* = *"upper_triangular"*,
*`epsilon`* = *0*
$$\mathrm{Matrix} = \begin{bmatrix}1.0 & 3.0 & 3.0 \\ 0 & 2.0 & 6.0 \\ 0 & 0 & 10.0\end{bmatrix}$$ ![figure](../assets/ab139fb3ca8fc327.svg)
$$\rightarrow \text{ Matrix }=\left[\begin{array}{ccc}1.00 & -1.50 & 0.60\\0 & 0.50 & -0.30\\0 & 0 & 0.10\end{array}\right]$$ ![figure](../assets/98dbe16ca0193077.svg)

*Example 3:*

*`matrixType`* = *"permuted_upper_triangular"*,
*`epsilon`* = *0*
$$\text{Matrix} = \begin{bmatrix} 1.0 & 3.0 & 3.0 \\ 0 & 0 & 10.0 \\ 0 & 2.0 & 6.0 \end{bmatrix}$$ ![figure](../assets/f08d7f32a295b408.svg)
$$\rightarrow \text{ Matrix }=\left[\begin{array}{ccc}1.00 & -1.50 & 0.60\\0 & 0.50 & -0.30\\0 & 0 & 0.10\end{array}\right]$$ ![figure](../assets/98dbe16ca0193077.svg)

For *`epsilon`* > 0, the pseudo inverse is computed using a
singular value decomposition (SVD). During the computation, all
singular values less than the value *`epsilon`* $\times$
the largest singular value are set to 0. For these values no
internal division is done to prevent a division by zero. If a
square matrix is computed with the SVD algorithm the computation
takes more time. The type of the matrix must be set to
*`matrixType`* = *"general"*.

*Example:*

*`matrixType`* = *"general"*,
*`epsilon`* = *2.2204e-16*
$$\text{Matrix = }\begin{bmatrix}3.0 & 1.0 & -2.0 & 5.0\\-5.0 & 7.0 & 2.0 & -6.0\\-9.0 & -4.0 & 1.0 & 4.0\end{bmatrix}$$ ![figure](../assets/13a09935c002ac36.svg)
$$\rightarrow Matrix = \begin{bmatrix}-0.0021 & -0.0482 & -0.0813\\ 0.1435 & 0.1137 & -0.0137\\ -0.0519 & -0.0015 & 0.0028\\ 0.1518 & 0.0056 & 0.0526\end{bmatrix}$$ ![figure](../assets/bee011e11cee429e.svg)

Note: The relative accuracy of the floating point representation of
the used data type (double) is *`epsilon`* = 2.2204e-16.

It should be also noted that in the examples there are differences
in the meaning of the numbers of the output matrices: The results
of the elements are per definition a certain value if the number of
this value is shown as an integer number, e.g., 0 or 1. If the
number is shown as a floating point number, e.g., 0.0 or 1.0, the
value is computed.

## Attention

For *`matrixType`* = *"symmetric"*,
*"positive_definite"*, or *"upper_triangular"* the
upper triangular part of the input `Matrix` must contain
the relevant information of the matrix. The strictly lower
triangular part of the matrix is not referenced. For
*`matrixType`* = *"lower_triangular"* the lower
triangular part of the input `Matrix` must contain the
relevant information of the matrix. The strictly upper triangular
part of the matrix is not referenced. For *`matrixType`* =
*"tridiagonal"*, only the main diagonal, the superdiagonal,
and the subdiagonal of the input `Matrix` are used. The
other parts of the matrix are not referenced. If the referenced
part of the input `Matrix` is not of the specified type,
an exception is raised.

`InvertMatrixMod` modifies the content of an already
existing matrix.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrixID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrixID`** (input_control, state is modified)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`matrixType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The type of the input matrix.

Default:
"general"

List of values:
"general", "lower_triangular", "permuted_lower_triangular", "permuted_upper_triangular", "positive_definite", "symmetric", "tridiagonal", "upper_triangular"

**`epsilon`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Type of inversion.

Default:
0.0

Suggested values:
0.0, 2.2204e-16

## Result

If the parameters are valid, the operator `InvertMatrixMod`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`InvertMatrix`

## See also

`TransposeMatrix`,
`TransposeMatrixMod`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
