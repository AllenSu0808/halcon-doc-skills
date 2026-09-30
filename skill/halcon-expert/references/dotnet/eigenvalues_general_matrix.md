# EigenvaluesGeneralMatrix (Operator)

## Name

`EigenvaluesGeneralMatrix` — Compute the eigenvalues and optionally the eigenvectors of a general
matrix.

## Signature

`static void HOperatorSet.EigenvaluesGeneralMatrix(HTuple matrixID, HTuple computeEigenvectors, out HTuple eigenvaluesRealID, out HTuple eigenvaluesImagID, out HTuple eigenvectorsRealID, out HTuple eigenvectorsImagID)`

`void HMatrix.EigenvaluesGeneralMatrix(string computeEigenvectors, out HMatrix eigenvaluesRealID, out HMatrix eigenvaluesImagID, out HMatrix eigenvectorsRealID, out HMatrix eigenvectorsImagID)`

## Description

The operator `EigenvaluesGeneralMatrix` computes all
eigenvalues and, optionally, the left or right eigenvectors of a
square, general `Matrix`. The matrix is defined by the
matrix handle *`matrixID`*. The computed eigenvectors have the
norm 1.

The operator generates the new matrices `EigenvaluesReal`
and `EigenvaluesImag` with the real and the imaginary parts
of the computed eigenvalues. Each matrix has one column and n
rows, where n is the number of rows of the input `Matrix`.
In contrast to the operator [`EigenvaluesSymmetricMatrix`](eigenvalues_symmetric_matrix.md),
the order of the eigenvalues is not defined.
The operator returns the matrix handles *`eigenvaluesRealID`*
and *`eigenvaluesImagID`*. If desired, the real and imaginary
parts of the computed eigenvectors are stored in the new matrices
`EigenvectorsReal` and `EigenvectorsImag`. For
this, the operator returns valid matrix handles
*`eigenvectorsRealID`* and *`eigenvectorsImagID`*.
Access to the elements of the matrix is possible e.g., with the
operator [`GetFullMatrix`](get_full_matrix.md).

The computation type of eigenvectors can be selected via the
parameter *`computeEigenvectors`*. If
*`computeEigenvectors`* = *"none"*, no eigenvectors are
computed. If *"left"* is selected, the left eigenvalues are
computed. If *"right"* is selected, the right eigenvalues are
computed.

*Example:*

*`computeEigenvectors`* = *"right"*
$$\text{Matrix}=\left[\begin{array}{ccc}6.0 & 4.0 & -8.0\\5.0 & 7.0 & 3.0\\4.0 & -1.0 & 4.0\end{array}\right]$$ ![figure](../assets/3cb2dee0a30853f3.svg)
$$\rightarrow EigenvaluesReal = \begin{bmatrix} 3.3110 \\ 3.3110 \\ 10.3781 \end{bmatrix} EigenvaluesImag = \begin{bmatrix} 5.4143 \\ -5.4143 \\ 0.0 \end{bmatrix} EigenvectorsReal = \begin{bmatrix} 0.6353 & 0.6353 & 0.4813 \\ -0.4764 & -0.4764 & 0.8605 \\ -0.0246 & -0.0246 & 0.1669 \end{bmatrix} EigenvectorsImag = \begin{bmatrix} 0.0 & 0.0 & 0.0 \\ -0.2485 & 0.2485 & 0.0 \\ -0.5542 & 0.5542 & 0.0 \end{bmatrix}$$ ![figure](../assets/0479539830f53bec.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`computeEigenvectors`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Computation of the eigenvectors.

Default:
"none"

List of values:
"left", "none", "right"

**`eigenvaluesRealID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the real parts of the
eigenvalues.

**`eigenvaluesImagID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the imaginary parts of the
eigenvalues.

**`eigenvectorsRealID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the real parts of the
eigenvectors.

**`eigenvectorsImagID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle with the imaginary parts of the
eigenvectors.

## Result

If the parameters are valid, the operator
`EigenvaluesGeneralMatrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`,
`GetDiagonalMatrix`

## See also

`EigenvaluesSymmetricMatrix`,
`GeneralizedEigenvaluesSymmetricMatrix`,
`GeneralizedEigenvaluesGeneralMatrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
