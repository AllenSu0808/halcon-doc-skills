# FreadLine (Operator)

## Name

`FreadLine` — Read a character line from a text file.

## Signature

`static void HOperatorSet.FreadLine(HTuple fileHandle, out HTuple outLine, out HTuple isEOF)`

`string HFile.FreadLine(out int isEOF)`

## Description

The operator `FreadLine` reads a whole line (including the line break
character) from the input file defined by the handle *`fileHandle`*.
The input file must have been opened with [`OpenFile`](open_file.md) in text format.

The read line is returned in parameter *`outLine`*.
It starts at the current file position and ends at the end of the file or
with the first line break character found.
A subsequent read operation on the file would start after the line break,
i.e., at the beginning of the next line.
If needed, the output string is transcoded into the current encoding of the
HALCON library (the default is UTF-8).

The range of control characters that are handled as line break depends on
the file encoding, which can be specified when the file is opened with
[`OpenFile`](open_file.md).
The standard line break characters are
*"\n"* (line feed),
*"\r"* (carriage return), and
*"\f"* (form feed).
These characters are accepted on all encodings or when the encoding has to
be ignored.
The line break sequence
*"\r\n"*
(carriage return + line feed), which
is the default line break under Windows, is handled (on all systems)
as one line break and returned as
*"\n"* in the output string.
In UTF-8 encoded files, the following Unicode control code points will also
terminate the read line: *U+0085* (next line), *U+2028*
(line separator), and *U+2029* (paragraph separator).

If the end of the file is reached before any character was written to the
output string, the parameter *`isEOF`* returns the value *1*,
otherwise *0*.

The operator `FreadLine` emits a low-level error message, when
it encounters bytes that do not represent a valid code point in the
specified encoding.
Despite of the low-level error message, the operator will not fail and
*`outLine`* will contain potentially invalid bytes
(invalid within the specified encoding).
Furthermore, the operator also emits a low-level error message, when the
output string cannot be transcoded without loss of information into the
current encoding of the HALCON library.
For a correctly encoded string this can only happen when the file is
UTF-8 encoded and the current encoding of the HALCON library is
*"locale"* (see `set_system(::'filename_encoding','locale':)`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`fileHandle`** (input_control)  file `→` [HFile](HFile.md), [HTuple](HTuple.md) (*IntPtr*)

File handle.

**`outLine`** (output_control)  string `→` [HTuple](HTuple.md) (*string*)

Read line.

**`isEOF`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Reached end of file before any character was read.

## Example (C)

```
do {
  fread_line(FileHandle,&Line,&IsEOF);
} while(IsEOF==0);
```

## Result

If the file is open and a suitable line is read, `FreadLine`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised.
Encoding errors have no influence on the result state.

## Possible Predecessors

`OpenFile`

## Possible Successors

`CloseFile`

## Alternatives

`FreadChar`,
`FreadString`

## See also

`OpenFile`,
`CloseFile`,
`FreadChar`,
`FreadString`

## Module

Foundation
