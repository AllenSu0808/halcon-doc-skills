# fwrite_bytes (Operator)

## Name

`fwrite_bytes` — Write bytes to a binary file.

## Signature

`def fwrite_bytes(file_handle: HHandle, data_to_write: Sequence[int]) -> int`

## Description

The operator `fwrite_bytes` writes bytes to the output
file defined by *`file_handle`*.
The output file must have been opened with [`open_file`](open_file.md) in
binary format.

The data to be written to the file is specified as *`data_to_write`*.

The number of bytes that are written to the file is returned in
*`number_of_bytes_written`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`file_handle`** (input_control)  file `→` HHandle

File handle.

**`data_to_write`** (input_control)  integer-array `→` Sequence[int]

Data to be written to the file.

**`number_of_bytes_written`** (output_control)  integer `→` int

Number of bytes written to the output
binary file.

## Example (HDevelop)

```
* Write a binary file byte by byte.
open_file (Filename, 'append_binary', FileHandle)
fwrite_bytes(FileHandle, [0x97, 99, 102], BytesWritten)
close_file (FileHandle)
```

## Result

If an output file is open in binary mode and no file write error occurs,
the operator `fwrite_bytes` returns 2 (
H_MSG_TRUE)
. Otherwise, an exception is
raised.

## Possible Predecessors

`open_file`

## Possible Successors

`close_file`

## Alternatives

`fwrite_string`

## See also

`open_file`,
`close_file`,
`fread_bytes`

## Module

Foundation
