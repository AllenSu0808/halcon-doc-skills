# min_max_gray (Operator)

## Name

`min_max_gray` — Determine the minimum and maximum gray values within regions.

## Signature

`def min_max_gray(regions: HObject, image: HObject, percent: Union[int, float]) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def min_max_gray_s(regions: HObject, image: HObject, percent: Union[int, float]) -> Tuple[float, float, float]`

## Description

The operator `min_max_gray` creates the histogram of the
absolute frequencies of the gray values within *`regions`* in
the input image *`image`* (see [`gray_histo`](gray_histo.md)) and
calculates the number of pixels *`percent`* corresponding to
the area of the input image. Then it goes inwards on both sides of
the histogram by this number of pixels and determines the smallest
and the largest gray value:

- —

  *Example:*

  With area = 60, *`percent`* = *5*, d.h. i.e. 3 pixels,
  histogram = [2,8,0,7,13,0,0,...,0,10,10,5,3,1,1],

  $\Rightarrow$ Minimum = 0, Maximum = 255, range = 255

  `min_max_gray` returns:
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

Note that the operator `min_max_gray` only considers
the given *`regions`* and ignores any previously set domain
of the input image *`image`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` HObject

Regions, the features of which are to be calculated.

**`image`** (input_object)  singlechannelimage `→` HObject (byte / direction / cyclic / int1 / int2 / uint2 / int4 / int8 / real)

Gray value image.

**`percent`** (input_control)  number `→` Union[int, float]

Percentage below (above) the absolute maximum
(minimum).

Default:
0

Suggested values:
0, 1, 2, 5, 7, 10, 15, 20, 30, 40, 50

Restriction:
`0 <= Percent && Percent <= 50`

**`min`** (output_control)  real(-array) `→` Sequence[float]

“Minimum” gray value.

**`max`** (output_control)  real(-array) `→` Sequence[float]

“Maximum” gray value.

Assertion:
`Max >= Min`

**`range`** (output_control)  real(-array) `→` Sequence[float]

Difference between Max and Min.

Assertion:
`Range >= 0`

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
