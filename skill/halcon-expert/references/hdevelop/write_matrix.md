# write_matrix (Operator)

## Name

`write_matrix` — Write a matrix to a file.

## Signature

`write_matrix( : : MatrixID, FileFormat, FileName : )`

## Description

The operator `write_matrix` writes a matrix to the
file *`FileName`*. The matrix can be read with
[`read_matrix`](read_matrix.md). The default HALCON file extension for the
matrix is 'mtx'. The format of the file can be selected
via the parameter *`FileFormat`*. The following values are
supported: *'binary'* for a binary file format, and
*'ascii'* for a ascii text format. In the text format
each row of the file contains one row of the matrix. The columns
are separated with white spaces. The advantage of using the binary
file format instead of the ascii text format is a smaller size of
the output file.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`MatrixID`** (input_control)  matrix `→`  (handle)

Matrix handle of the input matrix.

**`FileFormat`** (input_control)  string `→`  (string)

Format of the file.

Default:
'binary'

List of values:
'ascii', 'binary'

**`FileName`** (input_control)  filename.write `→`  (string)

File name.

File extension:
.`mtx`

## Result

If the file name is valid (write permission), the operator
`write_matrix` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`create_matrix`

## Module

Foundation
