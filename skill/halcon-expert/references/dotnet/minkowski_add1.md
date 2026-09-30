# MinkowskiAdd1 (Operator)

## Name

`MinkowskiAdd1` — Perform a Minkowski addition on a region.

## Signature

`static void HOperatorSet.MinkowskiAdd1(HObject region, HObject structElement, out HObject regionMinkAdd, HTuple iterations)`

`HRegion HRegion.MinkowskiAdd1(HRegion structElement, int iterations)`

## Description

`MinkowskiAdd1` dilates the input regions with a
structuring element. By applying `MinkowskiAdd1` to a
region, its boundary gets smoothed. In the process, the area of the
region is enlarged. Furthermore, disconnected regions may be
merged. Such regions, however, remain logically distinct region.
The Minkowski addition is a set-theoretic region operation. It is
based on translations and union operations.

Let M (*`structElement`*) and R (*`region`*) be
two regions, where M is the structuring element and R is the
region to be processed. Furthermore, let m be a point in M.
Then the displacement vector $\vec{v}_{m} = (dx, dy)$ ![figure](../assets/fcb6dfd60b68379f.svg) is defined as the difference of the
center of gravity of M and the vector $\vec{m}$ ![figure](../assets/d29361c66a47570b.svg). Let
$t\vec{v}_m(R)$ ![figure](../assets/8db924e4920e9126.svg) denote the translation of a
region R by a vector $\vec{v}$ ![figure](../assets/05a972972d5ef7bd.svg). Then
$$minkowski_add1(R,M) := \bigcup_{m \in M} t_{\vec{m}}(R)$$ ![figure](../assets/db1d8c4eb504c502.svg)

For each point m in M a translation of the region R is
performed. The union of all these translations is the Minkowski
addition of R with M. `MinkowskiAdd1` is similar to
the operator [`Dilation1`](dilation1.md), the difference is that in
[`Dilation1`](dilation1.md) the structuring element is mirrored at the
origin. The position of *`structElement`* is meaningless,
since the displacement vectors are determined with respect to the
center of gravity of M.

The parameter *`iterations`* determines the number of
iterations which are to be performed with the structuring element.
The result of iteration n-1 is used as input for iteration n.
From the above definition it follows that an empty region is
generated in case of an empty structuring element.

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

`MinkowskiAdd1` returns 2 (
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

`MinkowskiAdd2`,
`Dilation1`

## See also

`TransposeRegion`,
`MinkowskiSub1`

## Module

Foundation
