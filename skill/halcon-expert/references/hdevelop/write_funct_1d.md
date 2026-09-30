# write_funct_1d (Operator)

## Name

`write_funct_1d` — Write a function to a file.

## Signature

`write_funct_1d( : : Function, FileName : )`

## Description

The operator `write_funct_1d` writes the contents of *`Function`*
to a file. The data is written in an ASCII format. Therefore, the file can
be exchanged between different architectures (see also
[Tuple / String Operations](toc_tuple_stringoperations.md)).
The data can be read by the operator [`read_funct_1d`](read_funct_1d.md).
There is no specific extension for this kind of file.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Function`** (input_control)  function_1d `→`  (real / integer)

Function to be written.

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the file to be written.

## Result

If the parameters are correct the operator `write_funct_1d`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`create_funct_1d_pairs`,
`create_funct_1d_array`

## Alternatives

`write_tuple`,
`fwrite_string`

## See also

`read_funct_1d`,
`write_image`,
`write_region`,
`open_file`

## Module

Foundation
