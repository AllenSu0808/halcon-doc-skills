# top_hat (Operator)

## Name

`top_hat` — Compute the top hat of regions.

## Signature

`def top_hat(region: HObject, struct_element: HObject) -> HObject`

## Description

`top_hat` computes the [`opening`](opening.md) of
*`region`* with *`struct_element`*. The difference
between the original region and the result of the opening is called
the top hat. In contrast to [`opening`](opening.md), which splits
regions under certain circumstances, `top_hat` computes
the regions removed by such a splitting.

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

Regions to be processed.

**`struct_element`** (input_object)  region `→` HObject

Structuring element (position independent).

**`region_top_hat`** (output_object)  region(-array) `→` HObject

Result of the top hat operator.

## Result

`top_hat` returns 2 (
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

`opening`,
`difference`

## See also

`bottom_hat`,
`gray_tophat`,
`opening`

## Module

Foundation
