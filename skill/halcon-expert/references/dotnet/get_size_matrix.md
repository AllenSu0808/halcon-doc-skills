# GetSizeMatrix (Operator)

## Name

`GetSizeMatrix` — Get the size of a matrix.

## Signature

`static void HOperatorSet.GetSizeMatrix(HTuple matrixID, out HTuple rows, out HTuple columns)`

`void HMatrix.GetSizeMatrix(out int rows, out int columns)`

## Description

The operator `GetSizeMatrix` returns the number of rows
*`rows`* and columns *`columns`* of the input
`Matrix`. The input `Matrix` is defined by the
matrix handle *`matrixID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`rows`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of rows of the matrix.

**`columns`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of columns of the matrix.

## Result

If the parameters are valid, the operator `GetSizeMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Possible Successors

`ClearMatrix`

## Module

Foundation
