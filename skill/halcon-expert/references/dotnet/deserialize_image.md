# DeserializeImage (Operator)

## Name

`DeserializeImage` — Deserialize a serialized image object.

## Signature

`static void HOperatorSet.DeserializeImage(out HObject image, HTuple serializedItemHandle)`

`void HImage.DeserializeImage(HSerializedItem serializedItemHandle)`

## Description

`DeserializeImage` deserializes an image object, that was serialized
by [`SerializeImage`](serialize_image.md) (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized image object is defined by the parameter
*`serializedItemHandle`*. The deserialized image is stored
in the image object defined by the parameter *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image`** (output_object)  image(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Image object.

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`DeserializeImage` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeImage`

## Possible Successors

`DispImage`,
`Threshold`,
`Regiongrowing`,
`CountChannels`,
`Decompose3`,
`ClassNdimNorm`,
`GaussFilter`,
`FillInterlace`,
`ZoomImageSize`,
`ZoomImageFactor`,
`CropPart`,
`WriteImage`,
`Rgb1ToGray`

## See also

`SerializeImage`

## Module

Foundation
