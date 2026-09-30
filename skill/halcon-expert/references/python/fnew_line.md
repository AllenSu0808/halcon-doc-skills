# fnew_line (Operator)

## Name

`fnew_line` — Write a line break and clear the output buffer.

## Signature

`def fnew_line(file_handle: HHandle) -> None`

## Description

The operator `fnew_line` writes a line break into the output
file defined by the handle *`file_handle`*.
The input file must have been opened with [`open_file`](open_file.md) in text format.
The call of `fnew_line` also empties possibly retained data from the
output buffer into the file (see [`fwrite_string`](fwrite_string.md) and
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

**`file_handle`** (input_control)  file `→` HHandle

File handle.

## Result

If an output file is open and it can be written to the file,
the operator `fnew_line`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`fwrite_string`

## See also

`fwrite_string`

## Module

Foundation
