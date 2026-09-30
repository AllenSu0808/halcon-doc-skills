# DualRank (Operator)

## Name

`DualRank` — Opening, Median and Closing with circle or rectangle mask.

## Signature

`static void HOperatorSet.DualRank(HObject image, out HObject imageRank, HTuple maskType, HTuple radius, HTuple modePercent, HTuple margin)`

`HImage HImage.DualRank(string maskType, int radius, int modePercent, HTuple margin)`

`HImage HImage.DualRank(string maskType, int radius, int modePercent, string margin)`

## Description

The operator `DualRank` carries out a non-linear
transformation of the gray values of all input images
(*`image`*). Circles or squares can be used as structuring
elements. The operator `DualRank` effects two
consecutive calls of [`RankImage`](rank_image.md). At the first call the
range gray value is calculated with the indicated range
(*`modePercent`*). The result of this calculation is the
input of a further call of [`RankImage`](rank_image.md), this time using the
range value 100-*`modePercent`*.

When filtering different parameters for border treatment
(*`margin`*) can be chosen:

- **gray value** —

  Pixels outside of the image border are assumed to be
  constant (with the indicated gray value).
- ***"continued"*** —

  Continuation of the gray values at the image
  border.
- ***"cyclic"*** —

  Cyclic continuation at the image borders.
- ***"mirrored"*** —

  Reflection of pixels at the image borders.

A range filtering is calculated according to the following scheme:
The indicated mask is put over the image to be filtered in such a
way that the center of the mask touches all pixels once. For each
of these pixels all neighboring pixels covered by the mask are
sorted in an ascending sequence corresponding to their gray values.
Each sorted sequence of gray values contains the same number of gray
values like the mask has image points. The n-th highest element, (=
*`modePercent`*, rank values between 0...100 in
percent) is selected and set as result gray value in the
corresponding result image.

If *`modePercent`* is 0, then the operator equals to the
gray value opening ([`GrayOpening`](gray_opening.md)). If
*`modePercent`* is 50, the operator results in the median
filter, which is applied twice ([`MedianImage`](median_image.md)). The
*`modePercent`* 100 in `DualRank` means that it
calculates the gray value closing ([`GrayClosing`](gray_closing.md)).
Choosing parameter values inside this range results in a smooth
transformation of these operators.

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

**`image`** (input_object)  (multichannel-)image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Image to be filtered.

**`imageRank`** (output_object)  multichannel-image(-array) `→` [HImage](HImage.md) (byte / int2 / uint2 / int4 / real)

Filtered Image.

**`maskType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Shape of the mask.

Default:
"circle"

List of values:
"circle", "square"

**`radius`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Radius of the filter mask.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 15, 19, 25, 31, 39, 47, 59

Value range:
`1
≤
radius
≤
101`

Minimum increment:
1

Recommended increment:
2

**`modePercent`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Filter Mode: 0 corresponds to a gray value
opening , 50 corresponds to a median and 100 to
a gray values closing.

Default:
10

Suggested values:
0, 2, 5, 10, 15, 20, 40, 50, 60, 80, 85, 90, 95, 98, 100

Value range:
`0
≤
modePercent
≤
100`

Minimum increment:
1

Recommended increment:
2

**`margin`** (input_control)  string `→` [HTuple](HTuple.md) (*string* / int / long / double)

Border treatment.

Default:
"mirrored"

Suggested values:
"mirrored", "cyclic", "continued", 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Example (HDevelop)

```
read_image(Image,'fabrik')
dual_rank(Image,ImageOpening,'circle',10,10,'mirrored')
dev_display(ImageOpening)
```

## Complexity

For each pixel: $O(\sqrt{F} * 10)$ ![figure](../assets/e01c151d4d521f8b.svg) with F =
area of the structuring element.

## Result

If the parameter values are correct the operator
`DualRank` returns the value 2 (
H_MSG_TRUE)
. The behavior in case
of empty input (no input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`ReadImage`

## Possible Successors

`Threshold`,
`DynThreshold`,
`SubImage`,
`Regiongrowing`

## Alternatives

`RankImage`,
`GrayClosing`,
`GrayOpening`,
`MedianImage`

## See also

`GenCircle`,
`GenRectangle1`,
`GrayErosionRect`,
`GrayDilationRect`,
`SigmaImage`

## References

W. Eckstein, O. Munkelt
“Extracting Objects from Digital Terrain Model”
Remote Sensing and Reconstruction for Threedimensional Objects and Scenes,
SPIE Symposium on Optical Science, Engeneering, and Instrumentation,
July 1995, San Diego

## Module

Foundation
