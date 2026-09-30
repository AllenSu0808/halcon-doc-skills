# eigenvalues_general_matrix (Operator)

## Name

`eigenvalues_general_matrix` — Compute the eigenvalues and optionally the eigenvectors of a general
matrix.

## Signature

`def eigenvalues_general_matrix(matrix_id: HHandle, compute_eigenvectors: str) -> Tuple[HHandle, HHandle, HHandle, HHandle]`

## Description

The operator `eigenvalues_general_matrix` computes all
eigenvalues and, optionally, the left or right eigenvectors of a
square, general `Matrix`. The matrix is defined by the
matrix handle *`matrix_id`*. The computed eigenvectors have the
norm 1.

The operator generates the new matrices `EigenvaluesReal`
and `EigenvaluesImag` with the real and the imaginary parts
of the computed eigenvalues. Each matrix has one column and n
rows, where n is the number of rows of the input `Matrix`.
In contrast to the operator [`eigenvalues_symmetric_matrix`](eigenvalues_symmetric_matrix.md),
the order of the eigenvalues is not defined.
The operator returns the matrix handles *`eigenvalues_real_id`*
and *`eigenvalues_imag_id`*. If desired, the real and imaginary
parts of the computed eigenvectors are stored in the new matrices
`EigenvectorsReal` and `EigenvectorsImag`. For
this, the operator returns valid matrix handles
*`eigenvectors_real_id`* and *`eigenvectors_imag_id`*.
Access to the elements of the matrix is possible e.g., with the
operator [`get_full_matrix`](get_full_matrix.md).

The computation type of eigenvectors can be selected via the
parameter *`compute_eigenvectors`*. If
*`compute_eigenvectors`* = *"none"*, no eigenvectors are
computed. If *"left"* is selected, the left eigenvalues are
computed. If *"right"* is selected, the right eigenvalues are
computed.

*Example:*

*`compute_eigenvectors`* = *"right"*
$$\text{Matrix}=\left[\begin{array}{ccc}6.0 & 4.0 & -8.0\\5.0 & 7.0 & 3.0\\4.0 & -1.0 & 4.0\end{array}\right]$$ ![figure](../assets/3cb2dee0a30853f3.svg)
$$\rightarrow EigenvaluesReal = \begin{bmatrix} 3.3110 \\ 3.3110 \\ 10.3781 \end{bmatrix} EigenvaluesImag = \begin{bmatrix} 5.4143 \\ -5.4143 \\ 0.0 \end{bmatrix} EigenvectorsReal = \begin{bmatrix} 0.6353 & 0.6353 & 0.4813 \\ -0.4764 & -0.4764 & 0.8605 \\ -0.0246 & -0.0246 & 0.1669 \end{bmatrix} EigenvectorsImag = \begin{bmatrix} 0.0 & 0.0 & 0.0 \\ -0.2485 & 0.2485 & 0.0 \\ -0.5542 & 0.5542 & 0.0 \end{bmatrix}$$ ![figure](../assets/0479539830f53bec.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_id`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix.

**`compute_eigenvectors`** (input_control)  string `→` str

Computation of the eigenvectors.

Default:
"none"

List of values:
"left", "none", "right"

**`eigenvalues_real_id`** (output_control)  matrix `→` HHandle

Matrix handle with the real parts of the
eigenvalues.

**`eigenvalues_imag_id`** (output_control)  matrix `→` HHandle

Matrix handle with the imaginary parts of the
eigenvalues.

**`eigenvectors_real_id`** (output_control)  matrix `→` HHandle

Matrix handle with the real parts of the
eigenvectors.

**`eigenvectors_imag_id`** (output_control)  matrix `→` HHandle

Matrix handle with the imaginary parts of the
eigenvectors.

## Result

If the parameters are valid, the operator
`eigenvalues_general_matrix` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`,
`get_diagonal_matrix`

## See also

`eigenvalues_symmetric_matrix`,
`generalized_eigenvalues_symmetric_matrix`,
`generalized_eigenvalues_general_matrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
