# tuple_is_serializable (Operator)

## Name

`tuple_is_serializable` — Test if a tuple is serializable.

## Signature

`def tuple_is_serializable(tuple: HTupleType) -> int`

## Description

`tuple_is_serializable` checks if *`tuple`* can be serialized with
[`serialize_tuple`](serialize_tuple.md).
If yes, *1* is returned in *`is_serializable`*.
Otherwise, *0* is returned.

A tuple can be serialized if it contains only integers, strings, reals, and
serializable handles.
Handles that are already freed cannot be serialized.
To check all elements of a tuple individually, use
[`tuple_is_serializable_elem`](tuple_is_serializable_elem.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`tuple`** (input_control)  tuple(-array) `→` HTupleType

Tuple to check for serializability.

**`is_serializable`** (output_control)  number `→` int

Boolean value indicating if the input can be serialized.

## Result

If the parameters are valid, the operator
`tuple_is_serializable` returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`serialize_tuple`,
`write_tuple`

## Alternatives

`tuple_is_serializable_elem`

## See also

`tuple_is_serializable_elem`,
`serialize_tuple`,
`serialize_handle`,
`deserialize_tuple`,
`deserialize_handle`,
`write_tuple`

## Module

Foundation
