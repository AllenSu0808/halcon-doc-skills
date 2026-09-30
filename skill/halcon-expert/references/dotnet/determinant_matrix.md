# DeterminantMatrix (Operator)

## Name

`DeterminantMatrix` — Compute the determinant of a matrix.

## Signature

`static void HOperatorSet.DeterminantMatrix(HTuple matrixID, HTuple matrixType, out HTuple value)`

`double HMatrix.DeterminantMatrix(string matrixType)`

## Description

The operator `DeterminantMatrix` computes the determinant of
the input `Matrix` given by the matrix handle
*`matrixID`*. The type of the input `Matrix` can be
selected via the parameter *`matrixType`*. The following
values are supported: *"general"* for general,
*"symmetric"* for symmetric, *"positive_definite"* for
symmetric positive definite, *"tridiagonal"* for tridiagonal,
*"upper_triangular"* for upper triangular,
*"permuted_upper_triangular"* for permuted upper triangular,
*"lower_triangular"* for lower triangular, and
*"permuted_lower_triangular"* for permuted lower triangular
matrices. The formula for the calculation of the result
is:
$$\texttt{Value}=\det \texttt{Matrix}.$$

*Example:*

$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & 2.0 \\ -5.0 & 7.0 & 2.0 \\ -9.0 & -4.0 & 1.0 \end{bmatrix} \Rightarrow \text{Value} = -134.0$$ ![figure](../assets/5b747120c26f540c.svg)

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

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`matrixType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

The type of the input matrix.

Default:
"general"

List of values:
"general", "lower_triangular", "permuted_lower_triangular", "permuted_upper_triangular", "positive_definite", "symmetric", "tridiagonal", "upper_triangular"

**`value`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Determinant of the input matrix.

## Result

If the parameters are valid, the operator `DeterminantMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
