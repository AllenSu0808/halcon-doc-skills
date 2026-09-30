# TupleStrReplace (Operator)

## Name

`TupleStrReplace` — Replace all occurrences of a substring within a string.

## Signature

`static void HOperatorSet.TupleStrReplace(HTuple stringVal, HTuple before, HTuple after, out HTuple replaced)`

`HTuple HTuple.TupleStrReplace(HTuple before, HTuple after)`

## Description

`TupleStrReplace` replaces all occurrences of *`before`* in
*`stringVal`* with *`after`* and returns the result in *`replaced`*.
All three tuples may only consist of strings. Otherwise, `TupleStrReplace`
returns an error.
As an exception, an empty tuple in *`after`* corresponds to an empty
string.
*`before`* and *`after`* must contain the same
number of elements. They can either contain one element, then *`before`* is
replaced with *`after`* in all input strings of the tuple *`stringVal`*
or they can contain exactly the same number of elements as the tuple
*`stringVal`*, then the n-th entry in *`before`* is replaced with the
n-th entry in *`after`* in the n-th entry of *`stringVal`*.
The string with all replacements is returned in *`replaced`* and
contains the same number of elements as *`stringVal`* in both cases.

For general information about string operations see
[Tuple / String Operations](toc_tuple_stringoperations.md).

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleStrReplace`,
which can be used in an expression in the following syntax:

[`Replaced := str_replace(String, Before, After)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_string_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`stringVal`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with string(s) to work on.

**`before`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with string(s) to search.

**`after`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Input tuple with string(s) to replace *`before`*.

**`replaced`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Output tuple with replaced strings.

## Alternatives

`TupleRegexpReplace`

## Module

Foundation
