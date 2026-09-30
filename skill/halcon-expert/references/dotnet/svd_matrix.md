# SvdMatrix (Operator)

## Name

`SvdMatrix` — Compute the singular value decomposition of a matrix.

## Signature

`static void HOperatorSet.SvdMatrix(HTuple matrixID, HTuple SVDType, HTuple computeSingularVectors, out HTuple matrixUID, out HTuple matrixSID, out HTuple matrixVID)`

`HMatrix HMatrix.SvdMatrix(string SVDType, string computeSingularVectors, out HMatrix matrixSID, out HMatrix matrixVID)`

## Description

The operator `SvdMatrix` computes a full or reduced singular
value decomposition (SVD) of the `Matrix` defined by the
matrix handle *`matrixID`*. The operator returns the matrix
handle *`matrixSID`* of the matrix `MatrixS` with
singular values in descending order.
Optionally, the matrices `MatrixU` with the left and
`MatrixV` with the right singular vectors are computed and
the matrix handles *`matrixUID`* and *`matrixVID`* are
returned. Access to the elements of the matrices is possible e.g.,
with the operator [`GetFullMatrix`](get_full_matrix.md). The SVD is written

$$\texttt{Matrix}=\texttt{MatrixU}\cdot\texttt{MatrixS}\cdot\texttt{MatrixV}^{T}.$$

For *`SVDType`* = *"full"*, a full SVD is computed.

*Example:*

*`SVDType`* = *"full"*,
*`computeSingularVectors`* = *"both"*
$$\mathbf{Matrix} = \begin{bmatrix} 6.0 & -5.0 \\ 10.0 & 4.0 \\ -3.0 & 5.0 \end{bmatrix}$$ ![figure](../assets/d6464090e63c3be6.svg)
$$\rightarrow \\text{MatrixU} = \\begin{bmatrix}-0.5228 & 0.5691 & 0.6346\\-0.8070 & -0.5702 & -0.1535\\0.2745 & -0.5924 & 0.7574\\\\end{bmatrix}\n\\text{MatrixS} = \\begin{bmatrix}12.0547 & 0 \\0 & 8.1046 \\0 & 0\\end{bmatrix}\n\\text{MatrixV} = \\begin{bmatrix}-0.9980 & -0.0629 \\0.0629 & -0.9980\\end{bmatrix}$$ ![figure](../assets/b9b758c61e002ab1.svg)

For *`SVDType`* = *"reduced"*, a reduced SVD is
computed.

*Example:*

*`SVDType`* = *"reduced"*,
*`computeSingularVectors`* = *"both"*
$$\mathbf{Matrix} = \begin{bmatrix} 6.0 & -5.0 \\ 10.0 & 4.0 \\ -3.0 & 5.0 \end{bmatrix}$$ ![figure](../assets/d6464090e63c3be6.svg)
$$\text{MatrixU} = \begin{bmatrix}-0.5228 & 0.5691 \\ -0.8070 & -0.5702 \\ 0.2745 & -0.5924\end{bmatrix}\\[6pt] \text{MatrixS} = \begin{bmatrix}12.0547 & 0 \\ 0 & 8.1046\end{bmatrix}\\[6pt] \text{MatrixV} = \begin{bmatrix}-0.9980 & -0.0629 \\ 0.0629 & -0.9980\end{bmatrix}$$ ![figure](../assets/57c4fad909ed17b0.svg)

For *`computeSingularVectors`* = *"left"*, the matrix
`MatrixU` with the left singular vectors is computed. For
*`computeSingularVectors`* = *"right"*, the matrix
`MatrixV` with the right singular vectors is computed. For
*`computeSingularVectors`* = *"both"*, the matrices
`MatrixU` and `MatrixV` with the left and right
singular vectors are computed.

For *`computeSingularVectors`* = *"none"*, no matrices
with the singular vectors are computed. The matrix
`MatrixS` is a matrix with n rows and one column, where
the number n = min(number of rows of the input `Matrix`,
number of columns of the input `Matrix`).

*Example:*

*`SVDType`* = *"reduced"* or *"full"*,
*`computeSingularVectors`* = *"none"*
$$\mathbf{Matrix} = \begin{bmatrix} 6.0 & -5.0 \\ 10.0 & 4.0 \\ -3.0 & 5.0 \end{bmatrix}$$ ![figure](../assets/d6464090e63c3be6.svg)
$$\Rightarrow \mathrm{Matrices} = \begin{bmatrix} 12.0547 \\ 8.1046 \end{bmatrix}$$ ![figure](../assets/f5144528ee7547ea.svg)

It should be noted that in the examples there are differences in the
meaning of the values of the output matrices: If a value is shown as
an integer number, e.g., 0 or 1, the value of this element is per
definition this certain value. If the number is shown as a floating
point number, e.g., 0.0 or 1.0, the value is computed by the
operator.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`SVDType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of computation.

Default:
"full"

List of values:
"full", "reduced"

**`computeSingularVectors`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Computation of singular values.

Default:
"both"

List of values:
"both", "left", "none", "right"

**`matrixUID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the left singular vectors.

**`matrixSID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with singular values.

**`matrixVID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the right singular vectors.

## Result

If the parameters are valid, the operator `SvdMatrix` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
