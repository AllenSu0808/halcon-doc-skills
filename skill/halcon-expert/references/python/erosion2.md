# erosion2 (Operator)

## Name

`erosion2` — Erode a region (using a reference point).

## Signature

`def erosion2(region: HObject, struct_element: HObject, row: int, column: int, iterations: int) -> HObject`

## Description

`erosion2` erodes the input regions with a structuring
element (*`struct_element`*) having the reference point
(*`row`*,*`column`*). `erosion2` has a
similar effect as [`erosion1`](erosion1.md), the difference is that
the reference point of the structuring element can be chosen
arbitrarily. The parameter *`iterations`* determines the
number of iterations which are to be performed with the structuring
element. The result of iteration n-1 is used as input for
iteration n.

A maximum region is generated in case of an empty structuring
element.

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

**`row`** (input_control)  point.y `→` int

Row coordinate of the reference point.

Default:
0

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

**`column`** (input_control)  point.x `→` int

Column coordinate of the reference point.

Default:
0

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

`erosion2` returns 2 (
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

`reduce_domain`,
`select_shape`,
`area_center`,
`connection`

## Alternatives

`minkowski_sub2`,
`minkowski_sub1`,
`erosion1`

## See also

`transpose_region`,
`gen_circle`,
`gen_rectangle2`,
`gen_region_polygon`

## Module

Foundation
