# dual_threshold (Operator)

## Name

`dual_threshold` — Threshold operator for signed images.

## Signature

`def dual_threshold(image: HObject, min_size: int, min_gray: float, threshold: float) -> HObject`

## Description

`dual_threshold` segments the input image into a region with
gray values $\ge$*`threshold`* (“positive”
regions) and a region with gray values $\le-$*`threshold`*
(“negative” regions). Only “positive” or
“negative” regions having a size larger than *`min_size`* are
taken into account. And regions whose maximum gray value is less than
*`min_gray`* in absolute value are suppressed.

The segmentation performed is not complete, i.e., the “positive”
and “negative” regions together do not necessarily cover the
entire image: Areas with a gray value between
$-$*`threshold`* and
*`threshold`*, $-$*`min_gray`* and
*`min_gray`*, respectively, are not taken into account.

`dual_threshold` is usually called after applying a Laplace
operator ([`laplace`](laplace.md), [`laplace_of_gauss`](laplace_of_gauss.md),
[`derivate_gauss`](derivate_gauss.md) or [`diff_of_gauss`](diff_of_gauss.md)) to an image or with
the difference of two images ([`sub_image`](sub_image.md)).

The zero crossings of a Laplace image correspond to edges in an
image, and are the separating regions of the “positive” and
“negative” regions in the Laplace image. They can be determined
by calling `dual_threshold` with *`threshold`* = 1 and
then creating the complement regions with [`complement`](complement.md). The
parameter *`min_gray`* determines the noise invariance, while
*`min_size`* determines the resolution of the edge detection.

Using byte images, only the positive part of the operator is
applied. Therefore `dual_threshold` behaves like a standard
threshold operator ([`threshold`](threshold.md)) with successive
[`connection`](connection.md) and [`select_gray`](select_gray.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` HObject (byte / int1 / int2 / int4 / real)

Input image.

**`region_crossings`** (output_object)  region-array `→` HObject

Positive and negative regions.

**`min_size`** (input_control)  integer `→` int

Regions smaller than MinSize are suppressed.

Default:
20

Suggested values:
0, 10, 20, 50, 100, 200, 500, 1000

Value range:
`0
≤
min_size
≤
10000` (lin)

Minimum increment:
1

Recommended increment:
10

**`min_gray`** (input_control)  real `→` float

Regions whose maximum absolute gray value is smaller
than MinGray are suppressed.

Default:
5.0

Suggested values:
1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0, 15.0, 20.0

Value range:
`0
≤
min_gray` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`threshold`** (input_control)  real `→` float

Regions that have a gray value smaller than Threshold
(or larger than -Threshold) are suppressed.

Default:
2.0

Suggested values:
1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0, 15.0, 20.0

Value range:
`0
≤
threshold` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

## Result

`dual_threshold` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`set_system`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`min_max_gray`,
`sobel_amp`,
`binomial_filter`,
`gauss_filter`,
`reduce_domain`,
`diff_of_gauss`,
`sub_image`,
`derivate_gauss`,
`laplace_of_gauss`,
`laplace`,
`expand_region`

## Possible Successors

`connection`,
`dilation1`,
`erosion1`,
`opening`,
`closing`,
`rank_region`,
`shape_trans`,
`skeleton`

## Alternatives

`threshold`,
`dyn_threshold`,
`check_difference`

## See also

`connection`,
`select_shape`,
`select_gray`

## Module

Foundation
