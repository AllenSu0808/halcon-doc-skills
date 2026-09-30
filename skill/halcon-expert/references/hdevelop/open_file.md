# open_file (Operator)

## Name

`open_file` — Open a file in text or binary format.

## Signature

`open_file( : : FileName, FileType : FileHandle)`

## Description

`open_file` opens a file in text format or in binary format.
The name of the file is defined by the parameter *`FileName`*.
The operator `open_file` returns a handle to the file in the output
parameter *`FileHandle`*.
The parameter *`FileType`* determines the type of the file.
For text files this parameter can also be used to specify the encoding
used for strings in that file, where besides UTF-8 only the local-8-bit
encoding is supported.

The following settings for *`FileType`* are supported:

- ***'input'*:** —

  An already existing input file is opened for reading in text format.
- ***'output'*:** —

  A new output file is opened for writing in text format.
- ***'append'*:** —

  An already existing output file is opened for writing at the end of the
  file in text format.
- ***'input_binary'*:** —

  An already existing input file is opened for reading in binary format.
- ***'output_binary'*:** —

  A new output file is opened for writing in binary format.
- ***'append_binary'*:** —

  An already existing output file is opened for writing at the end of the
  file in binary format.

For text files the tuple passed to *`FileType`* can be extended by
one of the following encoding settings:

- ***'utf8_encoding'*:** —

  Strings in the file are encoded in UTF-8.
  This is the default, so for UTF-8 encoded files and all files which use
  only pure 7-bit US-ASCII characters this value can be omitted.
- ***'locale_encoding'*:** —

  Strings in the file are encoded in the local-8-bit encoding which
  depends on the system's current locale setting.
  Valid encodings are defined, e.g., under Windows by the code pages 1252
  (a Microsoft dialect of Latin-1) or 932 (Shift-JIS) or on Linux by the
  locales en_US.utf8, de_DE.iso885915, or ja_JP.sjis.
- ***'ignore_encoding'*:** —

  The encoding of the strings that are read from the file or written into
  it is not handled. In that mode multi-byte characters are neither
  processed nor interpreted, the operator [`fread_char`](fread_char.md) returns
  always one byte, and separator characters that depend on a specific
  locale are not handled in [`fread_line`](fread_line.md) and [`fread_string`](fread_string.md).
  Furthermore, the strings are not transcoded into or from the current
  encoding of the HALCON library.

  Note: Strings are still transcoded in the HALCON C/C++ interface,
  when the encoding of the HALCON C/C++ interface differs from the encoding
  of the HALCON library. For HDevelop scripts, the encoding is always set
  to UTF-8. To avoid transcoding of strings to HDevelop, the
  encoding of the HALCON library should be set to UTF-8.

For the standard terminal input and output streams, the file names
*'standard'* (*'input'* and *'output'*) and
*'error'* (only *'output'*) are reserved.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename `→`  (string)

Name of file to be opened.

Default:
'standard'

Suggested values:
'standard', 'error', '/tmp/dat.dat'

**`FileType`** (input_control)  string(-array) `→`  (string)

Type of file access and optional the string encoding.

Default:
'output'

List of values:
'append', 'append_binary', 'ignore_encoding', 'input', 'input_binary', 'locale_encoding', 'output', 'output_binary', 'utf8_encoding'

**`FileHandle`** (output_control)  file `→`  (handle)

File handle.

## Example (HDevelop)

```
* Create an output text file with the name '/tmp/log.txt'
* and write a string to the file:
open_file ('/tmp/log.txt', 'output', FileHandle)
fwrite_string (FileHandle, 'these are the first and last lines')
fnew_line (FileHandle)
close_file (FileHandle)

* Write a string to the standard output stream (stdout),
* typically used to display information in the console:
open_file ('standard', 'output', FileHandle)
fwrite_string (FileHandle, 'Hello console')
close_file (FileHandle)
```

## Result

If the parameters are valid, the operator
`open_file` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Successors

`fwrite_string`,
`fread_char`,
`fread_string`,
`fread_line`,
`fread_serialized_item`,
`fwrite_serialized_item`,
`fread_bytes`,
`fwrite_bytes`,
`close_file`

## See also

`close_file`

## Module

Foundation
