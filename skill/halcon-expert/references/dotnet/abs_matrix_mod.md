# AbsMatrixMod (Operator)

## Name

`AbsMatrixMod` — Compute the absolute values of the elements of a matrix.

## Signature

`static void HOperatorSet.AbsMatrixMod(HTuple matrixID)`

`void HMatrix.AbsMatrixMod()`

## Description

The operator `AbsMatrixMod` computes the absolute values of
all elements of the input `Matrix` given by the matrix
handle *`matrixID`*. The input matrix is overwritten with the
result. Access to the elements of the matrix is possible e.g., with
the operator [`GetFullMatrix`](get_full_matrix.md). The formula for the
calculation of the result is:
$$\texttt{Matrix}_{ij}=|\texttt{Matrix}_{ij}|.$$

*Example:*

$$\mathrm{Matrix} = \begin{bmatrix} 3.0 & 1.0 & -2.0 \\ -5.0 & 7.0 & 2.0 \\ -9.0 & -4.0 & 1.0 \end{bmatrix} \rightarrow \mathrm{Matrix} = \begin{bmatrix} 3.0 & 1.0 & 2.0 \\ 5.0 & 7.0 & 2.0 \\ 9.0 & 4.0 & 1.0 \end{bmatrix}$$ ![figure](../assets/08fc8b699979d1cb.svg)

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

## Result

If the parameters are valid, the operator `AbsMatrixMod` returns
the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`GetFullMatrix`,
`GetValueMatrix`

## Alternatives

`AbsMatrix`

## Module

Foundation
