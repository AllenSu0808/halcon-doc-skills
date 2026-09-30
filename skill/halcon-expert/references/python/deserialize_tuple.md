# deserialize_tuple (Operator)

## Name

`deserialize_tuple` — Deserialize a serialized tuple.

## Signature

`def deserialize_tuple(serialized_item_handle: HHandle) -> Sequence[HTupleElementType]`

`def deserialize_tuple_s(serialized_item_handle: HHandle) -> HTupleElementType`

## Description

`deserialize_tuple` deserializes the data of a tuple, that was
serialized by [`serialize_tuple`](serialize_tuple.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized data of the tuple is defined by the handle
*`serialized_item_handle`*.
The deserialized values are stored in an automatically created
tuple with the handle *`tuple`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`tuple`** (output_control)  tuple(-array) `→` Sequence[HTupleElementType]

Tuple.

## Result

If the parameters are valid, the operator
`deserialize_tuple` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_tuple`

## Module

Foundation
