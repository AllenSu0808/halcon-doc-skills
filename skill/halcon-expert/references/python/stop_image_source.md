# stop_image_source (Operator)

## Name

`stop_image_source` — Stop the continuous acquisition, transmission and reception of images
of the image source.

## Signature

`def stop_image_source(image_source_handle: HHandle, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> None`

## Description

`stop_image_source` stops the continuous acquisition, transmission
and reception of images of the image source device
defined in the handle *`image_source_handle`*. It withdraws the
preparations performed by [`start_image_source`](start_image_source.md).
The status parameter *"stream_state"* changes from
*"running"* to *"initialized"*.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

`stop_image_source` can be used from another thread to abort a
blocking call of [`fetch_from_image_source`](fetch_from_image_source.md).

Currently, no generic parameters *`gen_param_name`* and
*`gen_param_value`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_source_handle`** (input_control)  image_source `→` HHandle

Handle of the image source to stop the stream.

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic parameter name.

Default:
[]

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Generic parameter value.

Default:
[]

## Result

If the parameter values are correct, `stop_image_source`
returns the value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`start_image_source`,
`fetch_from_image_source`

## Possible Successors

`disconnect_image_source`

## See also

`start_image_source`

## Module

Foundation
