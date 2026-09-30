# eliminate_sp (Operator)

## Name

`eliminate_sp` — Replace values outside of thresholds with average value.

## Signature

`def eliminate_sp(image: HObject, mask_width: int, mask_height: int, min_thresh: int, max_thresh: int) -> HObject`

## Description

The operator `eliminate_sp` replaces all gray values outside
the indicated gray value intervals (*`min_thresh`* to
*`max_thresh`*) with the neighboring mean values. Only those
neighboring pixels which also fall within the gray value interval
are used for averaging. If no such pixel is present in the vicinity
the original gray value is used. The gray values in the input image
falling within the gray value interval are also adopted without
change.

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

If even values instead of odd values are given for
*`mask_height`* or *`mask_width`*, the routine uses the
next larger odd values instead (this way the center of the filter
mask is always explicitly determined).

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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Input image.

**`image_fill_sp`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Smoothed image.

**`mask_width`** (input_control)  extent.x `→` int

Width of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9, 11

Value range:
`3
≤
mask_width` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth) && MaskWidth < width(Image) * 2`

**`mask_height`** (input_control)  extent.y `→` int

Height of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9, 11

Value range:
`3
≤
mask_height` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskHeight) && MaskHeight < height(Image) * 2`

**`min_thresh`** (input_control)  integer `→` int

Minimum gray value.

Default:
1

Suggested values:
1, 5, 7, 9, 11, 15, 23, 31, 43, 61, 101

**`max_thresh`** (input_control)  integer `→` int

Maximum gray value.

Default:
254

Suggested values:
5, 7, 9, 11, 15, 23, 31, 43, 61, 101, 200, 230, 250, 254

Restriction:
`MinThresh <= MaxThresh`

## Possible Successors

`disp_image`

## Alternatives

`mean_sp`,
`mean_image`,
`median_image`,
`eliminate_min_max`

## See also

`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`anisotropic_diffusion`,
`sigma_image`,
`eliminate_min_max`

## Module

Foundation
