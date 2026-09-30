# fwrite_string (Operator)

## Name

`fwrite_string` — Write strings and numbers into a text file.

## Signature

`fwrite_string( : : FileHandle, String : )`

## Description

The operator `fwrite_string` writes one or more strings or numbers
to the output file defined by the handle *`FileHandle`*.
The output file must have been opened with [`open_file`](open_file.md) in text format.

Strings and numbers that are to be written into the file are passed via the
input parameter *`String`* to the operator `fwrite_string`.
The parameter *`String`* accepts also tuples where strings
and numbers are mixed.
All elements of the tuple are written consecutively into the file without
blanks or other separators in between.
Numbers are converted into a string before they are written.

The operator `fwrite_string` emits a low-level error message, when the
string cannot be transcoded without loss of information into the specified
file encoding.
This can only happen when the file encoding is
*'locale_encoding'* and the current encoding of the HALCON library is
*'utf8'* (see `set_system(::'filename_encoding','utf8':)`).

The call `set_system(::'flush_file', <boolean-value>:)`
determines whether the output characters are immediately written to the file
or not.
If the value *'flush_file'* is set to *'false'*, the characters
(especially in case of screen output) show up only after the operator
[`fnew_line`](fnew_line.md) is called.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`FileHandle`** (input_control)  file `→`  (handle)

File handle.

**`String`** (input_control)  string(-array) `→`  (string / integer / real)

Values to be written into the file.

Default:
'hallo'

## Example (HDevelop)

```
fwrite_string(FileHandle,['text with numbers:',5,' and ',1.0])
* results in the following output:
* 'text with numbers:5 and 1.00000'
```

## Result

If the writing procedure was carried out
successfully, the operator `fwrite_string`
returns the value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.
Encoding errors have no influence on the result state.

## Possible Predecessors

`open_file`

## Possible Successors

`close_file`

## Alternatives

`write_string`

## See also

`open_file`,
`close_file`,
`set_system`

## Module

Foundation
