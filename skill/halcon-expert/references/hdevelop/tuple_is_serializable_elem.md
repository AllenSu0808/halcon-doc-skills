# tuple_is_serializable_elem (Operator)

## Name

`tuple_is_serializable_elem` — Test if the elements of a tuple are serializable.

## Signature

`tuple_is_serializable_elem( : : Tuple : IsSerializableElem)`

## Description

[`tuple_is_serializable`](tuple_is_serializable.md) checks if the elements of *`Tuple`* can
be serialized with [`serialize_tuple`](serialize_tuple.md).
The output *`IsSerializableElem`* has the same length as the input
*`Tuple`* and contains at each position either *0* if the
corresponding entry in *`Tuple`* cannot be serialized, or
*1* if it can.

A tuple element can be serialized if it is an integer, a string, a real value
or a serializable handle.
Handles that are already freed cannot be serialized.
To check the complete tuple for serializability, use
[`tuple_is_serializable`](tuple_is_serializable.md).

## Execution Information

- Multithreading type: independent (runs in parallel even with exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (handle / integer / real / string)

Tuple to check for serializability.

**`IsSerializableElem`** (output_control)  number(-array) `→`  (integer)

Boolean value indicating if the input elements can be serialized.

## Example (HDevelop)

```
* Serialize all serializable elements of a tuple
tuple_is_serializable_elem (Tuple, IsSerializableElem)
if (sum(IsSerializableElem[=]0)>0)
  Tuple[find(IsSerializableElem,0)] := HNULL
endif
serialize_tuple (Tuple, SerializedItem)
```

## Result

If the parameters are valid, the operator
[`tuple_is_serializable`](tuple_is_serializable.md) returns the value 2 (
H_MSG_TRUE)
.

## Possible Successors

`serialize_tuple`,
`write_tuple`

## Alternatives

`tuple_is_serializable`

## See also

`tuple_is_serializable`,
`serialize_tuple`,
`serialize_handle`,
`deserialize_tuple`,
`deserialize_handle`,
`write_tuple`

## Module

Foundation
