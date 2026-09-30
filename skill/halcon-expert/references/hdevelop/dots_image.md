# dots_image (Operator)

## Name

`dots_image` — Enhance circular dots in an image.

## Signature

`dots_image(Image : DotImage : Diameter, FilterType, PixelShift : )`

## Description

`dots_image` enhances circular dots of diameter
*`Diameter`* in the input image *`Image`*. Hence,
`dots_image` is especially suited for the segmentation of dot
prints, e.g., in OCR applications. The enhancement is performed by
using matched filters with filter masks that are tuned for a
particular dot size. For example, for *`Diameter`* = 5 the
filter mask is given by:
$$\frac{1}{336}$$ ![figure](../assets/1c113e0d605010a2.svg)
The parameter *`FilterType`* selects whether *'dark'*,
*'light'*, or *'all'* dots in the image should be
enhanced. The *`PixelShift`* can be used either to increase
the contrast of the output image (*`PixelShift`* > 0) or to
dampen the values in extremely bright areas that would be cut off
otherwise (*`PixelShift`* = -1).

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

**`Image`** (input_object)  (multichannel-)image(-array) `→` object (byte / uint2)

Input image.

**`DotImage`** (output_object)  (multichannel-)image(-array) `→` object (byte / uint2)

Output image.

**`Diameter`** (input_control)  integer `→`  (integer)

Diameter of the dots to be enhanced.

Default:
5

List of values:
3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23

**`FilterType`** (input_control)  string `→`  (string)

Enhance dark, light, or all dots.

Default:
'light'

List of values:
'all', 'dark', 'light'

**`PixelShift`** (input_control)  integer `→`  (integer)

Shift of the filter response.

Default:
0

List of values:
-1, 0, 1, 2

## Possible Successors

`threshold`

## Alternatives

`laplace`,
`laplace_of_gauss`,
`diff_of_gauss`,
`derivate_gauss`,
`convol_image`

## Module

Foundation
