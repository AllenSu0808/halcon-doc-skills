# fread_bytes (Operator)

## Name

`fread_bytes` — Read bytes from a binary file.

## Signature

`fread_bytes( : : FileHandle, NumberOfBytes : ReadData, IsEOF)`

## Description

The operator `fread_bytes` reads bytes from the input
file defined by *`FileHandle`*.
The input file must have been opened with [`open_file`](open_file.md) in
binary format.

The number of bytes to be read, greater than *0*, is specified
as *`NumberOfBytes`*.

The bytes that are read are returned in *`ReadData`*.
*`IsEOF`* is set to *1* if end of file is reached while reading
the bytes from the input binary file. Otherwise, it is set to *0*.

When the number of bytes to be read is larger than the number of
bytes in the input binary file, the operator `fread_bytes` returns
all bytes read till the end of the file in *`ReadData`* and parameter
*`IsEOF`* is set to *1*.

If no byte can be read because the end of the file is reached,
*`ReadData`* is empty and *`IsEOF`* is set to *1*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileHandle`** (input_control)  file `→`  (handle)

File handle.

**`NumberOfBytes`** (input_control)  integer `→`  (integer)

Number of bytes to be read.

**`ReadData`** (output_control)  integer-array `→`  (integer)

Bytes read from the input binary file.

**`IsEOF`** (output_control)  integer `→`  (integer)

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
