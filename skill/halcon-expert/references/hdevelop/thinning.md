# thinning (Operator)

## Name

`thinning` — Remove the result of a hit-or-miss operation from a region.

## Warning

**`thinning` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`thinning(Region, StructElement1, StructElement2 : RegionThin : Row, Column, Iterations : )`

## Description

`thinning` performs a thinning of the input regions
using morphological operations. The operator first applies a
hit-or-miss-transformation to *`Region`* (cf.
[`hit_or_miss`](hit_or_miss.md)), and then removes the detected points from
the input region. The parameter *`Iterations`* determines
the number of iterations performed.

For the choice of the structuring elements *`StructElement1`*
and *`StructElement2`*, as well as for *`Row`* and
*`Column`*, the same restrictions described under
[`hit_or_miss`](hit_or_miss.md) apply.

Structuring elements (*`StructElement1`*,
*`StructElement2`*) can be generated with operators such as
[`gen_circle`](gen_circle.md), [`gen_rectangle1`](gen_rectangle1.md), [`gen_rectangle2`](gen_rectangle2.md),
[`gen_ellipse`](gen_ellipse.md), [`draw_region`](draw_region.md),
[`gen_region_polygon`](gen_region_polygon.md), [`gen_region_points`](gen_region_points.md), etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be processed.

**`StructElement1`** (input_object)  region `→` object

Structuring element for the foreground.

**`StructElement2`** (input_object)  region `→` object

Structuring element for the background.

**`RegionThin`** (output_object)  region(-array) `→` object

Result of the thinning operator.

**`Row`** (input_control)  point.y `→`  (integer)

Row coordinate of the reference point.

Default:
0

Value range:
`0
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

Default:
0

Value range:
`0
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
