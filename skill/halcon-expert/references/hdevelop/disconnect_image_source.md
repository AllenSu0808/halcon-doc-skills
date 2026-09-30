# disconnect_image_source (Operator)

## Name

`disconnect_image_source` — Disconnect an image source.

## Signature

`disconnect_image_source( : : ImageSourceHandle, GenParamName, GenParamValue : )`

## Description

`disconnect_image_source` closes the connection to the image source
module specified in *`ImageSourceHandle`*.
After the call, the handle *`ImageSourceHandle`* is in an unconnected
state.

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

Image source handle to be disconnected.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic parameter name.

Default:
[]

**`GenParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

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
