# FnewLine (Operator)

## Name

`FnewLine` — Write a line break and clear the output buffer.

## Signature

`static void HOperatorSet.FnewLine(HTuple fileHandle)`

`void HFile.FnewLine()`

## Description

The operator `FnewLine` writes a line break into the output
file defined by the handle *`fileHandle`*.
The input file must have been opened with [`OpenFile`](open_file.md) in text format.
The call of `FnewLine` also empties possibly retained data from the
output buffer into the file (see [`FwriteString`](fwrite_string.md) and
`set_system(::'flush_file', <boolean-value>:)`).

Which characters are written as line break depends on the operating system:
under Windows the sequence
*"\r\n"*
(carriage return + line feed) is used as the standard line break,
under Linux just *"\n"* (line feed).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileHandle`** (input_control)  file `→` [HFile](HFile.md), [HTuple](HTuple.md) (*IntPtr*)

File handle.

## Example (HDevelop)

```
  fwrite_string(FileHandle,'Good Morning')
  fnew_line(FileHandle)
```

## Result

If an output file is open and it can be written to the file,
the operator `FnewLine`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`FwriteString`

## See also

`FwriteString`

## Module

Foundation
