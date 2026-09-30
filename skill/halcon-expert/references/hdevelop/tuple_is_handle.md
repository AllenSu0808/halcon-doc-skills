# tuple_is_handle (Operator)

## Name

`tuple_is_handle` — Test if the internal representation of a tuple is of type `handle`.

## Signature

`tuple_is_handle( : : T : IsHandle)`

## Description

`tuple_is_handle` tests if the internal representation of the
input tuple *`T`* is of type `handle`. In that case the value
*1* (true) is returned in *`IsHandle`*, otherwise the value
*0* (false) is returned. If a tuple consists of `handle`
elements only, *`IsHandle`* can nevertheless be 0 in case the internal
representation is H_TYPE_MIXED; see [`tuple_type`](tuple_type.md) for details.

### Exception: Empty input tuple

If the input tuple is empty, the operator returns *1*.

### HDevelop In-line Operation

HDevelop provides an in-line operation for `tuple_is_handle`,
which can be used in an expression in the following syntax:

[`IsHandle := is_handle(T)`](https://www.mvtec.com/doc/halcon/manuals/hdevelop_users_guide/hdevelop_language_operations_type_0000.html)

## Attention

Even if all tuple elements are of type `handle`,
`tuple_is_handle` returns *0* (false) if the internal
representation of the tuple is of type H_TYPE_MIXED. To test if the elements
of the tuple are of type `handle`, the operator
[`tuple_is_handle_elem`](tuple_is_handle_elem.md) should be used.

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`T`** (input_control)  tuple(-array) `→`  (handle / real / integer / string)

Input tuple.

**`IsHandle`** (output_control)  number `→`  (integer)

Boolean value indicating if the input tuple is of type
`handle`.

## Result

If the parameters are valid, the operator
`tuple_is_handle` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`tuple_type`,
`tuple_is_number`,
`tuple_is_handle_elem`,
`tuple_is_string`,
`tuple_sem_type`

## See also

`tuple_is_int`,
`tuple_is_real`,
`tuple_is_string`

## Module

Foundation
