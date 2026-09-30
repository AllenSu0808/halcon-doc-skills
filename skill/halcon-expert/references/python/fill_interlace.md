# fill_interlace (Operator)

## Name

`fill_interlace` — Interpolate 2 video half images.

## Signature

`def fill_interlace(image_camera: HObject, mode: str) -> HObject`

## Description

The operator `fill_interlace` calculates an interpolated
full image or removes odd/even lines
from a video image composed of two half images. If an
image is recorded with a video camera it consists of two half images
recorded at different times but stored in one image in the digital
form. This can lead to several errors in further processing. In
order to reduce these errors the video image is modified. Every
second line is re-calculated or removed. The parameter *`mode`*
determines whether this must be done for even (*"even"*,
*"rmeven"*) or odd (*"odd"*, *"rmodd"*) line numbers.
If you choose *"even"* or *"odd"* the gray values
in the generated lines are calculated as mean values
from the direct neighbors above or below the current pixel,
respectively. If you choose *"rmeven"* or *"rmodd"* the even or
odd lines numbers are removed (in that case the resulting image
is only half as high as the input image).
The value *"switch"* for *`mode`* cause the odd and even lines
to be exchanged.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

Note that filter operators may return unexpected results if
an image with a reduced domain is used as input. Please refer to the
chapter [Filters](toc_filters.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on channel level.
- Automatically parallelized on domain level.

## Parameters

**`image_camera`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Gray image consisting of two half images.

**`image_filled`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Full image with interpolated/removed lines.

**`mode`** (input_control)  string `→` str

Instruction whether even or odd lines should
be replaced/removed.

Default:
"odd"

List of values:
"even", "odd", "rmeven", "rmodd", "switch"

## Complexity

For each pixel: O(2).

## Result

If the parameter values are correct the operator
`fill_interlace` returns the value 2 (
H_MSG_TRUE)
. The behavior
in case of empty input (no input images available) is set via the
operator `set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`,
`grab_image`

## Possible Successors

`sobel_amp`,
`edges_image`,
`regiongrowing`,
`diff_of_gauss`,
`threshold`,
`dyn_threshold`,
`auto_threshold`,
`mean_image`,
`binomial_filter`,
`gauss_filter`,
`anisotropic_diffusion`,
`sigma_image`,
`median_image`

## See also

`median_image`,
`binomial_filter`,
`gauss_filter`,
`crop_part`

## Module

Foundation
