# connect_image_source (Operator)

## Name

`connect_image_source` — Connect to an image source.

## Signature

`def connect_image_source(image_source_handle: HHandle, gen_param_name: Sequence[str], gen_param_value: Sequence[Union[int, float, str]]) -> None`

## Description

`connect_image_source` connects to the image source modules
(device, plugin, etc.) specified in *`image_source_handle`*.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

When calling `connect_image_source` with an image source handle
containing invalid identifiers, an error is thrown.

Currently, no generic parameters *`gen_param_name`* and
*`gen_param_value`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_source_handle`** (input_control)  image_source `→` HHandle

Image source handle to be connected.

**`gen_param_name`** (input_control)  attribute.name-array `→` Sequence[str]

Generic parameter name.

Default:
[]

**`gen_param_value`** (input_control)  attribute.value-array `→` Sequence[Union[int, float, str]]

Generic parameter value.

Default:
[]

## Result

If the parameter values are correct and the desired image source modules
could be connected, `connect_image_source` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`query_image_sources`,
`create_image_source`

## Possible Successors

`get_image_source_param`,
`set_image_source_param`,
`start_image_source`

## See also

`disconnect_image_source`

## Module

Foundation
