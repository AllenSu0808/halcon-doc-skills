# start_image_source (Operator)

## Name

`start_image_source` — Prepare the image source for continuously acquiring, transmitting and
receiving images.

## Signature

`start_image_source( : : ImageSourceHandle, GenParamName, GenParamValue : )`

## Description

`start_image_source` prepares the image source device defined in
the handle *`ImageSourceHandle`* for continuously acquiring,
transmitting and receiving images. These preparations include, e.g.,
allocating memory, starting the receiver and finally starting
the sending device.
If the image source has been started successfully, the status parameter
*'stream_state'* changes from *'initialized'* to
*'running'*.

As soon as the stream has been started images are continuously
acquired and stored in the receivers image buffer queue,
assuming the device is in a free running configuration.
Images can be retrieved from the buffer queue with
[`fetch_from_image_source`](fetch_from_image_source.md). See *'num_buffers'* in
[`get_image_source_param`](get_image_source_param.md) on how to adapt the buffer queue capacity.

The device and a corresponding stream defined in
*`ImageSourceHandle`* need to be connected when calling
`start_image_source`.
See [`connect_image_source`](connect_image_source.md) on how to connect your image source.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

Currently, no generic parameters *`GenParamName`* and
*`GenParamValue`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageSourceHandle`** (input_control)  image_source `→`  (handle)

Handle of the image source to start the stream.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic parameter name.

Default:
[]

**`GenParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

Generic parameter value.

Default:
[]

## Result

If the parameter values are correct, `start_image_source`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`connect_image_source`,
`set_image_source_param`

## Possible Successors

`fetch_from_image_source`,
`stop_image_source`

## See also

`stop_image_source`

## Module

Foundation
