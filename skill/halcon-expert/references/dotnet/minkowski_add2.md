# MinkowskiAdd2 (Operator)

## Name

`MinkowskiAdd2` — Dilate a region (using a reference point).

## Signature

`static void HOperatorSet.MinkowskiAdd2(HObject region, HObject structElement, out HObject regionMinkAdd, HTuple row, HTuple column, HTuple iterations)`

`HRegion HRegion.MinkowskiAdd2(HRegion structElement, int row, int column, int iterations)`

## Description

`MinkowskiAdd2` computes the Minkowski addition of the
input regions with a structuring element (*`structElement`*)
having the reference point (*`row`*,*`column`*).
`MinkowskiAdd2` has a similar effect as
[`MinkowskiAdd1`](minkowski_add1.md), the difference is that the reference
point of the structuring element can be chosen arbitrarily. The
parameter *`iterations`* determines the number of iterations
which are to be performed with the structuring element. The result
of iteration n-1 is used as input for iteration n.

An empty region is generated in case of an empty structuring
element.

Structuring elements (*`structElement`*) can be generated
with operators such as [`GenCircle`](gen_circle.md), [`GenRectangle1`](gen_rectangle1.md),
[`GenRectangle2`](gen_rectangle2.md), [`GenEllipse`](gen_ellipse.md),
[`DrawRegion`](draw_region.md), [`GenRegionPolygon`](gen_region_polygon.md),
[`GenRegionPoints`](gen_region_points.md), etc.

## Attention

A Minkowski addition always results in enlarged regions.
Closely spaced regions which may touch or overlap as a result of the
dilation are still treated as two separate regions. If the desired
behavior is to merge them into one region, the operator
[`Union1`](union1.md) has to be called first.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be dilated.

**`structElement`** (input_object)  region `→` [HRegion](HRegion.md)

Structuring element.

**`regionMinkAdd`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Dilated regions.

**`row`** (input_control)  point.y `→` [HTuple](HTuple.md) (*int* / long)

Row coordinate of the reference point.

Value range:
`1
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

Value range:
`1
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

`MinkowskiAdd2` returns 2 (
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
`Connection`,
`Union1`,
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

`MinkowskiAdd1`,
`Dilation1`

## See also

`TransposeRegion`

## Module

Foundation
