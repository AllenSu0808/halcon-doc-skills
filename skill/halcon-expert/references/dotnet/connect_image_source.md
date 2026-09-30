# ConnectImageSource (Operator)

## Name

`ConnectImageSource` — Connect to an image source.

## Signature

`static void HOperatorSet.ConnectImageSource(HTuple imageSourceHandle, HTuple genParamName, HTuple genParamValue)`

`void HImageSource.ConnectImageSource(HTuple genParamName, HTuple genParamValue)`

## Description

`ConnectImageSource` connects to the image source modules
(device, plugin, etc.) specified in *`imageSourceHandle`*.

For further information about the states of an image source see
[Image Source](toc_imagesource.md).

When calling `ConnectImageSource` with an image source handle
containing invalid identifiers, an error is thrown.

Currently, no generic parameters *`genParamName`* and
*`genParamValue`* are supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`imageSourceHandle`** (input_control)  image_source `→` [HImageSource](HImageSource.md), [HTuple](HTuple.md) (*IntPtr*)

Image source handle to be connected.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Generic parameter name.

Default:
[]

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*int* / long / double / string)

Generic parameter value.

Default:
[]

## Result

If the parameter values are correct and the desired image source modules
could be connected, `ConnectImageSource` returns the value
2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`QueryImageSources`,
`CreateImageSource`

## Possible Successors

`GetImageSourceParam`,
`SetImageSourceParam`,
`StartImageSource`

## See also

`DisconnectImageSource`

## Module

Foundation
