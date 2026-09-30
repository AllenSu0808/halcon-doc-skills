# mean_sp (Operator)

## Name

`mean_sp` — Suppress salt and pepper noise.

## Signature

`def mean_sp(image: HObject, mask_width: int, mask_height: int, min_thresh: int, max_thresh: int) -> HObject`

## Description

The operator `mean_sp` carries out a smoothing by
averaging the values. Only the gray values within the interval from
*`min_thresh`* to *`max_thresh`* are averaged. Gray
values which are too light or too dark are ignored during summation.
If no gray value lies within the default interval during summation
the original gray value is adopted. If the thresholds are set at
*0* or *255*, respectively, the operator
`mean_sp` behaves like [`mean_image`](mean_image.md) except for the
running time.

The operator `mean_sp` is used to suppress extreme gray
values (salt and pepper noise = white and black dots).

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

**`image_spmean`** (output_object)  (multichannel-)image(-array) `→` HObject (byte / uint2)

Smoothed image.

**`mask_width`** (input_control)  extent.x `→` int

Width of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9, 11

Value range:
`mask_width` (lin)

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
`mask_height` (lin)

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

Value range:
`0
≤
min_thresh`

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

`mean_image`,
`median_image`,
`median_separate`,
`eliminate_min_max`

## See also

`anisotropic_diffusion`,
`sigma_image`,
`binomial_filter`,
`gauss_filter`,
`smooth_image`,
`eliminate_min_max`

## Module

Foundation
