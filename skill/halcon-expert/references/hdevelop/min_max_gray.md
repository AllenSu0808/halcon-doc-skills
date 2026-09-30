# min_max_gray (Operator)

## Name

`min_max_gray` — Determine the minimum and maximum gray values within regions.

## Signature

`min_max_gray(Regions, Image : : Percent : Min, Max, Range)`

## Description

The operator `min_max_gray` creates the histogram of the
absolute frequencies of the gray values within *`Regions`* in
the input image *`Image`* (see [`gray_histo`](gray_histo.md)) and
calculates the number of pixels *`Percent`* corresponding to
the area of the input image. Then it goes inwards on both sides of
the histogram by this number of pixels and determines the smallest
and the largest gray value:

- —

  *Example:*

  With area = 60, *`Percent`* = *5*, d.h. i.e. 3 pixels,
  histogram = [2,8,0,7,13,0,0,...,0,10,10,5,3,1,1],

  $\Rightarrow$ Minimum = 0, Maximum = 255, range = 255

  `min_max_gray` returns:
  *`Min`* = *1*,
  *`Max`* = *253*,
  *`Range`* = *252*.

For images of type `int4`, `int8`, and `real`,
the above calculation is not performed via histograms, but using a rank
selection algorithm.
If *`Percent`* is set to *50*,
*`Min`* = *`Max`* = Median.
If *`Percent`* is *0* no histogram is calculated in
order to enhance the runtime.

## Attention

Note that the operator `min_max_gray` only considers
the given *`Regions`* and ignores any previously set domain
of the input image *`Image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Regions, the features of which are to be calculated.

**`Image`** (input_object)  singlechannelimage `→` object (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Gray value image.

**`Percent`** (input_control)  number `→`  (real / integer)

Percentage below (above) the absolute maximum
(minimum).

Default:
0

Suggested values:
0, 1, 2, 5, 7, 10, 15, 20, 30, 40, 50

Restriction:
`0 <= Percent && Percent <= 50`

**`Min`** (output_control)  real(-array) `→`  (real)

“Minimum” gray value.

**`Max`** (output_control)  real(-array) `→`  (real)

“Maximum” gray value.

Assertion:
`Max >= Min`

**`Range`** (output_control)  real(-array) `→`  (real)

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

The operator `min_max_gray` returns the value 2 (
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

`draw_region`,
`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`threshold`,
`regiongrowing`

## Possible Successors

`threshold`

## Alternatives

`select_gray`,
`intensity`

## See also

`gray_histo`,
`scale_image`,
`scale_image_max`,
`learn_ndim_norm`

## Module

Foundation
