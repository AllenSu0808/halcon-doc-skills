# opening (Operator)

## Name

`opening` — Open a region.

## Signature

`def opening(region: HObject, struct_element: HObject) -> HObject`

## Description

An `opening` operation is defined as an erosion followed
by a Minkowski addition. By applying `opening` to a
region, larger structures remain mostly intact, while small
structures like lines or points are eliminated. In contrast, a
[`closing`](closing.md) operation results in small gaps being retained
or filled up (see [`closing`](closing.md)).

`opening` serves to eliminate small regions (smaller than
*`struct_element`*) and to smooth the boundaries of a region.
The position of *`struct_element`* is meaningless, since an
opening operation is invariant with respect to the choice of the
reference point.

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

Regions to be opened.

**`struct_element`** (input_object)  region `→` HObject

Structuring element (position-invariant).

**`region_opening`** (output_object)  region(-array) `→` HObject

Opened regions.

## Complexity

Let F1 be the area of the input region, and F2 be the area of
the structuring element. Then the runtime complexity for one region
is:
$$O\left(2\cdot \sqrt{F1}\cdot \sqrt{F2}\right)\,.$$ ![figure](../assets/df053ef6aed1f7b1.svg)

## Result

`opening` returns 2 (
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

`minkowski_add1`,
`erosion1`,
`opening_circle`

## See also

`gen_circle`,
`gen_rectangle2`,
`gen_region_polygon`

## Module

Foundation
