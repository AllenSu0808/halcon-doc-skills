# tuple_replace (Operator)

## Name

`tuple_replace` — Replaces one or more elements of a tuple.

## Signature

`tuple_replace( : : Tuple, Index, ReplaceTuple : Replaced)`

## Description

`tuple_replace` replaces one or more elements of the
input tuple *`Tuple`* and returns them with *`Replaced`*.
At this, *`Index`* determines the indices of the elements
and *`ReplaceTuple`* the corresponding values to replace.
The parameter *`Index`* must contain one or more integer values
(any floating point number must represent an integer value without
fraction). Indices of tuple elements start at 0. Therefore, the first
tuple element has got the index 0. If *`ReplaceTuple`* contains only
one value, this value will be replaced at all indices of *`Index`*.
If a value of *`Index`* is greater than the length of the input
tuple *`Tuple`*, *`Replaced`* will be extended accordingly and
initialized with zeros. For example, if *`Tuple`* contains [1],
*`Index`* contains the values [2,4], and *`ReplaceTuple`*
contains the values [3,5], *`Replaced`* will be [1,0,3,0,5].

It is allowed to mix strings and numbers in the input tuples
*`Tuple`* and *`ReplaceTuple`*.

### Exception: Empty input tuples

If either *`Index`* or *`ReplaceTuple`* is empty and the other is
not, an exception is raised. If both are empty, the output tuple
*`Replaced`* corresponds to the input *`Tuple`*. If both are
empty, but the input *`Tuple`* is not, the empty tuple will be
extended as described above.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_replace`,
which can be used in an expression in the following syntax:

[`Replaced := replace(Tuple, Index, ReplaceTuple)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Index`** (input_control)  integer(-array) `→`  (integer)

Index/Indices of elements to be replaced.

**`ReplaceTuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Element(s) to replace.

**`Replaced`** (output_control)  tuple-array `→`  (integer / real / string)

Tuple with replaced elements.

## Alternatives

`tuple_select`,
`tuple_first_n`,
`tuple_last_n`,
`tuple_select_mask`,
`tuple_str_bit_select`,
`tuple_concat`,
`tuple_select_rank`

## See also

`tuple_remove`,
`tuple_insert`

## Module

Foundation
