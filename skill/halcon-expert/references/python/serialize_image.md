# serialize_image (Operator)

## Name

`serialize_image` — Serialize an image object.

## Signature

`def serialize_image(image: HObject) -> HHandle`

## Description

`serialize_image` serializes an image object (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The image object is defined by the parameter
*`image`*. The serialized image object is returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_image`](deserialize_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Image object.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_image` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_image`

## Module

Foundation
