# WriteMatrix (Operator)

## Name

`WriteMatrix` — Write a matrix to a file.

## Signature

`static void HOperatorSet.WriteMatrix(HTuple matrixID, HTuple fileFormat, HTuple fileName)`

`void HMatrix.WriteMatrix(string fileFormat, string fileName)`

## Description

The operator `WriteMatrix` writes a matrix to the
file *`fileName`*. The matrix can be read with
[`ReadMatrix`](read_matrix.md). The default HALCON file extension for the
matrix is 'mtx'. The format of the file can be selected
via the parameter *`fileFormat`*. The following values are
supported: *"binary"* for a binary file format, and
*"ascii"* for a ascii text format. In the text format
each row of the file contains one row of the matrix. The columns
are separated with white spaces. The advantage of using the binary
file format instead of the ascii text format is a smaller size of
the output file.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`matrixID`** (input_control)  matrix `→` [HMatrix](HMatrix.md), [HTuple](HTuple.md) (*IntPtr*)

Matrix handle of the input matrix.

**`fileFormat`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Format of the file.

Default:
"binary"

List of values:
"ascii", "binary"

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`mtx`

## Result

If the file name is valid (write permission), the operator
`WriteMatrix` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`CreateMatrix`

## Module

Foundation
