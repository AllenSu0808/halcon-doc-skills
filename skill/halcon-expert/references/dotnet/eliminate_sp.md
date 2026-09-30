# EliminateSp (Operator)

## Name

`EliminateSp` — Replace values outside of thresholds with average value.

## Signature

`static void HOperatorSet.EliminateSp(HObject image, out HObject imageFillSP, HTuple maskWidth, HTuple maskHeight, HTuple minThresh, HTuple maxThresh)`

`HImage HImage.EliminateSp(int maskWidth, int maskHeight, int minThresh, int maxThresh)`

## Description

The operator `EliminateSp` replaces all gray values outside
the indicated gray value intervals (*`minThresh`* to
*`maxThresh`*) with the neighboring mean values. Only those
neighboring pixels which also fall within the gray value interval
are used for averaging. If no such pixel is present in the vicinity
the original gray value is used. The gray values in the input image
falling within the gray value interval are also adopted without
change.

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

**`imageFillSP`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / uint2)

Smoothed image.

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of filter mask.

Default:
3

Suggested values:
3, 5, 7, 9, 11

Value range:
`3
≤
maskWidth` (lin)

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
`3
≤
maskHeight` (lin)

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
eliminate_sp(Image,ImageFillSP,3,3,101,201)
dev_display(ImageFillSP)
```

## Possible Successors

`DispImage`

## Alternatives

`MeanSp`,
`MeanImage`,
`MedianImage`,
`EliminateMinMax`

## See also

`BinomialFilter`,
`GaussFilter`,
`SmoothImage`,
`AnisotropicDiffusion`,
`SigmaImage`,
`EliminateMinMax`

## Module

Foundation
