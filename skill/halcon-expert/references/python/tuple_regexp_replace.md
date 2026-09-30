# tuple_regexp_replace (Operator)

## Name

`tuple_regexp_replace` — Replace a substring using regular expressions.

## Signature

`def tuple_regexp_replace(data: MaybeSequence[str], expression: MaybeSequence[str], replace: str) -> Sequence[str]`

`def tuple_regexp_replace_s(data: MaybeSequence[str], expression: MaybeSequence[str], replace: str) -> str`

## Description

`tuple_regexp_replace` applies the regular expression in
*`expression`* to one or more input strings in *`data`*,
and replaces the **first** matching substring using the *`replace`*
expression. For each input string, a processed output string is
returned in *`result`*.

Please refer to the documentation of [`tuple_regexp_match`](tuple_regexp_match.md) for syntax
and options of regular expressions. Additionally, `tuple_regexp_replace`
supports the option *"replace_all"*, which causes **all** matches
within each individual string to be replaced.

The *`replace`* expression may use the tag *"$0"* to refer to the
matched substring in the input data, *"$i"* to refer to the submatch of
the i-th capturing group (for i <= 9), and *"$$"* to
refer to the *'$'* literal.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

If *`data`* is an empty tuple, the operator returns an empty tuple. If
*`replace`* is an empty tuple and *`data`* is not empty, an
exception is raised.

### Unicode code points versus bytes

Regular expression matching operates on Unicode code points. One Unicode
code point may be composed of multiple bytes in the UTF-8 string.
If regular expression matching should only match on bytes, this operator can
be switched to byte mode with
`set_system('tsp_tuple_string_operator_mode','byte')`. If
*"filename_encoding"* is set to *"locale"* (legacy), this
operator always uses the byte mode.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_regexp_replace`,
which can be used in an expression in the following syntax:

[`Result := regexp_replace(Data, Expression, Replace)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`data`** (input_control)  string(-array) `→` MaybeSequence[str]

Input strings to process.

**`expression`** (input_control)  string(-array) `→` MaybeSequence[str]

Regular expression.

Default:
".*"

Suggested values:
".*", "replace_all", "ignore_case", "multiline", "dot_matches_all", "newline_lf", "newline_crlf", "newline_cr"

**`replace`** (input_control)  string `→` str

Replacement expression.

**`result`** (output_control)  string(-array) `→` Sequence[str]

Processed strings.

## Example (HDevelop)

```
tuple_regexp_replace(['img10.bmp','img11.bmp','img12.bmp'], \
                     'img(.*).bmp', 'out$1.txt', Result)
* Returns ['out10.txt','out11.txt','out12.txt']
```

## See also

`tuple_regexp_match`,
`tuple_regexp_test`,
`tuple_regexp_select`

## Module

Foundation
