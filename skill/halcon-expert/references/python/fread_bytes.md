# fread_bytes (Operator)

## Name

`fread_bytes` — Read bytes from a binary file.

## Signature

`def fread_bytes(file_handle: HHandle, number_of_bytes: int) -> Tuple[Sequence[int], int]`

## Description

The operator `fread_bytes` reads bytes from the input
file defined by *`file_handle`*.
The input file must have been opened with [`open_file`](open_file.md) in
binary format.

The number of bytes to be read, greater than *0*, is specified
as *`number_of_bytes`*.

The bytes that are read are returned in *`read_data`*.
*`is_eof`* is set to *1* if end of file is reached while reading
the bytes from the input binary file. Otherwise, it is set to *0*.

When the number of bytes to be read is larger than the number of
bytes in the input binary file, the operator `fread_bytes` returns
all bytes read till the end of the file in *`read_data`* and parameter
*`is_eof`* is set to *1*.

If no byte can be read because the end of the file is reached,
*`read_data`* is empty and *`is_eof`* is set to *1*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`file_handle`** (input_control)  file `→` HHandle

File handle.

**`number_of_bytes`** (input_control)  integer `→` int

Number of bytes to be read.

**`read_data`** (output_control)  integer-array `→` Sequence[int]

Bytes read from the input binary file.

**`is_eof`** (output_control)  integer `→` int

Indicates if end of file is reached while reading
the file.

## Example (HDevelop)

```
* Read a binary file 5 bytes at a time till EOF is reached.
open_file(Filename,'input_binary',FileHandle)
repeat
  fread_bytes(FileHandle, 5, BytesRead, IsEOF)
until (IsEOF)
close_file (FileHandle)
```

## Result

If an input file is open in binary mode and no file read error occurs,the
operator `fread_bytes` returns 2 (
H_MSG_TRUE)
. Otherwise, an exception is
raised.

## Possible Predecessors

`open_file`

## Possible Successors

`close_file`

## Alternatives

`fread_char`

## See also

`open_file`,
`close_file`,
`fwrite_bytes`

## Module

Foundation
