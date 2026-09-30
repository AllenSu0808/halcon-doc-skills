# TupleSelectRange (Operator)

## Name

`TupleSelectRange` — Select several elements of a tuple.

## Signature

`static void HOperatorSet.TupleSelectRange(HTuple tuple, HTuple leftindex, HTuple rightindex, out HTuple selected)`

`HTuple HTuple.TupleSelectRange(HTuple leftindex, HTuple rightindex)`

## Description

`TupleSelectRange` selects several consecutive elements of the
input tuple *`tuple`* and returns them with *`selected`*.
At this, *`leftindex`* determines the index of the first element
and *`rightindex`* determines the index of the last element to select.
Thus, both parameters *`leftindex`* and *`rightindex`* must
contain a single integer value (any floating point number must
represent an integer value without fraction). Indices of tuple elements
start at 0, that means, the first tuple element has got the index 0.
The result tuple *`selected`* contains every element from the
tuple *`tuple`* that has got an index between *`leftindex`*
and *`rightindex`* (including the elements at position
*`leftindex`* and *`rightindex`*). If the indices are equal,
only one element is selected.
In addition, it is possible that the right index is *`leftindex`* - 1.
In this case and if the left or right index are valid an empty tuple
is returned. Hence, the index *`rightindex`* must be greater or
equal to *`leftindex`* - 1.

### Exception: Empty input tuples

If *`leftindex`* and *`rightindex`* are empty tuples, the operator
returns an empty tuple. If only one of those parameters or *`tuple`*
is an empty tuple, an exception is raised.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleSelectRange`,
which can be used in an expression in the following syntax:

[`Selected := Tuple[Leftindex:Rightindex]`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_tuple_0000.html)

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Input tuple.

**`leftindex`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of first element to select.

**`rightindex`** (input_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Index of last element to select.

**`selected`** (output_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string)

Selected tuple elements.

## Alternatives

`TupleSelect`,
`TupleFirstN`,
`TupleLastN`,
`TupleSelectMask`,
`TupleStrBitSelect`,
`TupleConcat`,
`TupleSelectRank`

## See also

`TupleRemove`

## Module

Foundation
