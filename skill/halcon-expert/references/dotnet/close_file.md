# CloseFile (Operator)

## Name

`CloseFile` — Closing a text file.

## Signature

`static void HOperatorSet.CloseFile(HTuple fileHandle)`

`static void HFile.CloseFile(HFile[] fileHandle)`

`void HFile.CloseFile()`

## Description

The operator `CloseFile` closes a file which was opened
via the operator [`OpenFile`](open_file.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileHandle`** (input_control)  file(-array) `→` [HFile](HFile.md), [HTuple](HTuple.md) (*IntPtr*)

File handle.

## Example (HDevelop)

```
open_file ('standard', 'output', FileHandle)
* ....
close_file(FileHandle)
```

## Result

If the file handle is correct
`CloseFile` returns the value 2 (
H_MSG_TRUE)
.
Otherwise an exception is raised.

## Possible Predecessors

`OpenFile`

## See also

`OpenFile`

## Module

Foundation
