# ReadMatrix (Operator)

## Name

`ReadMatrix` — Read a matrix from a file.

## Signature

`static void HOperatorSet.ReadMatrix(HTuple fileName, out HTuple matrixID)`

`public HMatrix(string fileName)`

`void HMatrix.ReadMatrix(string fileName)`

## Description

The operator `ReadMatrix` reads a matrix, which has
been written to the file with [`WriteMatrix`](write_matrix.md), from the file
*`fileName`*. The default HALCON file extension for the
matrix is 'mtx'. The format of the file can be binary or ascii.
Each row of the file contains one row of a matrix with a number
of columns. The columns are separated with white spaces or tabs.
Each row must have the same number of columns. Empty lines are
ignored.

The reading results are stored in the matrix `Matrix`.
The operator returns the matrix handle *`matrixID`* of this
matrix. Access to the elements of the matrix is possible e.g.,
with the operator [`GetFullMatrix`](get_full_matrix.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`mtx`

**`matrixID`** (output_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle.

## Result

If the file name is valid, the operator `ReadMatrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`GetFullMatrix`

## Module

Foundation
