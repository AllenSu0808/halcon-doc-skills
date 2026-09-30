# TupleIsInt (Operator)

## Name

`TupleIsInt` — Test if the internal representation of a tuple is of type `integer`.

## Signature

`static void HOperatorSet.TupleIsInt(HTuple t, out HTuple isInt)`

`HTuple HTuple.TupleIsInt()`

## Description

`TupleIsInt` tests if the internal representation of the
input tuple *`t`* is of type `integer`. In that case
the value *1* (true) is returned in *`isInt`*, otherwise the value
*0* (false) is returned. If a tuple consists of `integer` elements only,
*`isInt`* can nevertheless be 0 in case the internal representation
is H_TYPE_MIXED; see [`TupleType`](tuple_type.md) for details.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns 1.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `TupleIsInt`,
which can be used in an expression in the following syntax:

[`IsInt := is_int(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

Even if all tuple elements are of type `integer`,
`TupleIsInt` returns *0* (false) if the internal representation
of the tuple is of type H_TYPE_MIXED. To test if the elements of the
tuple are of type `integer` the operator [`TupleIsIntElem`](tuple_is_int_elem.md)
should be used.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`t`** (input_control)  tuple(-array) `→` [HTuple](HTuple.md) (*int* / long / double / string / HHandle)

Input tuple.

**`isInt`** (output_control)  number `→` [HTuple](HTuple.md) (*int* / long)

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
`TupleIsInt` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`TupleType`,
`TupleIsNumber`,
`TupleIsIntElem`

## See also

`TupleIsReal`,
`TupleIsString`,
`TupleIsHandle`

## Module

Foundation
