# deserialize_object (Operator)

## Name

`deserialize_object` — Deserialize a serialized iconic object.

## Signature

`def deserialize_object(serialized_item_handle: HHandle) -> HObject`

## Description

`deserialize_object` deserializes an iconic object, that was
serialized by [`serialize_object`](serialize_object.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md)
for an introduction of the basic principle of serialization). The
serialized iconic object is defined by the parameter
*`serialized_item_handle`*. The deserialized iconic object is
stored in the iconic object defined by the parameter *`object`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object`** (output_object)  object(-array) `→` HObject

Iconic object.

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`deserialize_object` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_object`

## See also

`serialize_object`

## Module

Foundation
