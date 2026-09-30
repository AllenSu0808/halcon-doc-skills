# ZoomRegion (Operator)

## Name

`ZoomRegion` — Zoom a region.

## Signature

`static void HOperatorSet.ZoomRegion(HObject region, out HObject regionZoom, HTuple scaleWidth, HTuple scaleHeight)`

`HRegion HRegion.ZoomRegion(double scaleWidth, double scaleHeight)`

## Description

`ZoomRegion` enlarges or reduces the regions given in
*`region`* in the x- and y-direction by the given scale
factors *`scaleWidth`* and *`scaleHeight`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be zoomed.

**`regionZoom`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Zoomed region(s).

Number of elements:
RegionZoom == Region

**`scaleWidth`** (input_control)  extent.x `→` [HTuple](HTuple.md) (*double*)

Scale factor in x-direction.

Default:
2.0

Suggested values:
0.25, 0.5, 1.0, 2.0, 3.0

Value range:
`0.0
≤
scaleWidth
≤
100.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.5

**`scaleHeight`** (input_control)  extent.y `→` [HTuple](HTuple.md) (*double*)

Scale factor in y-direction.

Default:
2.0

Suggested values:
0.25, 0.5, 1.0, 2.0, 3.0

Value range:
`0.0
≤
scaleHeight
≤
100.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.5

## Possible Predecessors

`Threshold`,
`Connection`,
`Regiongrowing`,
`Pouring`

## Possible Successors

`SelectShape`,
`DispRegion`

## See also

`ZoomImageSize`,
`ZoomImageFactor`

## Module

Foundation
