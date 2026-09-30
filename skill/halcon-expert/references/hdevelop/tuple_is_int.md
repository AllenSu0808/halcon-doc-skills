# tuple_is_int (Operator)

## Name

`tuple_is_int` — Test if the internal representation of a tuple is of type `integer`.

## Signature

`tuple_is_int( : : T : IsInt)`

## Description

`tuple_is_int` tests if the internal representation of the
input tuple *`T`* is of type `integer`. In that case
the value *1* (true) is returned in *`IsInt`*, otherwise the value
*0* (false) is returned. If a tuple consists of `integer` elements only,
*`IsInt`* can nevertheless be 0 in case the internal representation
is H_TYPE_MIXED; see [`tuple_type`](tuple_type.md) for details.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 1.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_int`,
which can be used in an expression in the following syntax:

[`IsInt := is_int(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

Even if all tuple elements are of type `integer`,
`tuple_is_int` returns *0* (false) if the internal representation
of the tuple is of type H_TYPE_MIXED. To test if the elements of the
tuple are of type `integer` the operator [`tuple_is_int_elem`](tuple_is_int_elem.md)
should be used.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (integer / real / string / handle)

Input tuple.

**`IsInt`** (output_control)  number `→`  (integer)

Is the input tuple of type `integer`?

## Example (HDevelop)

```
tuple_is_int ([3.1416,'pi',3], IsIntA)
* IsIntA = false
tuple_is_int ([1,2,3], IsIntB)
* IsIntB = true
tuple_is_int ([], IsIntC)
* IsIntC = true
```

## Result

If the parameters are valid, the operator
`tuple_is_int` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_type`,
`tuple_is_number`,
`tuple_is_int_elem`

## See also

`tuple_is_real`,
`tuple_is_string`,
`tuple_is_handle`

## Module

Foundation
