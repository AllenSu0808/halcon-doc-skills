# file_exists (Operator)

## Name

`file_exists` — Check whether file exists.

## Signature

`def file_exists(file_name: str) -> int`

## Description

The operator `file_exists` checks whether the
indicated file already exists. If this is the case, the parameter
*`file_exists`* is set to TRUE, otherwise to FALSE.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`file_name`** (input_control)  filename `→` str

Name of file to be checked.

Default:
"/bin/cc"

**`file_exists`** (output_control)  integer `→` int

Boolean number.

## Result

If the parameters are correct the operator `file_exists` returns
the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`open_file`

## Alternatives

`open_file`

## Module

Foundation
