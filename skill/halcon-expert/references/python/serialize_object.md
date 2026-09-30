# serialize_object (Operator)

## Name

`serialize_object` — Serialize an iconic object.

## Signature

`def serialize_object(object: HObject) -> HHandle`

## Description

`serialize_object` serializes an iconic object (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The iconic object is a tuple of image objects,
region objects, or XLD objects, and is defined by the parameter
*`object`*. The serialized iconic object is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_object`](deserialize_object.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`object`** (input_object)  object(-array) `→` HObject

Iconic object.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_object` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_object`

## See also

`deserialize_object`

## Module

Foundation
