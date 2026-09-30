# GetFramegrabberParam (Operator)

## Name

`GetFramegrabberParam` — Query specific parameters of an image acquisition device.

## Signature

`static void HOperatorSet.GetFramegrabberParam(HTuple acqHandle, HTuple param, out HTuple value)`

`HTuple HFramegrabber.GetFramegrabberParam(HTuple param)`

`HTuple HFramegrabber.GetFramegrabberParam(string param)`

## Description

The operator `GetFramegrabberParam` returns specific parameter
values for the image acquisition device specified by *`acqHandle`*. The
standard parameters listed below are available for all image acquisition
devices. Additional parameters may be supported by a specific image
acquisition device. A list of those parameters can be obtained with the
query *"parameter"* via [`InfoFramegrabber`](info_framegrabber.md).

Standard values for *`param`*, see [`OpenFramegrabber`](open_framegrabber.md):

- ***"name"*** —

  Name of the image acquisition interface.
- ***"horizontal_resolution"*** —

  Horizontal resolution of the image acquisition device.
- ***"vertical_resolution"*** —

  Vertical resolution of the image acquisition device.
- ***"image_width"*** —

  Width of the specified image part.
- ***"image_height"*** —

  Height of the specified image part.
- ***"start_row"*** —

  Row coordinate of upper left corner of specified image part.
- ***"start_column"*** —

  Column coordinate of upper left corner of specified image part.
- ***"field"*** —

  Selected video field or full frame.
- ***"bits_per_channel"*** —

  Number of transferred bits per pixel and image channel.
- ***"color_space"*** —

  Color space of resulting image.
- ***"generic"*** —

  Generic value with device-specific meaning.
- ***"external_trigger"*** —

  External triggering (*"true"*/ *"false"*).
- ***"camera_type"*** —

  Type of used camera (interface-specific).
- ***"device"*** —

  Device name of the image acquisition device.
- ***"port"*** —

  Port the image acquisition device is connected to.
- ***"line_in"*** —

  Camera input line of multiplexer (optional).

## Attention

For a multithreaded application,
[`InfoFramegrabber`](info_framegrabber.md), [`OpenFramegrabber`](open_framegrabber.md), and
[`CloseFramegrabber`](close_framegrabber.md) are executed exclusively.

`GetFramegrabberParam` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`acqHandle`** (input_control)  framegrabber `→` [HFramegrabber](HFramegrabber.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the acquisition device to be used.

**`param`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Parameter of interest.

Default:
"revision"

Suggested values:
"bits_per_channel", "camera_type", "color_space", "continuous_grabbing", "device", "external_trigger", "field", "generic", "grab_timeout", "horizontal_resolution", "image_available", "image_height", "image_width", "line_in", "name", "port", "revision", "start_column", "start_row", "vertical_resolution", "volatile"

**`value`** (output_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long / HHandle)

Parameter value.

## Result

If the image acquisition device is open and the specified parameter
is supported, the operator `GetFramegrabberParam` returns the
value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`OpenFramegrabber`,
`SetFramegrabberParam`

## Possible Successors

`GrabImage`,
`GrabData`,
`GrabImageStart`,
`GrabImageAsync`,
`GrabDataAsync`,
`SetFramegrabberParam`,
`CloseFramegrabber`

## See also

`OpenFramegrabber`,
`InfoFramegrabber`,
`SetFramegrabberParam`

## Module

Foundation
