# DualThreshold (Operator)

## Name

`DualThreshold` — Threshold operator for signed images.

## Signature

`static void HOperatorSet.DualThreshold(HObject image, out HObject regionCrossings, HTuple minSize, HTuple minGray, HTuple threshold)`

`HRegion HImage.DualThreshold(int minSize, double minGray, double threshold)`

## Description

`DualThreshold` segments the input image into a region with
gray values $\ge$*`threshold`* (“positive”
regions) and a region with gray values $\le-$*`threshold`*
(“negative” regions). Only “positive” or
“negative” regions having a size larger than *`minSize`* are
taken into account. And regions whose maximum gray value is less than
*`minGray`* in absolute value are suppressed.

The segmentation performed is not complete, i.e., the “positive”
and “negative” regions together do not necessarily cover the
entire image: Areas with a gray value between
$-$*`threshold`* and
*`threshold`*, $-$*`minGray`* and
*`minGray`*, respectively, are not taken into account.

`DualThreshold` is usually called after applying a Laplace
operator ([`Laplace`](laplace.md), [`LaplaceOfGauss`](laplace_of_gauss.md),
[`DerivateGauss`](derivate_gauss.md) or [`DiffOfGauss`](diff_of_gauss.md)) to an image or with
the difference of two images ([`SubImage`](sub_image.md)).

The zero crossings of a Laplace image correspond to edges in an
image, and are the separating regions of the “positive” and
“negative” regions in the Laplace image. They can be determined
by calling `DualThreshold` with *`threshold`* = 1 and
then creating the complement regions with [`Complement`](complement.md). The
parameter *`minGray`* determines the noise invariance, while
*`minSize`* determines the resolution of the edge detection.

Using byte images, only the positive part of the operator is
applied. Therefore `DualThreshold` behaves like a standard
threshold operator ([`Threshold`](threshold.md)) with successive
[`Connection`](connection.md) and [`SelectGray`](select_gray.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`image`** (input_object)  singlechannelimage(-array) `→` [HImage](HImage.md) (byte / int1 / int2 / int4 / real)

Input image.

**`regionCrossings`** (output_object)  region-array `→` [HRegion](HRegion.md)

Positive and negative regions.

**`minSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Regions smaller than MinSize are suppressed.

Default:
20

Suggested values:
0, 10, 20, 50, 100, 200, 500, 1000

Value range:
`0
≤
minSize
≤
10000` (lin)

Minimum increment:
1

Recommended increment:
10

**`minGray`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

Regions whose maximum absolute gray value is smaller
than MinGray are suppressed.

Default:
5.0

Suggested values:
1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 9.0, 11.0, 15.0, 20.0

Value range:
`0
≤
minGray` (lin)

Minimum increment:
1.0

Recommended increment:
10.0

**`threshold`** (input_control)  real `→` [HTuple](HTuple.md) (*double*)

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

`DualThreshold` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior with respect to the input images and output
regions can be determined by setting the values of the flags
*"no_object_result"*, *"empty_region_result"*, and
*"store_empty_region"* with [`SetSystem`](set_system.md).
If necessary, an exception is raised.

## Possible Predecessors

`MinMaxGray`,
`SobelAmp`,
`BinomialFilter`,
`GaussFilter`,
`ReduceDomain`,
`DiffOfGauss`,
`SubImage`,
`DerivateGauss`,
`LaplaceOfGauss`,
`Laplace`,
`ExpandRegion`

## Possible Successors

`Connection`,
`Dilation1`,
`Erosion1`,
`Opening`,
`Closing`,
`RankRegion`,
`ShapeTrans`,
`Skeleton`

## Alternatives

`Threshold`,
`DynThreshold`,
`CheckDifference`

## See also

`Connection`,
`SelectShape`,
`SelectGray`

## Module

Foundation
