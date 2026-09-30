# zoom_region (Operator)

## Name

`zoom_region` — Zoom a region.

## Signature

`zoom_region(Region : RegionZoom : ScaleWidth, ScaleHeight : )`

## Description

`zoom_region` enlarges or reduces the regions given in
*`Region`* in the x- and y-direction by the given scale
factors *`ScaleWidth`* and *`ScaleHeight`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Region`** (input_object)  region(-array) `→` object

Region(s) to be zoomed.

**`RegionZoom`** (output_object)  region(-array) `→` object

Zoomed region(s).

Number of elements:
RegionZoom == Region

**`ScaleWidth`** (input_control)  extent.x `→`  (real)

Scale factor in x-direction.

Default:
2.0

Suggested values:
0.25, 0.5, 1.0, 2.0, 3.0

Value range:
`0.0
≤
ScaleWidth
≤
100.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.5

**`ScaleHeight`** (input_control)  extent.y `→`  (real)

Scale factor in y-direction.

Default:
2.0

Suggested values:
0.25, 0.5, 1.0, 2.0, 3.0

Value range:
`0.0
≤
ScaleHeight
≤
100.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.5

## Possible Predecessors

`threshold`,
`connection`,
`regiongrowing`,
`pouring`

## Possible Successors

`select_shape`,
`disp_region`

## See also

`zoom_image_size`,
`zoom_image_factor`

## Module

Foundation
