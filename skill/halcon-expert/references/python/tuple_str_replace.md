# tuple_str_replace (Operator)

## Name

`tuple_str_replace` — Replace all occurrences of a substring within a string.

## Signature

`def tuple_str_replace(string: MaybeSequence[str], before: MaybeSequence[str], after: MaybeSequence[str]) -> Sequence[str]`

`def tuple_str_replace_s(string: MaybeSequence[str], before: MaybeSequence[str], after: MaybeSequence[str]) -> str`

## Description

`tuple_str_replace` replaces all occurrences of *`before`* in
*`string`* with *`after`* and returns the result in *`replaced`*.
All three tuples may only consist of strings. Otherwise, `tuple_str_replace`
returns an error.
As an exception, an empty tuple in *`after`* corresponds to an empty
string.
*`before`* and *`after`* must contain the same
number of elements. They can either contain one element, then *`before`* is
replaced with *`after`* in all input strings of the tuple *`string`*
or they can contain exactly the same number of elements as the tuple
*`string`*, then the n-th entry in *`before`* is replaced with the
n-th entry in *`after`* in the n-th entry of *`string`*.
The string with all replacements is returned in *`replaced`* and
contains the same number of elements as *`string`* in both cases.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_str_replace`,
which can be used in an expression in the following syntax:

[`Replaced := str_replace(String, Before, After)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`string`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple with string(s) to work on.

**`before`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple with string(s) to search.

**`after`** (input_control)  string(-array) `→` MaybeSequence[str]

Input tuple with string(s) to replace *`before`*.

**`replaced`** (output_control)  string(-array) `→` Sequence[str]

Output tuple with replaced strings.

## Alternatives

`tuple_regexp_replace`

## Module

Foundation
