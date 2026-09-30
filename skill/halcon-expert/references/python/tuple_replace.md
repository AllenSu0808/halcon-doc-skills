# tuple_replace (Operator)

## Name

`tuple_replace` — Replaces one or more elements of a tuple.

## Signature

`def tuple_replace(tuple: MaybeSequence[Union[float, int, str]], index: MaybeSequence[int], replace_tuple: MaybeSequence[Union[float, int, str]]) -> Sequence[Union[float, int, str]]`

## Description

`tuple_replace` replaces one or more elements of the
input tuple *`tuple`* and returns them with *`replaced`*.
At this, *`index`* determines the indices of the elements
and *`replace_tuple`* the corresponding values to replace.
The parameter *`index`* must contain one or more integer values
(any floating point number must represent an integer value without
fraction). Indices of tuple elements start at 0. Therefore, the first
tuple element has got the index 0. If *`replace_tuple`* contains only
one value, this value will be replaced at all indices of *`index`*.
If a value of *`index`* is greater than the length of the input
tuple *`tuple`*, *`replaced`* will be extended accordingly and
initialized with zeros. For example, if *`tuple`* contains [1],
*`index`* contains the values [2,4], and *`replace_tuple`*
contains the values [3,5], *`replaced`* will be [1,0,3,0,5].

It is allowed to mix strings and numbers in the input tuples
*`tuple`* and *`replace_tuple`*.

### Exception: Empty input tuples

If either *`index`* or *`replace_tuple`* is empty and the other is
not, an exception is raised. If both are empty, the output tuple
*`replaced`* corresponds to the input *`tuple`*. If both are
empty, but the input *`tuple`* is not, the empty tuple will be
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

**`tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Input tuple.

**`index`** (input_control)  integer(-array) `→` MaybeSequence[int]

Index/Indices of elements to be replaced.

**`replace_tuple`** (input_control)  tuple(-array) `→` MaybeSequence[Union[float, int, str]]

Element(s) to replace.

**`replaced`** (output_control)  tuple-array `→` Sequence[Union[float, int, str]]

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
