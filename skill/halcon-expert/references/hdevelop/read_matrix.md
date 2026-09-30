# read_matrix (Operator)

## Name

`read_matrix` — Read a matrix from a file.

## Signature

`read_matrix( : : FileName : MatrixID)`

## Description

The operator `read_matrix` reads a matrix, which has
been written to the file with [`write_matrix`](write_matrix.md), from the file
*`FileName`*. The default HALCON file extension for the
matrix is 'mtx'. The format of the file can be binary or ascii.
Each row of the file contains one row of a matrix with a number
of columns. The columns are separated with white spaces or tabs.
Each row must have the same number of columns. Empty lines are
ignored.

The reading results are stored in the matrix `Matrix`.
The operator returns the matrix handle *`MatrixID`* of this
matrix. Access to the elements of the matrix is possible e.g.,
with the operator [`get_full_matrix`](get_full_matrix.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

File name.

File extension:
.`mtx`

**`MatrixID`** (output_control)  matrix `→`  (handle)

Matrix handle.

## Result

If the file name is valid, the operator `read_matrix`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`get_full_matrix`

## Module

Foundation
