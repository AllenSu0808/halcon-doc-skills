# FwriteBytes (Operator)

## Name

`FwriteBytes` — Write bytes to a binary file.

## Signature

`static void HOperatorSet.FwriteBytes(HTuple fileHandle, HTuple dataToWrite, out HTuple numberOfBytesWritten)`

`int HFile.FwriteBytes(HTuple dataToWrite)`

## Description

The operator `FwriteBytes` writes bytes to the output
file defined by *`fileHandle`*.
The output file must have been opened with [`OpenFile`](open_file.md) in
binary format.

The data to be written to the file is specified as *`dataToWrite`*.

The number of bytes that are written to the file is returned in
*`numberOfBytesWritten`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileHandle`** (input_control)  file `→` [HFile](HFile.md), [HTuple](HTuple.md) (*IntPtr*)

File handle.

**`dataToWrite`** (input_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Data to be written to the file.

**`numberOfBytesWritten`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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
the operator `FwriteBytes` returns 2 (
H_MSG_TRUE)
. Otherwise, an exception is
raised.

## Possible Predecessors

`OpenFile`

## Possible Successors

`CloseFile`

## Alternatives

`FwriteString`

## See also

`OpenFile`,
`CloseFile`,
`FreadBytes`

## Module

Foundation
