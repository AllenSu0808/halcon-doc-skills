# stop_image_source (Operator)

## Name

`stop_image_source` — Stop the continuous acquisition, transmission and reception of images
of the image source.

## Signature

`stop_image_source( : : ImageSourceHandle, GenParamName, GenParamValue : )`

## Description

`stop_image_source` stops the continuous acquisition, transmission
and reception of images of the image source device
defined in the handle *`ImageSourceHandle`*. It withdraws the
preparations performed by [`start_image_source`](start_image_source.md).
The status parameter *'stream_state'* changes from
*'running'* to *'initialized'*.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

`stop_image_source` can be used from another thread to abort a
blocking call of [`fetch_from_image_source`](fetch_from_image_source.md).

Currently, no generic parameters *`GenParamName`* and
*`GenParamValue`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ImageSourceHandle`** (input_control)  image_source `→`  (handle)

Handle of the image source to stop the stream.

**`GenParamName`** (input_control)  attribute.name-array `→`  (string)

Generic parameter name.

Default:
[]

**`GenParamValue`** (input_control)  attribute.value-array `→`  (integer / real / string)

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
