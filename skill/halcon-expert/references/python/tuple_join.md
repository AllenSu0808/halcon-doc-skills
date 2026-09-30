# tuple_join (Operator)

## Name

`tuple_join` — Join strings using separator symbol(s).

## Signature

`def tuple_join(strings: MaybeSequence[str], separators: MaybeSequence[str]) -> Sequence[str]`

`def tuple_join_s(strings: MaybeSequence[str], separators: MaybeSequence[str]) -> str`

## Description

`tuple_join` joins the strings of the input tuple
*`strings`* interleaved with the separators defined in the input tuple
*`separators`* and returns the result in the tuple
*`joined_strings`*.

For each string element in *`separators`*, there is one corresponding
element in *`joined_strings`* which holds the elements of *`strings`*
joined by this separator.
Thereby an empty string in *`separators`* corresponds to simple
string concatenation.

*Example:* *`strings`* = *["aaa", "bbb", "ccc", "ddd"]*
and *`separators`* = *["++", "--", ""]*.
In this case the operator returns the tuple *`joined_strings`* =
*["aaa++bbb++ccc++ddd", "aaa--bbb--ccc--ddd", "aaabbbcccddd"]*.

Both input tuples (*`strings`* and *`separators`*)
may only consist of strings.
Otherwise `tuple_join` returns an error.

### Exception: Empty input tuples

If either or both of the input tuples are empty, the operator returns an
empty tuple.

### Unicode code points versus bytes

A separator always consists of the entire string.
This is true regardless of the system setting of
*"tsp_tuple_string_operator_mode"*.

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

**`strings`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple with strings to join.

**`separators`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple with separator symbol(s).

**`joined_strings`** (output_control)  string(-array) `→` Sequence[str]

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
