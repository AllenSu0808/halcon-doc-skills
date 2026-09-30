# gen_parallel_contour_xld (Operator)

## Name

`gen_parallel_contour_xld` — Compute the parallel contour of an XLD contour.

## Signature

`gen_parallel_contour_xld(Contours : ParallelContours : Mode, Distance : )`

## Description

`gen_parallel_contour_xld` computes for each of the input
contours *`Contours`* a parallel contour with distance
*`Distance`*. The resulting contours are returned in
*`ParallelContours`*. To calculate the parallel contour, the
normal vector of the input contour is needed in every contour point.
The parameter *`Mode`* determines how these normal vectors are
computed. If *`Mode`* = *'gradient'*, it is assumed
that the input contours are edges, and the normal information is
obtained from the gradient direction of the edge (see
[`edges_sub_pix`](edges_sub_pix.md)). For this, the attribute
*'edge_direction'* must exist for the input contour
(see [`get_contour_attrib_xld`](get_contour_attrib_xld.md)).
If *`Mode`* = *'contour_normal'*, a possibly existing
normal information is used to determine the normals. For this, the
contour attribute *'angle'* must exist (see
[`lines_gauss`](lines_gauss.md) or [`edges_sub_pix`](edges_sub_pix.md)). Finally, if
*`Mode`* = *'regression_normal'*, the normal vectors are
determined from a local line fit to each contour point. Here, the
normal vectors are oriented such that they point to the right side
of the contour when the contour is traversed from start to end. In
contrast to the first two modes, this mode can be used for all XLD
contours, no matter how they were generated.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contours`** (input_object)  xld_cont-array `→` object

Contours to be transformed.

**`ParallelContours`** (output_object)  xld_cont-array `→` object

Parallel contours.

**`Mode`** (input_control)  string `→`  (string)

Mode, with which the direction information is computed.

Default:
'regression_normal'

Suggested values:
'gradient', 'contour_normal', 'regression_normal'

**`Distance`** (input_control)  number `→`  (real / integer)

Distance of the parallel contour.

Default:
1

Suggested values:
0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5, 7, 10, 15, 20, 30, 40, 50

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`,
`threshold_sub_pix`

## Possible Successors

`gen_polygons_xld`

## See also

`get_contour_xld`

## Module

Foundation
