# StartImageSource (Operator)

## Name

`StartImageSource` — Prepare the image source for continuously acquiring, transmitting and
receiving images.

## Signature

`static void HOperatorSet.StartImageSource(HTuple imageSourceHandle, HTuple genParamName, HTuple genParamValue)`

`void HImageSource.StartImageSource(HTuple genParamName, HTuple genParamValue)`

## Description

`StartImageSource` prepares the image source device defined in
the handle *`imageSourceHandle`* for continuously acquiring,
transmitting and receiving images. These preparations include, e.g.,
allocating memory, starting the receiver and finally starting
the sending device.
If the image source has been started successfully, the status parameter
*"stream_state"* changes from *"initialized"* to
*"running"*.

As soon as the stream has been started images are continuously
acquired and stored in the receivers image buffer queue,
assuming the device is in a free running configuration.
Images can be retrieved from the buffer queue with
[`FetchFromImageSource`](fetch_from_image_source.md). See *"num_buffers"* in
[`GetImageSourceParam`](get_image_source_param.md) on how to adapt the buffer queue capacity.

The device and a corresponding stream defined in
*`imageSourceHandle`* need to be connected when calling
`StartImageSource`.
See [`ConnectImageSource`](connect_image_source.md) on how to connect your image source.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

Currently, no generic parameters *`genParamName`* and
*`genParamValue`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageSourceHandle`** (input_control)  image_source `→` [HImageSource](HImageSource.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the image source to start the stream.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic parameter name.

Default:
[]

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Generic parameter value.

Default:
[]

## Result

If the parameter values are correct, `StartImageSource`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`ConnectImageSource`,
`SetImageSourceParam`

## Possible Successors

`FetchFromImageSource`,
`StopImageSource`

## See also

`StopImageSource`

## Module

Foundation
