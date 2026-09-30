# minkowski_add2 (Operator)

## Name

`minkowski_add2` — Dilate a region (using a reference point).

## Signature

`minkowski_add2(Region, StructElement : RegionMinkAdd : Row, Column, Iterations : )`

## Description

`minkowski_add2` computes the Minkowski addition of the
input regions with a structuring element (*`StructElement`*)
having the reference point (*`Row`*,*`Column`*).
`minkowski_add2` has a similar effect as
[`minkowski_add1`](minkowski_add1.md), the difference is that the reference
point of the structuring element can be chosen arbitrarily. The
parameter *`Iterations`* determines the number of iterations
which are to be performed with the structuring element. The result
of iteration n-1 is used as input for iteration n.

An empty region is generated in case of an empty structuring
element.

Structuring elements (*`StructElement`*) can be generated
with operators such as [`gen_circle`](gen_circle.md), [`gen_rectangle1`](gen_rectangle1.md),
[`gen_rectangle2`](gen_rectangle2.md), [`gen_ellipse`](gen_ellipse.md),
[`draw_region`](draw_region.md), [`gen_region_polygon`](gen_region_polygon.md),
[`gen_region_points`](gen_region_points.md), etc.

## Attention

A Minkowski addition always results in enlarged regions.
Closely spaced regions which may touch or overlap as a result of the
dilation are still treated as two separate regions. If the desired
behavior is to merge them into one region, the operator
[`union1`](union1.md) has to be called first.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be dilated.

**`StructElement`** (input_object)  region `→` object

Structuring element.

**`RegionMinkAdd`** (output_object)  region(-array) `→` object

Dilated regions.

**`Row`** (input_control)  point.y `→`  (integer)

Row coordinate of the reference point.

Value range:
`1
≤
Row
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Column`** (input_control)  point.x `→`  (integer)

Column coordinate of the reference point.

Value range:
`1
≤
Column
≤
511` (lin)

Minimum increment:
1

Recommended increment:
1

**`Iterations`** (input_control)  integer `→`  (integer)

Number of iterations.

Default:
1

Suggested values:
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 17, 20, 30, 40, 50

Value range:
`1
≤
Iterations` (lin)

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

`minkowski_add2` returns 2 (
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

`threshold`,
`regiongrowing`,
`connection`,
`union1`,
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

`minkowski_add1`,
`dilation1`

## See also

`transpose_region`

## Module

Foundation
