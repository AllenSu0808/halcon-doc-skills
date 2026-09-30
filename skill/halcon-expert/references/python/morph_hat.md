# morph_hat (Operator)

## Name

`morph_hat` — Compute the union of [`bottom_hat`](bottom_hat.md) and [`top_hat`](top_hat.md).

## Warning

**`morph_hat` is obsolete and is only provided for
reasons of backward compatibility.**

## Signature

`def morph_hat(region: HObject, struct_element: HObject) -> HObject`

## Description

`morph_hat` computes the union of the regions that are
removed by an [`opening`](opening.md) operation with the regions that are
added by a [`closing`](closing.md) operation. Hence this is the union
of the results of [`top_hat`](top_hat.md) and [`bottom_hat`](bottom_hat.md).
The position of *`struct_element`* does not influence the
result.

Structuring elements (*`struct_element`*) can be generated
with operators such as [`gen_circle`](gen_circle.md), [`gen_rectangle1`](gen_rectangle1.md),
[`gen_rectangle2`](gen_rectangle2.md), [`gen_ellipse`](gen_ellipse.md),
[`draw_region`](draw_region.md), [`gen_region_polygon`](gen_region_polygon.md),
[`gen_region_points`](gen_region_points.md), etc.

## Attention

The individual regions are processed separately.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Regions to be processed.

**`struct_element`** (input_object)  region `→` HObject

Structuring element (position-invariant).

**`region_morph_hat`** (output_object)  region(-array) `→` HObject

Union of top hat and bottom hat.

## Result

`morph_hat` returns 2 (
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

`top_hat`,
`bottom_hat`,
`union2`

## See also

`opening`,
`closing`

## Module

Foundation
