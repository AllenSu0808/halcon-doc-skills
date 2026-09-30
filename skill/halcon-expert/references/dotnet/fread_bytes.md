# FreadBytes (Operator)

## Name

`FreadBytes` — Read bytes from a binary file.

## Signature

`static void HOperatorSet.FreadBytes(HTuple fileHandle, HTuple numberOfBytes, out HTuple readData, out HTuple isEOF)`

`HTuple HFile.FreadBytes(int numberOfBytes, out int isEOF)`

## Description

The operator `FreadBytes` reads bytes from the input
file defined by *`fileHandle`*.
The input file must have been opened with [`OpenFile`](open_file.md) in
binary format.

The number of bytes to be read, greater than *0*, is specified
as *`numberOfBytes`*.

The bytes that are read are returned in *`readData`*.
*`isEOF`* is set to *1* if end of file is reached while reading
the bytes from the input binary file. Otherwise, it is set to *0*.

When the number of bytes to be read is larger than the number of
bytes in the input binary file, the operator `FreadBytes` returns
all bytes read till the end of the file in *`readData`* and parameter
*`isEOF`* is set to *1*.

If no byte can be read because the end of the file is reached,
*`readData`* is empty and *`isEOF`* is set to *1*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileHandle`** (input_control)  file `→` [HFile](HFile.md), [HTuple](HTuple.md) (*IntPtr*)

File handle.

**`numberOfBytes`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of bytes to be read.

**`readData`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Bytes read from the input binary file.

**`isEOF`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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
operator `FreadBytes` returns 2 (
H_MSG_TRUE)
. Otherwise, an exception is
raised.

## Possible Predecessors

`OpenFile`

## Possible Successors

`CloseFile`

## Alternatives

`FreadChar`

## See also

`OpenFile`,
`CloseFile`,
`FwriteBytes`

## Module

Foundation
