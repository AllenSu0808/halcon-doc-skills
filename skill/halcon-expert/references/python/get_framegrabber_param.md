# get_framegrabber_param (Operator)

## Name

`get_framegrabber_param` — Query specific parameters of an image acquisition device.

## Signature

`def get_framegrabber_param(acq_handle: HHandle, param: MaybeSequence[str]) -> Sequence[HTupleElementType]`

`def get_framegrabber_param_s(acq_handle: HHandle, param: MaybeSequence[str]) -> HTupleElementType`

## Description

The operator `get_framegrabber_param` returns specific parameter
values for the image acquisition device specified by *`acq_handle`*. The
standard parameters listed below are available for all image acquisition
devices. Additional parameters may be supported by a specific image
acquisition device. A list of those parameters can be obtained with the
query *"parameter"* via [`info_framegrabber`](info_framegrabber.md).

Standard values for *`param`*, see [`open_framegrabber`](open_framegrabber.md):

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
[`info_framegrabber`](info_framegrabber.md), [`open_framegrabber`](open_framegrabber.md), and
[`close_framegrabber`](close_framegrabber.md) are executed exclusively.

`get_framegrabber_param` runs in parallel with all non-exclusive
operators inside and outside of this group.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`acq_handle`** (input_control)  framegrabber `→` HHandle

Handle of the acquisition device to be used.

**`param`** (input_control)  string(-array) `→` MaybeSequence[str]

Parameter of interest.

Default:
"revision"

Suggested values:
"bits_per_channel", "camera_type", "color_space", "continuous_grabbing", "device", "external_trigger", "field", "generic", "grab_timeout", "horizontal_resolution", "image_available", "image_height", "image_width", "line_in", "name", "port", "revision", "start_column", "start_row", "vertical_resolution", "volatile"

**`value`** (output_control)  string(-array) `→` Sequence[HTupleElementType]

Parameter value.

## Result

If the image acquisition device is open and the specified parameter
is supported, the operator `get_framegrabber_param` returns the
value 2 (
H_MSG_TRUE)
. Otherwise an exception is raised.

## Possible Predecessors

`open_framegrabber`,
`set_framegrabber_param`

## Possible Successors

`grab_image`,
`grab_data`,
`grab_image_start`,
`grab_image_async`,
`grab_data_async`,
`set_framegrabber_param`,
`close_framegrabber`

## See also

`open_framegrabber`,
`info_framegrabber`,
`set_framegrabber_param`

## Module

Foundation
