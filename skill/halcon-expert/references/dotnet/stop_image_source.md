# StopImageSource (Operator)

## Name

`StopImageSource` — Stop the continuous acquisition, transmission and reception of images
of the image source.

## Signature

`static void HOperatorSet.StopImageSource(HTuple imageSourceHandle, HTuple genParamName, HTuple genParamValue)`

`void HImageSource.StopImageSource(HTuple genParamName, HTuple genParamValue)`

## Description

`StopImageSource` stops the continuous acquisition, transmission
and reception of images of the image source device
defined in the handle *`imageSourceHandle`*. It withdraws the
preparations performed by [`StartImageSource`](start_image_source.md).
The status parameter *"stream_state"* changes from
*"running"* to *"initialized"*.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

`StopImageSource` can be used from another thread to abort a
blocking call of [`FetchFromImageSource`](fetch_from_image_source.md).

Currently, no generic parameters *`genParamName`* and
*`genParamValue`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageSourceHandle`** (input_control)  image_source `→` [HImageSource](HImageSource.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the image source to stop the stream.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic parameter name.

Default:
[]

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Generic parameter value.

Default:
[]

## Result

If the parameter values are correct, `StopImageSource`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`StartImageSource`,
`FetchFromImageSource`

## Possible Successors

`DisconnectImageSource`

## See also

`StartImageSource`

## Module

Foundation
