# tuple_greater_equal (Operator)

## Name

`tuple_greater_equal` — Test whether a tuple is greater or equal to another tuple.

## Signature

`tuple_greater_equal( : : T1, T2 : Greatereq)`

## Description

`tuple_greater_equal` tests whether the input tuple
*`T1`* is greater or equal to *`T2`*. A tuple *`T1`*
is said to be greater or equal to a tuple *`T2`*, if
*`T1`* is not less than *`T2`*. A tuple *`T1`* is
said to be less than a tuple *`T2`*, if *`T1`* has been
found to be less when comparing it elementwise to *`T2`* or if
the first min(|T1|,|T2|) elements are equal and *`T1`* has
got less elements than *`T2`*.

With the elementwise comparison, the elements of *`T1`* and
*`T2`* are compared one by one. If the two elements are equal,
the next pair of elements will be examined. If the element of
*`T1`* is greater than that from *`T2`*, the result is 1 and
the comparison will be aborted. If the element of *`T1`* is less
than that from *`T2`*, the result is 0 and the comparison will be
aborted. If all elements have been tested and if all were equal, the
result is 1.

As a precondition for comparing the tuples elementwise two
corresponding elements must either both be (integer or floating point)
numbers or both be strings. Otherwise `tuple_greater_equal`
returns an error.

### Exception: Empty input tuples

If one input tuple is empty and the other is not, the tuple that is not
empty is considered greater than the empty one.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_greater_equal`,
which can be used in an expression in the following syntax:

[`Greatereq := T1 >= T2`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_comparison_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T1`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple 1.

**`T2`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple 2.

**`Greatereq`** (output_control)  integer `→`  (integer)

Result of the comparison of the input tuples.

## Alternatives

`tuple_greater`,
`tuple_less`,
`tuple_less_equal`,
`tuple_equal`,
`tuple_not_equal`,
`tuple_equal_elem`,
`tuple_not_equal_elem`,
`tuple_less_elem`,
`tuple_greater_elem`,
`tuple_less_equal_elem`,
`tuple_greater_equal_elem`

## Module

Foundation
