# fetch_from_image_source (Operator)

## Name

`fetch_from_image_source` — Fetch images and corresponding meta data from the image source
buffer queue.

## Signature

`def fetch_from_image_source(image_source_handle: HHandle) -> Tuple[HObject, HHandle]`

## Description

`fetch_from_image_source` fetches *`images`*
from the buffer queue of the image source defined in the handle
*`image_source_handle`*. For conventional devices, *`images`*
is most likely to be a single image, but complex sensors, e.g. 3D sensors,
might provide multiple images at once.
Additionally, meta information is returned in *`data`*.

`fetch_from_image_source` tries to pull images from the buffer queue
of the image source and deliver it to the application.
If the buffer queue is empty, the operator waits for an image to arrive
in the buffer queue up to the configured timeout value
(see *"fetch_timeout"* in [`get_image_source_param`](get_image_source_param.md)).
If images have arrived in the buffer queue before the call of
`fetch_from_image_source` it returns immediately by pulling one
buffer from the queue and delivering its contained images. The operator
runtime depends on various factors like for example the state of the buffer
queue and the current configuration of the imaging device.
See *"num_buffers"* in [`get_image_source_param`](get_image_source_param.md)
on how to adapt the buffer queue capacity.

Based on availability, the returned meta information in the *`data`*
dictionary contains the following:

- In the sub-dictionary *"buffer_info"*:

  - ***"frame_id"*** —

    Linearly increasing image counter transmitted
    by the device alongside the image data. Inconsistencies in the counter
    sequence indicate lost buffers.
  - ***"is_incomplete"*** —

    Completeness status of the acquired data.
    Incomplete data might indicate data transmission problems.

    List of values:
     *0* (complete), *1* (incomplete).
  - ***"timestamp_ns"*** —

    Timestamp [ns] of the image transmitted by
    the device alongside the image data. It reflects the value of the
    devices internal clock at the moment of exposure.
- In the sub-dictionary *"chunk_data"*:

  If supported and activated on the device side, GenICam chunk data
  received alongside the image is returned here. This mechanism
  is usually controlled by the device parameters *"ChunkModeActive"*,
  *"ChunkSelector"*, and *"ChunkEnable"*.

  In some cases it is not possible to return all chunk-related values
  via this output dictionary. For example, chunks that either select
  or are selected by others are not returned here.
  Therefore it is also possible to query the chunk values with
  [`get_image_source_param`](get_image_source_param.md) directly.

The device and a corresponding stream defined in
*`image_source_handle`* need to be connected and started
when calling `fetch_from_image_source`.
See [`connect_image_source`](connect_image_source.md) on how to connect and
[`start_image_source`](start_image_source.md) on how to start your image source.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`images`** (output_object)  image(-array) `→` HObject (byte / int1 / int2 / uint2 / int4 / int8 / real)

Retrieved images.

**`image_source_handle`** (input_control)  image_source `→` HHandle

Handle of the image source whose buffer queue should
be accessed.

**`data`** (output_control)  dict `→` HHandle

Meta information about the images.

## Result

If the parameter values are correct, `fetch_from_image_source`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`start_image_source`

## Possible Successors

`stop_image_source`

## Module

Foundation
