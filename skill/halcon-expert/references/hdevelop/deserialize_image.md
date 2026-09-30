# deserialize_image (Operator)

## Name

`deserialize_image` — Deserialize a serialized image object.

## Signature

`deserialize_image( : Image : SerializedItemHandle : )`

## Description

`deserialize_image` deserializes an image object, that was serialized
by [`serialize_image`](serialize_image.md) (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized image object is defined by the parameter
*`SerializedItemHandle`*. The deserialized image is stored
in the image object defined by the parameter *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (output_object)  image(-array) `→` object (byte / direction / cyclic / int1 / complex / int2 / uint2 / vector_field / int4 / int8 / real)

Image object.

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`deserialize_image` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_image`

## Possible Successors

`disp_image`,
`threshold`,
`regiongrowing`,
`count_channels`,
`decompose3`,
`class_ndim_norm`,
`gauss_filter`,
`fill_interlace`,
`zoom_image_size`,
`zoom_image_factor`,
`crop_part`,
`write_image`,
`rgb1_to_gray`

## See also

`serialize_image`

## Module

Foundation
