# SerializeImage (Operator)

## Name

`SerializeImage` — Serialize an image object.

## Signature

`static void HOperatorSet.SerializeImage(HObject image, out HTuple serializedItemHandle)`

`HSerializedItem HImage.SerializeImage()`

## Description

`SerializeImage` serializes an image object (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The image object is defined by the parameter
*`image`*. The serialized image object is returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeImage`](deserialize_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Image object.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeImage` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`ReadImage`

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeImage`

## Module

Foundation
