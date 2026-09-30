# serialize_image (Operator)

## Name

`serialize_image` — Serialize an image object.

## Signature

`serialize_image(Image : : : SerializedItemHandle)`

## Description

`serialize_image` serializes an image object (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The image object is defined by the parameter
*`Image`*. The serialized image object is returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_image`](deserialize_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Image object.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

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
