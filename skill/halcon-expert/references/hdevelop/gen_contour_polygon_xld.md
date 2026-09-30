# gen_contour_polygon_xld (Operator)

## Name

`gen_contour_polygon_xld` — Generate an XLD contour from a polygon (given as tuples).

## Signature

`gen_contour_polygon_xld( : Contour : Row, Col : )`

## Description

`gen_contour_polygon_xld` generates an XLD contour
*`Contour`* from a polygon given in the tuples *`Row`*
and *`Col`*. This operator is useful if contours have been
obtained from routines outside the core library, but higher level
operators, e.g., polygon approximation and extraction of parallels,
are to be performed on the contours.

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
[0,1,2,2,2]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

**`Col`** (input_control)  coordinates.x-array `→`  (real / integer)

Column coordinates of the polygon.

Default:
[0,0,0,1,2]

Suggested values:
0, 1, 2, 3, 4, 5, 10, 20, 50, 100, 200, 500

## Possible Predecessors

`get_region_contour`

## Possible Successors

`smooth_contours_xld`,
`gen_polygons_xld`

## See also

`gen_contours_skeleton_xld`,
`get_contour_xld`

## Module

Foundation
