# Erosion1 (Operator)

## Name

`Erosion1` — Erode a region.

## Signature

`static void HOperatorSet.Erosion1(HObject region, HObject structElement, out HObject regionErosion, HTuple iterations)`

`HRegion HRegion.Erosion1(HRegion structElement, int iterations)`

## Description

`Erosion1` erodes the input regions with a structuring
element. By applying `Erosion1` to a region, its boundary
gets smoothed. In the process, the area of the region is reduced.
Furthermore, connected regions may be split. Such regions, however,
remain logically one region. The erosion is a set-theoretic region
operation. It uses the intersection operation.

Let M (*`structElement`*) and R (*`region`*) be
two regions, where M is the structuring element and R is the
region to be processed. Furthermore, let m be a point in M.
Then the displacement vector $\vec{v}_{m} = (dx, dy)$ ![figure](../assets/fcb6dfd60b68379f.svg) is defined as the difference of the
center of gravity of M and the vector $\vec{m}$ ![figure](../assets/d29361c66a47570b.svg). Let
$t\vec{v}_m(R)$ ![figure](../assets/8db924e4920e9126.svg) denote the translation of a
region R by a vector $\vec{v}$ ![figure](../assets/05a972972d5ef7bd.svg). Then
$$erosion1(R, M) := \bigcap_{m\in M} t_{-\vec{v}_m}(R).$$ ![figure](../assets/3db9ee011dc3e651.svg)

For each point m in M a translation of the region R is
performed. The intersection of all these translations is the
erosion of R with M. `Erosion1` is similar to the
operator [`MinkowskiSub1`](minkowski_sub1.md), the difference is that in
`Erosion1` the structuring element is mirrored at the
origin. The position of *`structElement`* is meaningless,
since the displacement vectors are determined with respect to the
center of gravity of M.

The parameter *`iterations`* determines the number of
iterations which are to be performed with the structuring element.
The result of iteration n-1 is used as input for iteration n.
From the above definition it follows that the maximum region is
generated in case of an empty structuring element.

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

**`regionErosion`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Eroded regions.

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

`Erosion1` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty or no input region can be set via:

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

`Connection`,
`ReduceDomain`,
`SelectShape`,
`AreaCenter`

## Alternatives

`MinkowskiSub1`,
`MinkowskiSub2`,
`Erosion2`

## See also

`TransposeRegion`

## Module

Foundation
