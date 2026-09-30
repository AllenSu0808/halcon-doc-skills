# TopHat (Operator)

## Name

`TopHat` — Compute the top hat of regions.

## Signature

`static void HOperatorSet.TopHat(HObject region, HObject structElement, out HObject regionTopHat)`

`HRegion HRegion.TopHat(HRegion structElement)`

## Description

`TopHat` computes the [`Opening`](opening.md) of
*`region`* with *`structElement`*. The difference
between the original region and the result of the opening is called
the top hat. In contrast to [`Opening`](opening.md), which splits
regions under certain circumstances, `TopHat` computes
the regions removed by such a splitting.

The position of *`structElement`* is meaningless, since an
opening operation is invariant with respect to the choice of the
reference point.

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

Regions to be processed.

**`structElement`** (input_object)  region `→` [HRegion](HRegion.md)

Structuring element (position independent).

**`regionTopHat`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Result of the top hat operator.

## Result

`TopHat` returns 2 (
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
`Connection`,
`Union1`,
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

`ReduceDomain`,
`SelectShape`,
`AreaCenter`,
`Connection`

## Alternatives

`Opening`,
`Difference`

## See also

`BottomHat`,
`GrayTophat`,
`Opening`

## Module

Foundation
