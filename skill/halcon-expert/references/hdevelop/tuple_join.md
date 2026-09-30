# tuple_join (Operator)

## Name

`tuple_join` — Join strings using separator symbol(s).

## Signature

`tuple_join( : : Strings, Separators : JoinedStrings)`

## Description

`tuple_join` joins the strings of the input tuple
*`Strings`* interleaved with the separators defined in the input tuple
*`Separators`* and returns the result in the tuple
*`JoinedStrings`*.

For each string element in *`Separators`*, there is one corresponding
element in *`JoinedStrings`* which holds the elements of *`Strings`*
joined by this separator.
Thereby an empty string in *`Separators`* corresponds to simple
string concatenation.

*Example:* *`Strings`* = *['aaa', 'bbb', 'ccc', 'ddd']*
and *`Separators`* = *['++', '--', '']*.
In this case the operator returns the tuple *`JoinedStrings`* =
*['aaa++bbb++ccc++ddd', 'aaa--bbb--ccc--ddd', 'aaabbbcccddd']*.

Both input tuples (*`Strings`* and *`Separators`*)
may only consist of strings.
Otherwise `tuple_join` returns an error.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### Unicode code points versus bytes

A separator always consists of the entire string.
This is true regardless of the system setting of
*'tsp_tuple_string_operator_mode'*.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_join`, which can be
used in an expression in the following syntax:

[`JoinedStrings := join(Strings, Separators)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Strings`** (input_control)  string(-array) `→`  (string)

Input tuple with strings to join.

**`Separators`** (input_control)  string(-array) `→`  (string)

Input tuple with separator symbol(s).

**`JoinedStrings`** (output_control)  string(-array) `→`  (string)

Output tuple with the contained strings.

## Possible Successors

`tuple_split`

## Alternatives

`tuple_strstr`,
`tuple_strrstr`,
`tuple_strchr`,
`tuple_strrchr`,
`tuple_strlen`,
`tuple_str_first_n`,
`tuple_str_last_n`,
`tuple_environment`

## Module

Foundation
