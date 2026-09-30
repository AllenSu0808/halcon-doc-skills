# MeanSp (Operator)

## Name

`MeanSp` — Suppress salt and pepper noise.

## Signature

`static void HOperatorSet.MeanSp(HObject image, out HObject imageSPMean, HTuple maskWidth, HTuple maskHeight, HTuple minThresh, HTuple maxThresh)`

`HImage HImage.MeanSp(int maskWidth, int maskHeight, int minThresh, int maxThresh)`

## Description

The operator `MeanSp` carries out a smoothing by
averaging the values. Only the gray values within the interval from
*`minThresh`* to *`maxThresh`* are averaged. Gray
values which are too light or too dark are ignored during summation.
If no gray value lies within the default interval during summation
the original gray value is adopted. If the thresholds are set at
*0* or *255*, respectively, the operator
`MeanSp` behaves like [`MeanImage`](mean_image.md) except for the
running time.

The operator `MeanSp` is used to suppress extreme gray
values (salt and pepper noise = white and black dots).

For an explanation of the concept of smoothing filters see the introduction
of chapter [Filters / Smoothing](toc_filters_smoothing.md).

## Attention

If even values instead of odd values are given for
*`maskHeight`* or *`maskWidth`*, the routine uses the
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Input image.

**`imageSPMean`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Smoothed image.

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9, 11

Value range:
`maskWidth` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth) && MaskWidth < width(Image) * 2`

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9, 11

Value range:
`maskHeight` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskHeight) && MaskHeight < height(Image) * 2`

**`minThresh`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum gray value.

Default:
1

Suggested values:
1, 5, 7, 9, 11, 15, 23, 31, 43, 61, 101

Value range:
`0
≤
minThresh`

**`maxThresh`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Maximum gray value.

Default:
254

Suggested values:
5, 7, 9, 11, 15, 23, 31, 43, 61, 101, 200, 230, 250, 254

Restriction:
`MinThresh <= MaxThresh`

## Example (HDevelop)

```
read_image(Image,'mreut')
dev_display(Image)
mean_sp(Image,ImageMeansp,3,3,101,201)
dev_display(ImageMeansp)
```

## Possible Successors

`DispImage`

## Alternatives

`MeanImage`,
`MedianImage`,
`MedianSeparate`,
`EliminateMinMax`

## See also

`AnisotropicDiffusion`,
`SigmaImage`,
`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`EliminateMinMax`

## Module

Foundation
