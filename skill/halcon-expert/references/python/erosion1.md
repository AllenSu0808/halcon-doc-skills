# erosion1 (Operator)

## Name

`erosion1` — Erode a region.

## Signature

`def erosion1(region: HObject, struct_element: HObject, iterations: int) -> HObject`

## Description

`erosion1` erodes the input regions with a structuring
element. By applying `erosion1` to a region, its boundary
gets smoothed. In the process, the area of the region is reduced.
Furthermore, connected regions may be split. Such regions, however,
remain logically one region. The erosion is a set-theoretic region
operation. It uses the intersection operation.

Let M (*`struct_element`*) and R (*`region`*) be
two regions, where M is the structuring element and R is the
region to be processed. Furthermore, let m be a point in M.
Then the displacement vector $\vec{v}_{m} = (dx, dy)$ ![figure](../assets/fcb6dfd60b68379f.svg) is defined as the difference of the
center of gravity of M and the vector $\vec{m}$ ![figure](../assets/d29361c66a47570b.svg). Let
$t\vec{v}_m(R)$ ![figure](../assets/8db924e4920e9126.svg) denote the translation of a
region R by a vector $\vec{v}$ ![figure](../assets/05a972972d5ef7bd.svg). Then
$$erosion1(R, M) := \bigcap_{m\in M} t_{-\vec{v}_m}(R).$$ ![figure](../assets/3db9ee011dc3e651.svg)

For each point m in M a translation of the region R is
performed. The intersection of all these translations is the
erosion of R with M. `erosion1` is similar to the
operator [`minkowski_sub1`](minkowski_sub1.md), the difference is that in
`erosion1` the structuring element is mirrored at the
origin. The position of *`struct_element`* is meaningless,
since the displacement vectors are determined with respect to the
center of gravity of M.

The parameter *`iterations`* determines the number of
iterations which are to be performed with the structuring element.
The result of iteration n-1 is used as input for iteration n.
From the above definition it follows that the maximum region is
generated in case of an empty structuring element.

Structuring elements (*`struct_element`*) can be generated
with operators such as [`gen_circle`](gen_circle.md), [`gen_rectangle1`](gen_rectangle1.md),
[`gen_rectangle2`](gen_rectangle2.md), [`gen_ellipse`](gen_ellipse.md),
[`draw_region`](draw_region.md), [`gen_region_polygon`](gen_region_polygon.md),
[`gen_region_points`](gen_region_points.md), etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be eroded.

**`struct_element`** (input_object)  region `→` HObject

Structuring element.

**`region_erosion`** (output_object)  region(-array) `→` HObject

Eroded regions.

**`iterations`** (input_control)  integer `→` int

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

`erosion1` returns 2 (
H_MSG_TRUE)
if all parameters are correct.
The behavior in case of empty or no input region can be set via:

- no region:
  `set_system('no_object_result',<RegionResult>)`
- empty region:
  `set_system('empty_region_result',<RegionResult>)`

Otherwise, an exception is raised.

## Possible Predecessors

`threshold`,
`regiongrowing`,
`watersheds`,
`class_ndim_norm`,
`gen_circle`,
`gen_ellipse`,
`gen_rectangle1`,
`gen_rectangle2`,
`draw_region`,
`gen_region_points`,
`gen_region_polygon_filled`

## Possible Successors

`connection`,
`reduce_domain`,
`select_shape`,
`area_center`

## Alternatives

`minkowski_sub1`,
`minkowski_sub2`,
`erosion2`

## See also

`transpose_region`

## Module

Foundation
