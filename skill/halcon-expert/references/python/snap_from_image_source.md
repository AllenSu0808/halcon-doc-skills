# snap_from_image_source (Operator)

## Name

`snap_from_image_source` — Acquire an image with corresponding meta data from an image source.

## Signature

`def snap_from_image_source(image_source_handle: HHandle) -> Tuple[HObject, HHandle]`

## Description

`snap_from_image_source` actively causes the acquisition of
*`images`* with the image source defined in the handle
*`image_source_handle`*. For conventional devices, *`images`*
is most likely to be a single image, but complex sensors, e.g. 3D sensors,
might provide multiple images at once. Additionally, meta information is
returned in *`data`*.

Internally, calling `snap_from_image_source` starts the image
acquisition, retrieves an image, and stops the acquisition again, freeing
all resources. It is therefore tailored towards the basic synchronous
acquisition of one image.
See [`fetch_from_image_source`](fetch_from_image_source.md) for continuous image acquisition.

As far as supported by the respective plugin, meta information
is returned in *`data`*.
If activated, meta information obtained from GenICam Chunk Data
is also returned in *`data`*.
Refer to [`fetch_from_image_source`](fetch_from_image_source.md) for a description of the
content of the *`data`* dictionary.

The device defined in *`image_source_handle`* needs to be
connected when calling `snap_from_image_source`.
See [`connect_image_source`](connect_image_source.md) on how to connect your image source.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`images`** (output_object)  image(-array) `→` HObject (byte / int1 / int2 / uint2 / int4 / int8 / real)

Acquired images.

**`image_source_handle`** (input_control)  image_source `→` HHandle

Handle of the image source that acquires the images.

**`data`** (output_control)  dict `→` HHandle

Meta information about the images.

## Result

If the parameter values are correct, `snap_from_image_source`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`connect_image_source`,
`set_image_source_param`

## Possible Successors

`disconnect_image_source`

## Module

Foundation
