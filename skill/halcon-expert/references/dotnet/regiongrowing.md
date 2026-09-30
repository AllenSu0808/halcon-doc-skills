# Regiongrowing (Operator)

## Name

`Regiongrowing` — Segment an image using region growing.

## Signature

`static void HOperatorSet.Regiongrowing(HObject image, out HObject regions, HTuple rasterHeight, HTuple rasterWidth, HTuple tolerance, HTuple minSize)`

`HRegion HImage.Regiongrowing(int rasterHeight, int rasterWidth, HTuple tolerance, int minSize)`

`HRegion HImage.Regiongrowing(int rasterHeight, int rasterWidth, double tolerance, int minSize)`

## Description

`Regiongrowing` segments images into regions of the same
intensity - rastered into rectangles of size *`rasterHeight`*
$\times$ *`rasterWidth`*. In order to decide
whether two adjacent rectangles belong to the same region only the
gray value of their center points is used. If the gray value
difference is less then or equal to *`tolerance`* the rectangles
are merged into one region.

If $g_{1}$ and $g_{2}$ are two gray values to be examined,
they are merged into the same region if:
$$|g_{1}-g_{2}|<\texttt{Tolerance}$$
For images of type 'cyclic', the following formulas are used:
$$\left|g_1 - g_2\right| < \mathrm{Tolerance} \land \left|g_1 - g_2\right| \le 127 (256 - \left|g_1 - g_2\right| < \mathrm{Tolerance} \land \left|g_1 - g_2\right| > 127$$ ![figure](../assets/19f5adcf99481f99.svg)

For rectangles larger than one pixel, usually the images should be
smoothed with a lowpass filter with a size of at least *`rasterHeight`*
$\times$ *`rasterWidth`* before calling `Regiongrowing`
(so that the gray values at the centers of the rectangles are
“representative” for the whole rectangle).
If the image contains little noise and the rectangles are small, the
smoothing can be omitted in many cases.

The resulting regions are collections of rectangles of the chosen
size *`rasterHeight`* $\times$ *`rasterWidth`*.
Only regions containing at least *`minSize`* points are
returned.

Region growing is a very fast operation, and thus suited for
time-critical applications.

## Attention

*`rasterWidth`* and *`rasterHeight`* are automatically converted to
odd values if necessary.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / int4 / real)

Input image.

**`regions`** (output_object)  region-array `→` [HRegion](HRegion.md)

Segmented regions.

**`rasterHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*int* / long)

Vertical distance between tested pixels (height of the
raster).

Default:
3

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21

Value range:
`1
≤
rasterHeight
≤
99` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`RasterHeight >= 1 && odd(RasterHeight)`

**`rasterWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*int* / long)

Horizontal distance between tested pixels (height of the
raster).

Default:
3

Suggested values:
1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21

Value range:
`1
≤
rasterWidth
≤
99` (lin)

Minimum increment:
2

Recommended increment:
2

Restriction:
`RasterWidth >= 1 && odd(RasterWidth)`

**`tolerance`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Points with a gray value difference less then or equal
to tolerance are accumulated into the same object.

Default:
6.0

Suggested values:
1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 18.0, 25.0

Value range:
`0
≤
tolerance` (lin)

Minimum increment:
0.01

Recommended increment:
1.0

**`minSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Minimum size of the output regions.

Default:
100

Suggested values:
1, 5, 10, 20, 50, 100, 200, 500, 1000

Value range:
`1
≤
minSize`

Minimum increment:
1

Recommended increment:
5

## Example (HDevelop)

```
read_image(Image,'fabrik')
mean_image(Image,Mean,RasterHeight,RasterWidth)
regiongrowing(Mean,Result,RasterHeight,RasterWidth,6.0,100)
```

## Complexity

Let N be the number of found regions and M the number of points
in one of these regions. Then the runtime complexity is
O(N * log(M) * M).

## Result

`Regiongrowing` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`BinomialFilter`,
`MeanImage`,
`GaussFilter`,
`SmoothImage`,
`MedianImage`,
`AnisotropicDiffusion`

## Possible Successors

`SelectShape`,
`ReduceDomain`,
`SelectGray`

## Alternatives

`RegiongrowingN`,
`RegiongrowingMean`,
`LabelToRegion`

## Module

Foundation
