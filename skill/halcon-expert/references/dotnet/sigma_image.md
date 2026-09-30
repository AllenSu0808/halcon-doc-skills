# SigmaImage (Operator)

## Name

`SigmaImage` — Non-linear smoothing with the sigma filter.

## Signature

`static void HOperatorSet.SigmaImage(HObject image, out HObject imageSigma, HTuple maskHeight, HTuple maskWidth, HTuple sigma)`

`HImage HImage.SigmaImage(int maskHeight, int maskWidth, int sigma)`

## Description

The operator `SigmaImage` carries out a non-linear smoothing
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
*`maskHeight`* or *`maskWidth`*, the routine uses the next
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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / cyclic / int1 / int2 / uint2 / int4 / real)

Image to be smoothed.

**`imageSigma`** (output_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / cyclic / int1 / int2 / uint2 / int4 / real)

Smoothed image.

**`maskHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Height of the mask (number of lines).

Default:
5

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
maskHeight`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskHeight)`

**`maskWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Width of the mask (number of columns).

Default:
5

Suggested values:
3, 5, 7, 9, 11, 13, 15

Value range:
`3
≤
maskWidth`

Minimum increment:
2

Recommended increment:
2

Restriction:
`odd(MaskWidth)`

**`sigma`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

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

## Example (HDevelop)

```
read_image(Image,'fabrik')
sigma_image(Image,ImageSigma,5,5,3)
dev_display(ImageSigma)
```

## Complexity

For each pixel: O(MaskHeight*MaskWidth).

## Result

If the parameter values are correct the operator `SigmaImage`
returns the value 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no
input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`ReadImage`

## Possible Successors

`Threshold`,
`DynThreshold`,
`Regiongrowing`

## Alternatives

`AnisotropicDiffusion`,
`RankImage`

## See also

`SmoothImage`,
`BinomialFilter`,
`GaussFilter`,
`MeanImage`

## References

R. Haralick, L. Shapiro; “Computer and Robot Vision”;
Addison-Wesley, 1992, Seite 325

## Module

Foundation
