# top_hat (Operator)

## Name

`top_hat` — Compute the top hat of regions.

## Signature

`top_hat(Region, StructElement : RegionTopHat : : )`

## Description

`top_hat` computes the [`opening`](opening.md) of
*`Region`* with *`StructElement`*. The difference
between the original region and the result of the opening is called
the top hat. In contrast to [`opening`](opening.md), which splits
regions under certain circumstances, `top_hat` computes
the regions removed by such a splitting.

The position of *`StructElement`* is meaningless, since an
opening operation is invariant with respect to the choice of the
reference point.

Structuring elements (*`StructElement`*) can be generated
with operators such as [`gen_circle`](gen_circle.md), [`gen_rectangle1`](gen_rectangle1.md),
[`gen_rectangle2`](gen_rectangle2.md), [`gen_ellipse`](gen_ellipse.md),
[`draw_region`](draw_region.md), [`gen_region_polygon`](gen_region_polygon.md),
[`gen_region_points`](gen_region_points.md), etc.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Regions to be processed.

**`StructElement`** (input_object)  region `→` object

Structuring element (position independent).

**`RegionTopHat`** (output_object)  region(-array) `→` object

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
