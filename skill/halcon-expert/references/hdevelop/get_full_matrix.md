# get_full_matrix (Operator)

## Name

`get_full_matrix` — Return all values of a matrix.

## Signature

`get_full_matrix( : : MatrixID : Values)`

## Description

The operator `get_full_matrix` returns the values of all
elements of the `Matrix` given by the matrix handle
*`MatrixID`*. The output parameter *`Values`* is a tuple
of floating point numbers and contains all values in a row-major
order, i.e., line by line.

*Example:*

$$\mathbf{Matrix}=\begin{bmatrix}3.0&1.0&-2.0\\-5.0&7.0&2.0\\-9.0&-4.0&1.0\end{bmatrix}\quad\rightarrow\quad\mathrm{Values}=[3.0,1.0,-2.0,-5.0,7.0,2.0,-9.0,-4.0,1.0]$$ ![figure](../assets/52984e3d51598fba.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`Values`** (output_control)  real(-array) `→`  (real)

Values of the matrix elements.

## Result

If the parameters are valid, the operator `get_full_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`create_matrix`

## Possible Successors

`clear_matrix`

## See also

`set_full_matrix`

## Module

Foundation
