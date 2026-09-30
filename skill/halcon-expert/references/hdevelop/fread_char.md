# fread_char (Operator)

## Name

`fread_char` — Read one character from a text file.

## Signature

`fread_char( : : FileHandle : Char)`

## Description

The operator `fread_char` reads a character from the input
file defined by *`FileHandle`*.
The input file must have been opened with [`open_file`](open_file.md) in text format.

The read character or the control character sequence 'eof' is returned in
parameter *`Char`*.
The operator `fread_char` respects the encoding of the characters,
unless the file was opened with the option *'ignore_encoding'*
(see [`open_file`](open_file.md)).
Thus, when opened with the correct encoding the operator `fread_char`
returns multi-byte characters at once.
If necessary, the character is transcoded into the current encoding of the
HALCON library (see `set_system(::'filename_encoding',<encoding>:)`).

When the file was opened with encoding mode *'ignore_encoding'*,
*`Char`* always returns one byte without any interpretation or
transcoding. This is useful for reading a file with special control bytes
in a kind of raw mode.
If no character can be read because the end of the file is reached,
`fread_char` returns the control character sequence *'eof'* in
*`Char`*.

The operator `fread_char` emits a low-level error message, when
the next byte or byte sequence does not represent a valid code point in the
specified encoding. Despite of the low-level error message, the operator
will not fail and *`Char`* will contain the next byte.
Furthermore, the operator also emits a low-level error
message, when the read character cannot be transcoded without loss of
information into the current encoding of the HALCON library.
This can only happen when the file is UTF-8 encoded and the
current encoding of the HALCON library is *'locale'*
(see `set_system(::'filename_encoding','locale':)`).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileHandle`** (input_control)  file `→`  (handle)

File handle.

**`Char`** (output_control)  string `→`  (string)

Read character, which can be multi-byte or the control string
*'eof'*.

## Example (HDevelop)

```
* Read a text file character by character.
open_file (FileName, 'input', FileHandle)
repeat
    fread_char (FileHandle, Char)
until (Char == 'eof')
close_file (FileHandle)
```

## Result

If an input file is open, the operator `fread_char` returns 2 (
H_MSG_TRUE)
.
Otherwise, an exception is raised.
Encoding errors have no influence on the result state.

## Possible Predecessors

`open_file`

## Possible Successors

`close_file`

## Alternatives

`fread_string`,
`read_string`,
`fread_line`

## See also

`open_file`,
`close_file`,
`fread_string`,
`fread_line`

## Module

Foundation
