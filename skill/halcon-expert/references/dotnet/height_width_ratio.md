# HeightWidthRatio (Operator)

## Name

`HeightWidthRatio` — Compute the width, height, and aspect ratio of the surrounding
rectangle parallel to the coordinate axes.

## Signature

`static void HOperatorSet.HeightWidthRatio(HObject regions, out HTuple height, out HTuple width, out HTuple ratio)`

`HTuple HRegion.HeightWidthRatio(out HTuple width, out HTuple ratio)`

`int HRegion.HeightWidthRatio(out int width, out double ratio)`

## Description

The operator `HeightWidthRatio` calculates the surrounding
rectangle of all input regions (parallel to the coordinate axes).
The surrounding rectangle is described by the coordinates of the
corner pixels
(`row1`,`column1`,`row2`,`column2`)
(see [`SmallestRectangle1`](smallest_rectangle1.md)). Based on these values,
`HeightWidthRatio` computes the width, height, and aspect
ratio of the smallest surrounding rectangle as follows:
$$Width = Column2-Column1+1 Height = Row2-Row1+1 Ratio = Height/Width$$ ![figure](../assets/05e73c057c084698.svg)

If more than one region is passed in *`regions`*, the results
are stored in tuples in the same order as the respective regions in
the *`regions`*. In case of empty regions, all parameters have
the value 0 if no other behavior was set (see [`SetSystem`](set_system.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`regions`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Regions to be examined.

**`height`** (output_control)  extent.y(-array) `→` [HTuple](HTuple.md) (*int* / long)

Height of the surrounding rectangle of the region.

**`width`** (output_control)  extent.x(-array) `→` [HTuple](HTuple.md) (*int* / long)

Width of the surrounding rectangle of the region.

**`ratio`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Aspect ratio of the surrounding rectangle of the region.

## Complexity

If F is the area of the region the mean runtime complexity is
O(sqrt(F)).

## Result

The operator `HeightWidthRatio` returns the value 2 (
H_MSG_TRUE)
if
the input is not empty. The behavior in case of empty input (no
input regions available) is set via the operator
`set_system('no_object_result',<Result>)`. The behavior in
case of empty region (the region is the empty set) is set via
`set_system('empty_region_result',<Result>)`. If necessary an
exception is raised.

## Possible Predecessors

`Threshold`,
`Regiongrowing`,
`Connection`,
`RunlengthFeatures`

## Alternatives

`SmallestRectangle1`,
`SmallestRectangle2`,
`RegionFeatures`

## See also

`SelectShape`,
`SmallestCircle`,
`EllipticAxis`,
`AreaCenter`

## Module

Foundation
