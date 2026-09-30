# generalized_eigenvalues_general_matrix (Operator)

## Name

`generalized_eigenvalues_general_matrix` — Compute the generalized eigenvalues and optionally the generalized
eigenvectors of general matrices.

## Signature

`def generalized_eigenvalues_general_matrix(matrix_aid: HHandle, matrix_bid: HHandle, compute_eigenvectors: str) -> Tuple[HHandle, HHandle, HHandle, HHandle]`

## Description

The operator `generalized_eigenvalues_general_matrix`
computes all generalized eigenvalues and, optionally, the left
or right generalized eigenvectors of the square, general matrices
`MatrixA` and `MatrixB`. Both matrices must have
identical dimensions. The matrices are defined by the matrix
handles *`matrix_aid`* and *`matrix_bid`*. The computed
eigenvectors have the norm 1.

The operator generates the new matrices `EigenvaluesReal`
and `EigenvaluesImag` with the real and the imaginary parts
of the computed eigenvalues. Each matrix has one column and n
rows, where n is the number of rows or columns of the input
matrices. In contrast to the operator
[`generalized_eigenvalues_symmetric_matrix`](generalized_eigenvalues_symmetric_matrix.md), the order of the
generalized eigenvalues is not defined.
The operator returns the matrix handles
*`eigenvalues_real_id`* and *`eigenvalues_imag_id`*. If
desired, the real and imaginary parts of the respective
eigenvectors are stored in the new matrices
`EigenvectorsReal` and `EigenvectorsImag`. Here,
the jth column of the matrices of eigenvectors contains the
related eigenvector to the jth eigenvalue. For this, the
operator returns additionally the matrix handles
*`eigenvectors_real_id`* and *`eigenvectors_imag_id`*.
Access to the elements of the matrix is possible, e.g., with the
operator [`get_full_matrix`](get_full_matrix.md) or [`get_sub_matrix`](get_sub_matrix.md).

The computation type of eigenvectors can be selected via the
parameter *`compute_eigenvectors`*. If
*`compute_eigenvectors`* = *"none"*, no eigenvectors
are computed and the operator is faster. For this, the matrix
handles *`eigenvectors_real_id`* and *`eigenvectors_imag_id`*
are invalid. If *"right"* is selected, the right generalized
eigenvalues are computed. The formula for the calculation of the
result is
$$\texttt{MatrixA}\cdot x_{j}=\lambda_{j}\cdot\texttt{MatrixB}\cdot x_{j},$$
with $\lambda_{j}$ representing the $j$th (complex) eigenvalue
and $x_{j}$ represents the corresponding (complex) eigenvector.

If *"left"* is selected, the left generalized eigenvalues
are computed. The formula for the calculation of the result is
$$x_{j}^{H}\texttt{MatrixA}\cdot=x_{j}^{H}\cdot\lambda_{j}\cdot\texttt{MatrixB},$$
with $x_{j}^{H}$ represents the conjugate-transposed of $x_{j}$.

*Example:*

*`compute_eigenvectors`* = *"right"*
$$\text{MatrixA} = \begin{bmatrix} 6.0 & 4.0 & -8.0 \\ 5.0 & 7.0 & 3.0 \\ 4.0 & -1.0 & 4.0 \end{bmatrix} \\\text{MatrixB} = \begin{bmatrix} 3.0 & 1.0 & 2.0 \\ -5.0 & 7.0 & 2.0 \\ 9.0 & 4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/efbe9fa89a6357ac.svg)
$$\rightarrow\quad \text{EigenvaluesReal} = \begin{bmatrix}0.5363\\0.5363\\-6.1616\end{bmatrix} \text{EigenvaluesImag} = \begin{bmatrix}0.4208\\-0.4208\\0.0\end{bmatrix} \text{EigenvectorsReal} = \begin{bmatrix}0.3500\quad 0.3500\quad 0.0410\\-0.9565\quad -0.9565\quad 0.3267\n-0.2757\quad -0.2757\quad -1.0000\\-0.0750\quad -0.0750\quad 0.0000\end{bmatrix} \text{EigenvectorsImag} = \begin{bmatrix}-0.4644\quad 0.4644\quad 0.0\\0.0435\quad -0.0435\quad 0.0\\-0.1869\quad 0.1869\quad 0.0\end{bmatrix}$$ ![figure](../assets/27efa9d3fa54cc28.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrix_aid`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix A.

**`matrix_bid`** (input_control)  matrix `→` HHandle

Matrix handle of the input matrix B.

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
`generalized_eigenvalues_general_matrix` returns the value
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`,
`get_diagonal_matrix`

## See also

`generalized_eigenvalues_symmetric_matrix`,
`eigenvalues_symmetric_matrix`,
`eigenvalues_general_matrix`

## References

David Poole: “Linear Algebra: A Modern Introduction”; Thomson;
Belmont; 2006.
  
Gene H. Golub, Charles F. van Loan: “Matrix Computations”; The
Johns Hopkins University Press; Baltimore and London; 1996.

## Module

Foundation
