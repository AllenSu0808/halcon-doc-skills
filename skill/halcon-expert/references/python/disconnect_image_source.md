# disconnect_image_source (Operator)

## Name

`disconnect_image_source` — Disconnect an image source.

## Signature

`def disconnect_image_source(image_source_handle: HHandle, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> None`

## Description

`disconnect_image_source` closes the connection to the image source
module specified in *`image_source_handle`*.
After the call, the handle *`image_source_handle`* is in an unconnected
state.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

Currently, no generic parameters *`gen_param_name`* and
*`gen_param_value`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_source_handle`** (input_control)  image_source `→` HHandle

Image source handle to be disconnected.

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic parameter name.

Default:
[]

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Generic parameter value.

Default:
[]

## Result

If the parameter values are correct and the desired image source
could be disconnected, `disconnect_image_source` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`stop_image_source`,
`connect_image_source`

## See also

`connect_image_source`

## Module

Foundation
