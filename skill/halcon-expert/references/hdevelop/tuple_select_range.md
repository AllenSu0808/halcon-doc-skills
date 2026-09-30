# tuple_select_range (Operator)

## Name

`tuple_select_range` — Select several elements of a tuple.

## Signature

`tuple_select_range( : : Tuple, Leftindex, Rightindex : Selected)`

## Description

`tuple_select_range` selects several consecutive elements of the
input tuple *`Tuple`* and returns them with *`Selected`*.
At this, *`Leftindex`* determines the index of the first element
and *`Rightindex`* determines the index of the last element to select.
Thus, both parameters *`Leftindex`* and *`Rightindex`* must
contain a single integer value (any floating point number must
represent an integer value without fraction). Indices of tuple elements
start at 0, that means, the first tuple element has got the index 0.
The result tuple *`Selected`* contains every element from the
tuple *`Tuple`* that has got an index between *`Leftindex`*
and *`Rightindex`* (including the elements at position
*`Leftindex`* and *`Rightindex`*). If the indices are equal,
only one element is selected.
In addition, it is possible that the right index is *`Leftindex`* - 1.
In this case and if the left or right index are valid an empty tuple
is returned. Hence, the index *`Rightindex`* must be greater or
equal to *`Leftindex`* - 1.

### Exception: Empty input tuples

If *`Leftindex`* and *`Rightindex`* are empty tuples, the operator
returns an empty tuple. If only one of those parameters or *`Tuple`*
is an empty tuple, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_select_range`,
which can be used in an expression in the following syntax:

[`Selected := Tuple[Leftindex:Rightindex]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (integer / real / string)

Input tuple.

**`Leftindex`** (input_control)  integer(-array) `→`  (integer)

Index of first element to select.

**`Rightindex`** (input_control)  integer(-array) `→`  (integer)

Index of last element to select.

**`Selected`** (output_control)  tuple(-array) `→`  (integer / real / string)

Selected tuple elements.

## Alternatives

`tuple_select`,
`tuple_first_n`,
`tuple_last_n`,
`tuple_select_mask`,
`tuple_str_bit_select`,
`tuple_concat`,
`tuple_select_rank`

## See also

`tuple_remove`

## Module

Foundation
