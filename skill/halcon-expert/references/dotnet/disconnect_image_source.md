# DisconnectImageSource (Operator)

## Name

`DisconnectImageSource` — Disconnect an image source.

## Signature

`static void HOperatorSet.DisconnectImageSource(HTuple imageSourceHandle, HTuple genParamName, HTuple genParamValue)`

`void HImageSource.DisconnectImageSource(HTuple genParamName, HTuple genParamValue)`

## Description

`DisconnectImageSource` closes the connection to the image source
module specified in *`imageSourceHandle`*.
After the call, the handle *`imageSourceHandle`* is in an unconnected
state.

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

Image source handle to be disconnected.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic parameter name.

Default:
[]

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Generic parameter value.

Default:
[]

## Result

If the parameter values are correct and the desired image source
could be disconnected, `DisconnectImageSource` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`StopImageSource`,
`ConnectImageSource`

## See also

`ConnectImageSource`

## Module

Foundation
