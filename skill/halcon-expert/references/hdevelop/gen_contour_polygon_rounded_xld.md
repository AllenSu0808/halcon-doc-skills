# gen_contour_polygon_rounded_xld (Operator)

## Name

`gen_contour_polygon_rounded_xld` — Generate an XLD contour with rounded corners from a polygon (given
as tuples).

## Signature

`gen_contour_polygon_rounded_xld( : Contour : Row, Col, Radius, SamplingInterval : )`

## Description

`gen_contour_polygon_rounded_xld` generates an XLD contour
*`Contour`* with rounded corners from a polygon given in the
tuples *`Row`* and *`Col`*. The rounded corners are created in
form of arcs defined by *`Radius`*. For every specified point of the
polygon there must be a corresponding rounding radius defined. In
case of a closed polygon the first and the last point have to be
defined identical with the radii of these points being equal. In
contrast, the radii of the first and last point of open polygons are
ignored. Finally, the *`SamplingInterval`* parameter defines the
distance of the control points of the formed contour
*`Contour`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (output_object)  xld_cont `→` object

Resulting contour.

**`Row`** (input_control)  coordinates.y-array `→`  (real / integer)

Row coordinates of the polygon.

Default:
[20,80,80,20,20]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

**`Col`** (input_control)  coordinates.x-array `→`  (real / integer)

Column coordinates of the polygon.

Default:
[20,20,80,80,20]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

**`Radius`** (input_control)  number-array `→`  (real / integer)

Radii of the rounded corners.

Default:
[20,20,20,20,20]

Suggested values:
0, 1, 2, 5, 10, 20, 50

**`SamplingInterval`** (input_control)  number `→`  (real / integer)

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
