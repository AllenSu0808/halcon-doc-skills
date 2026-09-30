# deserialize_tuple (Operator)

## Name

`deserialize_tuple` — Deserialize a serialized tuple.

## Signature

`deserialize_tuple( : : SerializedItemHandle : Tuple)`

## Description

`deserialize_tuple` deserializes the data of a tuple, that was
serialized by [`serialize_tuple`](serialize_tuple.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized data of the tuple is defined by the handle
*`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
tuple with the handle *`Tuple`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`Tuple`** (output_control)  tuple(-array) `→`  (real / integer / string / handle)

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
