# thinning (Operator)

## Name

`thinning` — Remove the result of a hit-or-miss operation from a region.

## Warning

**`thinning` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def thinning(region: HObject, struct_element_1: HObject, struct_element_2: HObject, row: int, column: int, iterations: int) -> HObject`

## Description

`thinning` performs a thinning of the input regions
using morphological operations. The operator first applies a
hit-or-miss-transformation to *`region`* (cf.
[`hit_or_miss`](hit_or_miss.md)), and then removes the detected points from
the input region. The parameter *`iterations`* determines
the number of iterations performed.

For the choice of the structuring elements *`struct_element_1`*
and *`struct_element_2`*, as well as for *`row`* and
*`column`*, the same restrictions described under
[`hit_or_miss`](hit_or_miss.md) apply.

Structuring elements (*`struct_element_1`*,
*`struct_element_2`*) can be generated with operators such as
[`gen_circle`](gen_circle.md), [`gen_rectangle1`](gen_rectangle1.md), [`gen_rectangle2`](gen_rectangle2.md),
[`gen_ellipse`](gen_ellipse.md), [`draw_region`](draw_region.md),
[`gen_region_polygon`](gen_region_polygon.md), [`gen_region_points`](gen_region_points.md), etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be processed.

**`struct_element_1`** (input_object)  region `→` HObject

Structuring element for the foreground.

**`struct_element_2`** (input_object)  region `→` HObject

Structuring element for the background.

**`region_thin`** (output_object)  region(-array) `→` HObject

Result of the thinning operator.

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

Let F be the area of an input region, F1 the area of the
structuring element 1, and F2 the area of the structuring element
2. Then the runtime complexity for one object is:
$$O\left(\text{Iterations} \cdot \sqrt{F} \cdot \left(\sqrt{F1} + \sqrt{F2}\right)\right).$$ ![figure](../assets/25502f7020ba92cd.svg)

## Result

`thinning` returns 2 (
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

`thinning_golay`,
`thinning_seq`

## See also

`hit_or_miss`

## Module

Foundation
