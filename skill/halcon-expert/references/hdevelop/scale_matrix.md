# scale_matrix (Operator)

## Name

`scale_matrix` — Scale a matrix.

## Signature

`scale_matrix( : : MatrixID, Factor : MatrixScaledID)`

## Description

The operator `scale_matrix` scales the `Matrix` by a
constant factor. The matrix is defined by the matrix handle
*`MatrixID`*. A new matrix `MatrixScaled` is generated
with the result. The operator returns the matrix handle
*`MatrixScaledID`*. Access to the elements of the matrix is
possible e.g., with the operator [`get_full_matrix`](get_full_matrix.md). The
formula for the calculation of the result is:
$$\texttt{MatrixScaled}_{ij}=\texttt{Factor}\cdot\texttt{Matrix}_{ij}.$$

*Example:*

*`Factor`* = *1.5*
$$\text{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 \\ -2.0 & 6.0 & 2.0 \\ -5.0 & -4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/f76a2100d54acda9.svg)
$$\rightarrow MatrixScaled = \begin{bmatrix} 4.5 & 1.5 & -3.0 \\ -3.0 & 9.0 & 3.0 \\ -7.5 & -6.0 & 1.5 \end{bmatrix}$$ ![figure](../assets/2d007a46d60e27b9.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`Factor`** (input_control)  number `→`  (real / integer)

Scale factor.

Default:
2.0

Suggested values:
0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0

**`MatrixScaledID`** (output_control)  matrix `→`  (handle)

Matrix handle with the scaled elements.

## Result

If the parameters are valid, the operator `scale_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`get_full_matrix`,
`get_value_matrix`

## Alternatives

`scale_matrix_mod`

## See also

`mult_element_matrix`,
`mult_element_matrix_mod`,
`div_element_matrix`,
`div_element_matrix_mod`

## Module

Foundation
