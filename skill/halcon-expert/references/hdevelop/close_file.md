# close_file (Operator)

## Name

`close_file` — Closing a text file.

## Signature

`close_file( : : FileHandle : )`

## Description

The operator `close_file` closes a file which was opened
via the operator [`open_file`](open_file.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileHandle`** (input_control)  file(-array) `→`  (handle)

File handle.

## Example (HDevelop)

```
open_file ('standard', 'output', FileHandle)
* ....
close_file(FileHandle)
```

## Result

If the file handle is correct
`close_file` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`open_file`

## See also

`open_file`

## Module

Foundation
