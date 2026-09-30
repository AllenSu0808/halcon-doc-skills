# find_rectification_grid (Operator)

## Name

`find_rectification_grid` — Segment the rectification grid region in the image.

## Signature

`find_rectification_grid(Image : GridRegion : MinContrast, Radius : )`

## Description

`find_rectification_grid` searches in the image *`Image`* for
image parts that contain the rectification grid and returns them in the
region *`GridRegion`*.
To do so, essentially image areas with a contrast of
at least *`MinContrast`* are extracted and the holes in these areas
are filled up. Then, an opening with the radius *`Radius`* is applied
to these areas to eliminate smaller areas of high contrast.

During grid-rectification, a careful reduction of the input region to those
image parts that actually contain the rectification grid is useful for two
purposes:
First, the computing time can be reduced and secondly,
[`saddle_points_sub_pix`](saddle_points_sub_pix.md)
and [`connect_grid_points`](connect_grid_points.md) can be prevented from detecting false grid
points and connecting lines.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`GridRegion`** (output_object)  region `→` object

Output region containing the rectification grid.

**`MinContrast`** (input_control)  number `→`  (real / integer)

Minimum contrast.

Default:
8.0

Suggested values:
2.0, 4.0, 8.0, 16.0, 32.0

Restriction:
`MinContrast >= 0`

**`Radius`** (input_control)  real `→`  (real / integer)

Radius of the circular structuring element.

Default:
7.5

Suggested values:
1.5, 2.5, 3.5, 4.5, 5.5, 7.5, 9.5, 12.5, 15.5, 19.5, 25.5, 33.5, 45.5, 60.5, 110.5

Restriction:
`Radius >= 0.5`

## Example (HDevelop)

```
find_rectification_grid (Image, GridRegion, 8, 10)
dilation_circle (GridRegion, GridRegionDilated, 5.5)
reduce_domain (Image, GridRegionDilated, ImageReduced)
saddle_points_sub_pix (ImageReduced, 'facet', 1.5, 5, Row, Column)
connect_grid_points (ImageReduced, ConnectingLines, Row, Column, 1.1, 5.5)
gen_grid_rectification_map (ImageReduced, ConnectingLines, Map, Meshes, 20, \
                            'auto', Row, Column, 'bilinear')
map_image (Image, Map, ImageMapped)
```

## Result

`find_rectification_grid` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct. If necessary, an exception is raised.

## Possible Successors

`dilation_circle`,
`reduce_domain`

## Module

Calibration
