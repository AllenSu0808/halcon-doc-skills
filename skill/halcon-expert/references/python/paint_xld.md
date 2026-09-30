# paint_xld (Operator)

## Name

`paint_xld` — Paint XLD objects into an image.

## Signature

`def paint_xld(xld: HObject, image: HObject, grayval: MaybeSequence[Union[int, float]]) -> HObject`

## Description

`paint_xld` paints the XLD objects *`xld`* of type contour or
polygon with the constant gray values *`grayval`* into each channel
of the background image given in *`image`* and returns the result in
*`image_result`*. Open contours of XLD
objects are closed and their enclosed regions are filled up. The rim of
the subpixel XLD objects is painted onto the background image using
anti-aliasing.

Filling up XLD-objects that have crossings does not work correctly and
leads to artifacts.
The [`set_system`](set_system.md) parameter *"neighborhood"* defines whether
diagonal neighbors are filled as well as orthogonal neighbors.

*`grayval`* contains the gray values for painting the XLD objects. These
gray values can either be specified for each channel once, valid for all XLD
objects, or for each XLD object separately. To define the latter, group the
channel gray values g of each XLD object and concatenate them to
a tuple according to the order of the XLD objects, e.g., for a three channel
image:

[g(channel1,xld1), g(channel2,xld1), g(channel3,xld1), g(channel1,xld2), ... ].
If the input image is of type `direction`, gray values that are not
in the value range that is valid for `direction` images are set to
the value 255 to mark them as invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`xld`** (input_object)  xld(-array) `→` HObject

XLD objects to be painted into the input image.

**`image`** (input_object)  (multichannel-)image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Image in which the xld objects are to be painted.

**`image_result`** (output_object)  image `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / real / complex)

Image containing the result.

**`grayval`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Desired gray value of the xld object.

Default:
255.0

Suggested values:
0.0, 1.0, 2.0, 5.0, 10.0, 16.0, 32.0, 64.0, 128.0, 253.0, 254.0, 255.0

## Result

`paint_xld` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. If the input is empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`.
If necessary, an exception is raised.

## Possible Predecessors

`read_image`,
`gen_image_const`,
`gen_image_proto`,
`gen_contour_polygon_xld`,
`threshold_sub_pix`

## Alternatives

`set_grayval`,
`paint_gray`,
`paint_region`

## See also

`gen_image_const`

## Module

Foundation
