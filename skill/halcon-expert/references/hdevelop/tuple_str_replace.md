# tuple_str_replace (Operator)

## Name

`tuple_str_replace` — Replace all occurrences of a substring within a string.

## Signature

`tuple_str_replace( : : String, Before, After : Replaced)`

## Description

`tuple_str_replace` replaces all occurrences of *`Before`* in
*`String`* with *`After`* and returns the result in *`Replaced`*.
All three tuples may only consist of strings. Otherwise, `tuple_str_replace`
returns an error.
As an exception, an empty tuple in *`After`* corresponds to an empty
string.
*`Before`* and *`After`* must contain the same
number of elements. They can either contain one element, then *`Before`* is
replaced with *`After`* in all input strings of the tuple *`String`*
or they can contain exactly the same number of elements as the tuple
*`String`*, then the n-th entry in *`Before`* is replaced with the
n-th entry in *`After`* in the n-th entry of *`String`*.
The string with all replacements is returned in *`Replaced`* and
contains the same number of elements as *`String`* in both cases.

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

**`String`** (input_control)  string(-array) `→`  (string)

Input tuple with string(s) to work on.

**`Before`** (input_control)  string(-array) `→`  (string)

Input tuple with string(s) to search.

**`After`** (input_control)  string(-array) `→`  (string)

Input tuple with string(s) to replace *`Before`*.

**`Replaced`** (output_control)  string(-array) `→`  (string)

Output tuple with replaced strings.

## Alternatives

`tuple_regexp_replace`

## Module

Foundation
