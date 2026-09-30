# MinMaxGray (Operator)

## Name

`MinMaxGray` — Determine the minimum and maximum gray values within regions.

## Signature

`static void HOperatorSet.MinMaxGray(HObject regions, HObject image, HTuple percent, out HTuple min, out HTuple max, out HTuple range)`

`void HImage.MinMaxGray(HRegion regions, HTuple percent, out HTuple min, out HTuple max, out HTuple range)`

`void HImage.MinMaxGray(HRegion regions, double percent, out double min, out double max, out double range)`

`void HRegion.MinMaxGray(HImage image, HTuple percent, out HTuple min, out HTuple max, out HTuple range)`

`void HRegion.MinMaxGray(HImage image, double percent, out double min, out double max, out double range)`

## Description

The operator `MinMaxGray` creates the histogram of the
absolute frequencies of the gray values within *`regions`* in
the input image *`image`* (see [`GrayHisto`](gray_histo.md)) and
calculates the number of pixels *`percent`* corresponding to
the area of the input image. Then it goes inwards on both sides of
the histogram by this number of pixels and determines the smallest
and the largest gray value:

- —

  *Example:*

  With area = 60, *`percent`* = *5*, d.h. i.e. 3 pixels,
  histogram = [2,8,0,7,13,0,0,...,0,10,10,5,3,1,1],

  $\Rightarrow$ Minimum = 0, Maximum = 255, range = 255

  `MinMaxGray` returns:
  *`min`* = *1*,
  *`max`* = *253*,
  *`range`* = *252*.

For images of type `int4`, `int8`, and `real`,
the above calculation is not performed via histograms, but using a rank
selection algorithm.
If *`percent`* is set to *50*,
*`min`* = *`max`* = Median.
If *`percent`* is *0* no histogram is calculated in
order to enhance the runtime.

## Attention

Note that the operator `MinMaxGray` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions, the features of which are to be calculated.

**`image`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Gray value image.

**`percent`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Percentage below (above) the absolute maximum
(minimum).

Default:
0

Suggested values:
0, 1, 2, 5, 7, 10, 15, 20, 30, 40, 50

Restriction:
`0 <= Percent && Percent <= 50`

**`min`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

“Minimum” gray value.

**`max`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

“Maximum” gray value.

Assertion:
`Max >= Min`

**`range`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Difference between Max and Min.

Assertion:
`Range >= 0`

## Example (HDevelop)

```
* Threshold segmentation with training region:
read_image(Image,'fabrik')
draw_region(Region,WindowHandle)
min_max_gray(Region,Image,5,Min,Max,Range)
threshold(Image,SegmentedRegion,Min,Max)
dev_display(SegmentedRegion)
```

## Result

The operator `MinMaxGray` returns the value 2 (
H_MSG_TRUE)
if the
input image has the defined gray values and the parameters are
correct. The behavior in case of empty input (no input images
available) is set via the operator
`set_system(::'no_object_result',<Result>:)`.
The behavior in case of an empty region is set via the operator
`set_system(::'empty_region_result',<Result>:)`.
If necessary an exception is raised.

## Possible Predecessors

`DrawRegion`,
`GenCircle`,
`GenEllipse`,
`GenRectangle1`,
`Threshold`,
`Regiongrowing`

## Possible Successors

`Threshold`

## Alternatives

`SelectGray`,
`Intensity`

## See also

`GrayHisto`,
`ScaleImage`,
`ScaleImageMax`,
`LearnNdimNorm`

## Module

Foundation
