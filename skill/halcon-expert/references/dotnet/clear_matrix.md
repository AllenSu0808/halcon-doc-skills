# ClearMatrix (Operator)

## Name

`ClearMatrix` — Free the memory of a matrix.

## Signature

`static void HOperatorSet.ClearMatrix(HTuple matrixID)`

`static void HMatrix.ClearMatrix(HMatrix[] matrixID)`

`void HMatrix.ClearMatrix()`

## Description

The operator `ClearMatrix` frees the memory of the matrix
`Matrix` given by the matrix handle *`matrixID`*.
After calling `ClearMatrix`, the `Matrix` can no
longer be used. The matrix handle *`matrixID`* becomes
invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- matrixID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`matrixID`** (input_control, state is modified)  matrix(-array) `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle.

## Result

If the parameters are valid, the operator `ClearMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`CreateMatrix`

## Module

Foundation
