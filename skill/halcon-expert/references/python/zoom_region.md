# zoom_region (Operator)

## Name

`zoom_region` — Zoom a region.

## Signature

`def zoom_region(region: HObject, scale_width: float, scale_height: float) -> HObject`

## Description

`zoom_region` enlarges or reduces the regions given in
*`region`* in the x- and y-direction by the given scale
factors *`scale_width`* and *`scale_height`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`region`** (input_object)  region(-array) `→` HObject

Region(s) to be zoomed.

**`region_zoom`** (output_object)  region(-array) `→` HObject

Zoomed region(s).

Number of elements:
RegionZoom == Region

**`scale_width`** (input_control)  extent.x `→` float

Scale factor in x-direction.

Default:
2.0

Suggested values:
0.25, 0.5, 1.0, 2.0, 3.0

Value range:
`0.0
≤
scale_width
≤
100.0` (lin)

Minimum increment:
0.01

Recommended increment:
0.5

**`scale_height`** (input_control)  extent.y `→` float

Scale factor in y-direction.

Default:
2.0

Suggested values:
0.25, 0.5, 1.0, 2.0, 3.0

Value range:
`0.0
≤
scale_height
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
