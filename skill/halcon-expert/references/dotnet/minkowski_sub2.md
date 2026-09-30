# MinkowskiSub2 (Operator)

## Name

`MinkowskiSub2` — Erode a region (using a reference point).

## Signature

`static void HOperatorSet.MinkowskiSub2(HObject region, HObject structElement, out HObject regionMinkSub, HTuple row, HTuple column, HTuple iterations)`

`HRegion HRegion.MinkowskiSub2(HRegion structElement, int row, int column, int iterations)`

## Description

`MinkowskiSub2` computes the Minkowski subtraction of the
input regions with a structuring element (*`structElement`*)
having the reference point (*`row`*,*`column`*).
`MinkowskiSub2` has a similar effect as
[`MinkowskiSub1`](minkowski_sub1.md), the difference is that the reference
point of the structuring element can be chosen arbitrarily. The
parameter *`iterations`* determines the number of iterations
which are to be performed with the structuring element. The result
of iteration n-1 is used as input for iteration n.

A maximum region is generated in case of an empty structuring
element.

Structuring elements (*`structElement`*) can be generated
with operators such as [`GenCircle`](gen_circle.md), [`GenRectangle1`](gen_rectangle1.md),
[`GenRectangle2`](gen_rectangle2.md), [`GenEllipse`](gen_ellipse.md),
[`DrawRegion`](draw_region.md), [`GenRegionPolygon`](gen_region_polygon.md),
[`GenRegionPoints`](gen_region_points.md), etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be eroded.

**`structElement`** (input_object)  region `→` [HRegion](HRegion.md)

Structuring element.

**`regionMinkSub`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Eroded regions.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the reference point.

Default:
0

Suggested values:
0, 10, 16, 32, 64, 100, 128

Value range:
`0
≤
row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`column`** (input_control)  point.x `→` [HTuple](HTuple.md) (*int* / long)

Column coordinate of the reference point.

Default:
0

Suggested values:
0, 10, 16, 32, 64, 100, 128

Value range:
`0
≤
column
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`iterations`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Number of iterations.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50

Value range:
`1
≤
iterations` (lin)

Minimum increment:
1

Recommended increment:
1

## Complexity

Let F1 be the area of the input region, and F2 be the area of
the structuring element. Then the runtime complexity for one region
is:
$$O\left(\sqrt{F1}\cdot\sqrt{F2}\cdotIterations\right) .$$ ![figure](../assets/d9f61aa2e42c6ccf.svg)

## Result

`MinkowskiSub2` returns 2 (
H_MSG_TRUE)
if all parameters are
correct. The behavior in case of empty or no input region can be
set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Watersheds`,
`ClassNdimNorm`,
`GenCircle`,
`GenEllipse`,
`GenRectangle1`,
`GenRectangle2`,
`DrawRegion`,
`GenRegionPoints`,
`GenRegionPolygonFilled`

## Possible Successors

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`MinkowskiSub1`,
`Erosion1`,
`Erosion2`

## See also

`GenCircle`,
`GenRectangle2`,
`GenRegionPolygon`

## Module

Foundation
