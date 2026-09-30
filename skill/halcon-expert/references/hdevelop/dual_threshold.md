# dual_threshold (Operator)

## Name

`dual_threshold` — Threshold operator for signed images.

## Signature

`dual_threshold(Image : RegionCrossings : MinSize, MinGray, Threshold : )`

## Description

`dual_threshold` segments the input image into a region with
gray values $\ge$*`Threshold`* (“positive”
regions) and a region with gray values $\le-$*`Threshold`*
(“negative” regions). Only “positive” or
“negative” regions having a size larger than *`MinSize`* are
taken into account. And regions whose maximum gray value is less than
*`MinGray`* in absolute value are suppressed.

The segmentation performed is not complete, i.e., the “positive”
and “negative” regions together do not necessarily cover the
entire image: Areas with a gray value between
$-$*`Threshold`* and
*`Threshold`*, $-$*`MinGray`* and
*`MinGray`*, respectively, are not taken into account.

`dual_threshold` is usually called after applying a Laplace
operator ([`laplace`](laplace.md), [`laplace_of_gauss`](laplace_of_gauss.md),
[`derivate_gauss`](derivate_gauss.md) or [`diff_of_gauss`](diff_of_gauss.md)) to an image or with
the difference of two images ([`sub_image`](sub_image.md)).

The zero crossings of a Laplace image correspond to edges in an
image, and are the separating regions of the “positive” and
“negative” regions in the Laplace image. They can be determined
by calling `dual_threshold` with *`Threshold`* = 1 and
then creating the complement regions with [`complement`](complement.md). The
parameter *`MinGray`* determines the noise invariance, while
*`MinSize`* determines the resolution of the edge detection.

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

**`Image`** (input_object)  singlechannelimage(-array) `→` object (byte / int1 / int2 / int4 / real)

Input image.

**`RegionCrossings`** (output_object)  region-array `→` object

Positive and negative regions.

**`MinSize`** (input_control)  integer `→`  (integer)

Regions smaller than MinSize are suppressed.

Default:
20

Suggested values:
0, 10, 20, 50, 100, 200, 500, 1000

Value range:
`0
≤
MinSize
≤
10000` (lin)

Minimum increment:
1

Recommended increment:
10

**`MinGray`** (input_control)  real `→`  (real)

Regions whose maximum absolute gray value is smaller
than MinGray are suppressed.

Default:
5.0

Suggested values:
1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0, 15.0, 20.0

Value range:
`0
≤
MinGray` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`Threshold`** (input_control)  real `→`  (real)

Regions that have a gray value smaller than Threshold
(or larger than -Threshold) are suppressed.

Default:
2.0

Suggested values:
1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0, 15.0, 20.0

Value range:
`0
≤
Threshold` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

## Example (HDevelop)

```
* Edge detection with the Laplace operator (and edge thinning)
diff_of_gauss(Image,Laplace,2.0,1.6)
* find "`positive"' and "`negative"' regions:
dual_threshold(Laplace,Region,20,2,1)
* The zero runnings are the complement to these image section:
complement(Region,ZeroCrossings)

* Simulation of dual_threshold
dual_threshold(Laplace,Result,MinS,MinG,Threshold)
threshold(Laplace,Tmp1,Threshold,999999)
connection(Tmp1,Tmp2)
select_shape(Tmp2,Tmp3,'area','and',MinS,999999)
select_gray(Laplace,Tmp3,Tmp4,'max','and',MinG,999999)
threshold(Laplace,Tmp5,-999999,-Threshold)
connection(Tmp5,Tmp6)
select_shape(Tmp6,Tmp7,'area','and',MinS,999999)
select_gray(Laplace,Tmp7,Tmp8,'min','and',-999999,-MinG)
concat_obj(Tmp4,Tmp8,Result)
```

## Result

`dual_threshold` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*'no_object_result'*, *'empty_region_result'*, and
*'store_empty_region'* with [`set_system`](set_system.md).
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
