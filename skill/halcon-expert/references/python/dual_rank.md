# dual_rank (Operator)

## Name

`dual_rank` — Opening, Median and Closing with circle or rectangle mask.

## Signature

`def dual_rank(image: HObject, mask_type: str, radius: int, mode_percent: int, margin: Union[int, float, str]) -> HObject`

## Description

The operator `dual_rank` carries out a non-linear
transformation of the gray values of all input images
(*`image`*). Circles or squares can be used as structuring
elements. The operator `dual_rank` effects two
consecutive calls of [`rank_image`](rank_image.md). At the first call the
range gray value is calculated with the indicated range
(*`mode_percent`*). The result of this calculation is the
input of a further call of [`rank_image`](rank_image.md), this time using the
range value 100-*`mode_percent`*.

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
*`mode_percent`*, rank values between 0...100 in
percent) is selected and set as result gray value in the
corresponding result image.

If *`mode_percent`* is 0, then the operator equals to the
gray value opening ([`gray_opening`](gray_opening.md)). If
*`mode_percent`* is 50, the operator results in the median
filter, which is applied twice ([`median_image`](median_image.md)). The
*`mode_percent`* 100 in `dual_rank` means that it
calculates the gray value closing ([`gray_closing`](gray_closing.md)).
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

**`image`** (input_object)  (multichannel-)image(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Image to be filtered.

**`image_rank`** (output_object)  multichannel-image(-array) `→` HObject (byte / int2 / uint2 / int4 / real)

Filtered Image.

**`mask_type`** (input_control)  string `→` str

Shape of the mask.

Default:
"circle"

List of values:
"circle", "square"

**`radius`** (input_control)  integer `→` int

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

**`mode_percent`** (input_control)  integer `→` int

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
mode_percent
≤
100`

Minimum increment:
1

Recommended increment:
2

**`margin`** (input_control)  string `→` Union[int, float, str]

Border treatment.

Default:
"mirrored"

Suggested values:
"mirrored", "cyclic", "continued", 0, 30, 60, 90, 120, 150, 180, 210, 240, 255

## Complexity

For each pixel: $O(\sqrt{F} * 10)$ ![figure](../assets/e01c151d4d521f8b.svg) with F =
area of the structuring element.

## Result

If the parameter values are correct the operator
`dual_rank` returns the value 2 (
H_MSG_TRUE)
. The behavior in case
of empty input (no input images available) is set via the operator
`set_system('no_object_result',<Result>)`.
If necessary an exception is raised.

## Possible Predecessors

`read_image`

## Possible Successors

`threshold`,
`dyn_threshold`,
`sub_image`,
`regiongrowing`

## Alternatives

`rank_image`,
`gray_closing`,
`gray_opening`,
`median_image`

## See also

`gen_circle`,
`gen_rectangle1`,
`gray_erosion_rect`,
`gray_dilation_rect`,
`sigma_image`

## References

W. Eckstein, O. Munkelt
“Extracting Objects from Digital Terrain Model”
Remote Sensing and Reconstruction for Threedimensional Objects and Scenes,
SPIE Symposium on Optical Science, Engeneering, and Instrumentation,
July 1995, San Diego

## Module

Foundation
