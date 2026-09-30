# read_object (Operator)

## Name

`read_object` — Read an iconic object.

## Signature

`read_object( : Object : FileName : )`

## Description

`read_object` reads an iconic object from the file *`FileName`*.
The file must be written in the HALCON Iconic Object format (HOBJ),
which is supported by the operators [`write_object`](write_object.md),
[`write_image`](write_image.md), and [`write_region`](write_region.md). See [`write_object`](write_object.md)
for more information about the HOBJ format.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Object`** (output_object)  object(-array) `→` object

Iconic object.

**`FileName`** (input_control)  filename `→`  (string)

Name of file.

File extension:
.`hobj`

## Result

If the parameters are valid, the operator
`read_object` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`write_image`,
`write_object`

## See also

`write_object`,
`write_image`,
`read_image`

## Module

Foundation
