# GetFullMatrix (Operator)

## Name

`GetFullMatrix` — Return all values of a matrix.

## Signature

`static void HOperatorSet.GetFullMatrix(HTuple matrixID, out HTuple values)`

`HTuple HMatrix.GetFullMatrix()`

## Description

The operator `GetFullMatrix` returns the values of all
elements of the `Matrix` given by the matrix handle
*`matrixID`*. The output parameter *`values`* is a tuple
of floating point numbers and contains all values in a row-major
order, i.e., line by line.

*Example:*

$$\mathbf{Matrix}=\begin{bmatrix}3.0&1.0&-2.0\\-5.0&7.0&2.0\\-9.0&-4.0&1.0\end{bmatrix}\quad\rightarrow\quad\mathrm{Values}=[3.0,1.0,-2.0,-5.0,7.0,2.0,-9.0,-4.0,1.0]$$ ![figure](../assets/52984e3d51598fba.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`values`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Values of the matrix elements.

## Result

If the parameters are valid, the operator `GetFullMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`ClearMatrix`

## See also

`SetFullMatrix`

## Module

Foundation
