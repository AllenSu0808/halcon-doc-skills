# tuple_regexp_select (Operator)

## Name

`tuple_regexp_select` — Select tuple elements matching a regular expression.

## Signature

`tuple_regexp_select( : : Data, Expression : Selection)`

## Description

`tuple_regexp_select` applies the regular expression in
*`Expression`* to one or more input strings in *`Data`*,
and returns the matching string elements in *`Selection`*. This
is convenient, e.g., for filtering a list of files obtained using
the operator [`list_files`](list_files.md).

Please refer to the documentation of [`tuple_regexp_match`](tuple_regexp_match.md) for syntax
and options of regular expressions. Additionally, `tuple_regexp_select`
supports the option *'invert_match'*, which causes those input strings
to be selected which do **not** match the regular expression.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

If the input tuple is empty, the operator returns an empty tuple.

### Unicode code points versus bytes

Regular expression matching operates on Unicode code points. One Unicode
code point may be composed of multiple bytes in the UTF-8 string.
If regular expression matching should only match on bytes, this operator can
be switched to byte mode with
`set_system('tsp_tuple_string_operator_mode','byte')`. If
*'filename_encoding'* is set to *'locale'* (legacy), this
operator always uses the byte mode.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_regexp_select`,
which can be used in an expression in the following syntax:

[`Selection := regexp_select(Data, Expression)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Data`** (input_control)  string(-array) `→`  (string)

Input strings to match.

**`Expression`** (input_control)  string(-array) `→`  (string)

Regular expression.

Default:
'.*'

Suggested values:
'.*', 'invert_match', 'ignore_case', 'multiline', 'dot_matches_all', 'newline_lf', 'newline_crlf', 'newline_cr'

**`Selection`** (output_control)  string(-array) `→`  (string)

Matching strings

## Example (HDevelop)

```
tuple_regexp_select (['.','..','mydir','a.png','b.txt','c.bmp','d.dat'], \
                     '.(bmp|png)', Result)
* Returns ['a.png','c.bmp']

tuple_regexp_select (Files, ['training','invert_match'], Matches)
* Returns all file names that do *not* contain the string 'training'
```

## Alternatives

`tuple_select`

## See also

`tuple_regexp_match`,
`tuple_regexp_replace`,
`tuple_regexp_test`

## Module

Foundation
