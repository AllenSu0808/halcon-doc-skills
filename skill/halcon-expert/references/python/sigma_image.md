# sigma_image (Operator)

## Name

`sigma_image` — Non-linear smoothing with the sigma filter.

## Signature

`def sigma_image(image: HObject, mask_height: int, mask_width: int, sigma: int) -> HObject`

## Description

The operator `sigma_image` carries out a non-linear smoothing
of the gray values of all input images (*`image`*). All
pixels in a rectangular window (MaskHeight x
MaskWidth) are used to determine
the new gray value of the central pixel of this window.
First, the gray value standard deviation
of all pixels in the window is calculated. Then, all pixels of the
window with a gray value that differs from the gray value of the
central pixel by less than *`sigma`* times this standard
deviation are used to calculate the new gray value of the central
pixel. The gray value of the central pixel is the average of the
gray values of the selected pixels. If no pixel could be selected
for the averaging of the gray values, the gray value of the central
pixel remains unchanged.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

If even values instead of odd values are given for
*`mask_height`* or *`mask_width`*, the routine uses the next
larger odd values instead (this way the center of the filter mask is
always explicitly determined).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / cyclic / int1 / int2 / uint2 / int4 / real)

Image to be smoothed.

**`image_sigma`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / cyclic / int1 / int2 / uint2 / int4 / real)

Smoothed image.

**`mask_height`** (input_control)  extent.y `→` int

Height of the mask (number of lines).

Default:
5

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
mask_height`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskHeight)`

**`mask_width`** (input_control)  extent.x `→` int

Width of the mask (number of columns).

Default:
5

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
mask_width`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth)`

**`sigma`** (input_control)  integer `→` int

Max. deviation to the average.

Default:
3

Suggested values:
3, 5, 7, 9, 11, 20, 30, 50

Value range:
`0
≤
sigma`

Minimum increment:
1

Recommended increment:
2

## Complexity

For each pixel: O(MaskHeight*MaskWidth).

## Result

If the parameter values are correct the operator `sigma_image`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`threshold`,
`dyn_threshold`,
`regiongrowing`

## Alternatives

`anisotropic_diffusion`,
`rank_image`

## See also

`smooth_image`,
`binomial_filter`,
`gauss_filter`,
`mean_image`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, Seite 325

## Module

Foundation
