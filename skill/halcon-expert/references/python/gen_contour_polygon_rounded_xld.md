# gen_contour_polygon_rounded_xld (Operator)

## Name

`gen_contour_polygon_rounded_xld` — Generate an XLD contour with rounded corners from a polygon (given
as tuples).

## Signature

`def gen_contour_polygon_rounded_xld(row: Sequence[Union[float, int]], col: Sequence[Union[float, int]], radius: Sequence[Union[float, int]], sampling_interval: Union[float, int]) -> HObject`

## Description

`gen_contour_polygon_rounded_xld` generates an XLD contour
*`contour`* with rounded corners from a polygon given in the
tuples *`row`* and *`col`*. The rounded corners are created in
form of arcs defined by *`radius`*. For every specified point of the
polygon there must be a corresponding rounding radius defined. In
case of a closed polygon the first and the last point have to be
defined identical with the radii of these points being equal. In
contrast, the radii of the first and last point of open polygons are
ignored. Finally, the *`sampling_interval`* parameter defines the
distance of the control points of the formed contour
*`contour`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (output_object)  xld_cont `→` HObject

Resulting contour.

**`row`** (input_control)  coordinates.y-array `→` Sequence[Union[float, int]]

Row coordinates of the polygon.

Default:
[20,80,80,20,20]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

**`col`** (input_control)  coordinates.x-array `→` Sequence[Union[float, int]]

Column coordinates of the polygon.

Default:
[20,20,80,80,20]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

**`radius`** (input_control)  number-array `→` Sequence[Union[float, int]]

Radii of the rounded corners.

Default:
[20,20,20,20,20]

Suggested values:
0, 1, 2, 5, 10, 20, 50

**`sampling_interval`** (input_control)  number `→` Union[float, int]

Distance of the samples.

Default:
1.0

Suggested values:
0.5, 1.0, 2.0, 5.0

## Possible Predecessors

`get_region_contour`

## Possible Successors

`smooth_contours_xld`,
`gen_polygons_xld`

## See also

`gen_contour_polygon_xld`,
`gen_contours_skeleton_xld`

## Module

Foundation
