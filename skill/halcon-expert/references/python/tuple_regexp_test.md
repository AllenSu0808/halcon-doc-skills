# tuple_regexp_test (Operator)

## Name

`tuple_regexp_test` — Test if a string matches a regular expression.

## Signature

`def tuple_regexp_test(data: MaybeSequence[str], expression: MaybeSequence[str]) -> int`

## Description

`tuple_regexp_test` applies the regular expression in
*`expression`* to one or more input strings in *`data`*,
and returns the number of matching strings in *`num_matches`*.
In particular, the result for a single input string will be 1
in case of a match, and 0 otherwise.

Please refer to the documentation of [`tuple_regexp_match`](tuple_regexp_match.md) for syntax
and options of regular expressions. Additionally, `tuple_regexp_test`
supports the option *"invert_match"*, which causes those input strings
to be counted which do **not** match the regular expression.

For convenient use in conditional
expressions, this functionality is also available as the
*"=~"* operation in HDevelop.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

If the input tuple is empty, the operator returns 0.

### Unicode code points versus bytes

Regular expression matching operates on Unicode code points. One Unicode
code point may be composed of multiple bytes in the UTF-8 string.
If regular expression matching should only match on bytes, this operator can
be switched to byte mode with
`set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_regexp_test`,
which can be used in an expression in the following syntax:

[`NumMatches := regexp_test(Data, Expression)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)
or
[`NumMatches := Data =~ Expression`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`data`** (input_control)  string(-array) `→` MaybeSequence[str]

Input strings to match.

**`expression`** (input_control)  string(-array) `→` MaybeSequence[str]

Regular expression.

Default:
".*"

Suggested values:
".*", "invert_match", "ignore_case", "multiline", "dot_matches_all", "newline_lf", "newline_crlf", "newline_cr"

**`num_matches`** (output_control)  integer `→` int

Number of matching strings

## Example (HDevelop)

```
tuple_regexp_test ('p10662599755', '[A-Z]*', Result)
* Returns 0

tuple_regexp_test ('p10662599755', ['[A-Z]*','ignore_case'], Result)
* Returns 1
```

## Alternatives

`tuple_strstr`

## See also

`tuple_regexp_match`,
`tuple_regexp_replace`,
`tuple_regexp_select`

## Module

Foundation
