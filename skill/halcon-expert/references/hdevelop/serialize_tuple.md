# serialize_tuple (Operator)

## Name

`serialize_tuple` — Serialize a tuple.

## Signature

`serialize_tuple( : : Tuple : SerializedItemHandle)`

## Description

`serialize_tuple` serializes the data of a tuple (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_tuple`](write_tuple.md) is converted to a serialized item.
The tuple is defined by the handle *`Tuple`*. The
serialized data of a tuple is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_tuple`](deserialize_tuple.md).

Note that not all handle types can be serialized.
If *`Tuple`* contains a handle that can not be serialized or that
has been freed already, an exception is raised.
The operators [`tuple_is_serializable`](tuple_is_serializable.md) and
[`tuple_is_serializable_elem`](tuple_is_serializable_elem.md) can be used to find out if a tuple or
its elements can be serialized.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Tuple`** (input_control)  tuple(-array) `→`  (real / integer / string / handle)

Tuple.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_tuple` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_tuple`

## Module

Foundation
