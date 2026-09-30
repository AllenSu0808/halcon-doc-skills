# connect_image_source (Operator)

## Name

`connect_image_source` — Connect to an image source.

## Signature

`connect_image_source( : : ImageSourceHandle, GenParamName, GenParamValue : )`

## Description

`connect_image_source` connects to the image source modules
(device, plugin, etc.) specified in *`ImageSourceHandle`*.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

When calling `connect_image_source` with an image source handle
containing invalid identifiers, an error is thrown.

Currently, no generic parameters *`GenParamName`* and
*`GenParamValue`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageSourceHandle`** (input_control)  image_source `→`  (handle)

Image source handle to be connected.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic parameter name.

Default:
[]

**`GenParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

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
