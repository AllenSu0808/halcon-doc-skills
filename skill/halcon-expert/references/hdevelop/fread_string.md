# fread_string (Operator)

## Name

`fread_string` — Read a string from a text file.

## Signature

`fread_string( : : FileHandle : OutString, IsEOF)`

## Description

The operator `fread_string` reads a string from the
input file defined by the handle *`FileHandle`*.
The input file must have been opened with [`open_file`](open_file.md) in text format.

A string begins with the first character that is not a separator, i.e., that
is no white space or line break: all other characters, mainly letters,
numbers, and all other printable characters, but also all other control
characters that are no separators are added to the output string.
The string ends at the first separator character after one or more
accepted characters, or when the end of the file was reached.
The terminating separator character is not added to the output string, but
the file position indicator remains after it. Thus, a subsequent read
operation on the file would start after the terminating separator character.
The read character sequence is returned in parameter *`OutString`*.
If needed, the output string is transcoded into the current encoding of the
HALCON library (the default is UTF-8).

The range of characters that are handled as separator depends on the
file encoding, which can be specified when the file is opened.
The character *' '* (space) and the standard ASCII whitespace control
characters
*'\t'* (tab),
*'\f'* (form feed),
*'\n'* (line feed),
*'\r'* (carriage return), and
*'\v'* (vertical tab)
are all accepted as separator on all locales or when the encoding has to be
ignored.
Other encodings may provide additional separator characters, e.g.,
Latin-1 defines *'0xA0'* (no-break space) or Shift-JIS (as many other
Asian encodings) defines *'0x8140'* (ideographic space) as valid
separator.
UTF-8 handles these characters also as a separator just as all other
code points which in the Unicode standard are defined as white spaces in
the categories space separators *Zs*, line separators *Zl*, and
paragraph separators *Zp*.

If the end of the file is reached before any character was written to the
output string, *`IsEOF`* returns the value *1*, otherwise
*0*.

The operator `fread_string` emits a low-level error message, when
it encounters bytes that do not represent a valid code point in the
specified encoding.
Despite of the low-level error message, the operator will not fail and
*`OutString`* will contain potentially invalid bytes
(invalid within the specified encoding).
Furthermore, the operator also emits a low-level error message, when the
output string cannot be transcoded without loss of information into the
current encoding of the HALCON library.
For a correctly encoded string this can only happen when the file is
UTF-8 encoded and the current encoding of the HALCON library is
*'locale'* (see `set_system(::'filename_encoding','locale':)`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileHandle`** (input_control)  file `→`  (handle)

File handle.

**`OutString`** (output_control)  string `→`  (string)

Read character sequence.

**`IsEOF`** (output_control)  integer `→`  (integer)

Reached end of file before any character was added to the
output string.

## Example (HDevelop)

```
fwrite_string(FileHandle,'Please enter text and return: ..')
fread_string(FileHandle,String,IsEOF)
fwrite_string(FileHandle,['here it is again: ',String])
fnew_line(FileHandle)
```

## Result

If a file is open and a suitable string is read, `fread_string`
returns the value 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised.
Encoding errors have no influence on the result state.

## Possible Predecessors

`open_file`

## Possible Successors

`close_file`

## Alternatives

`fread_char`,
`read_string`,
`fread_line`

## See also

`open_file`,
`close_file`,
`fread_char`,
`fread_line`

## Module

Foundation
