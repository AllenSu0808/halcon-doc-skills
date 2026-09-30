# GenParallelContourXld (Operator)

## Name

`GenParallelContourXld` — Compute the parallel contour of an XLD contour.

## Signature

`static void HOperatorSet.GenParallelContourXld(HObject contours, out HObject parallelContours, HTuple mode, HTuple distance)`

`HXLDCont HXLDCont.GenParallelContourXld(string mode, HTuple distance)`

`HXLDCont HXLDCont.GenParallelContourXld(string mode, double distance)`

## Description

`GenParallelContourXld` computes for each of the input
contours *`contours`* a parallel contour with distance
*`distance`*. The resulting contours are returned in
*`parallelContours`*. To calculate the parallel contour, the
normal vector of the input contour is needed in every contour point.
The parameter *`mode`* determines how these normal vectors are
computed. If *`mode`* = *"gradient"*, it is assumed
that the input contours are edges, and the normal information is
obtained from the gradient direction of the edge (see
[`EdgesSubPix`](edges_sub_pix.md)). For this, the attribute
*"edge_direction"* must exist for the input contour
(see [`GetContourAttribXld`](get_contour_attrib_xld.md)).
If *`mode`* = *"contour_normal"*, a possibly existing
normal information is used to determine the normals. For this, the
contour attribute *"angle"* must exist (see
[`LinesGauss`](lines_gauss.md) or [`EdgesSubPix`](edges_sub_pix.md)). Finally, if
*`mode`* = *"regression_normal"*, the normal vectors are
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

**`contours`** (input_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Contours to be transformed.

**`parallelContours`** (output_object)  xld_cont-array `→` [HXLDCont](HXLDCont.md)

Parallel contours.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Mode, with which the direction information is computed.

Default:
"regression_normal"

Suggested values:
"gradient", "contour_normal", "regression_normal"

**`distance`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Distance of the parallel contour.

Default:
1

Suggested values:
0.2, 0.4, 0.6, 0.8, 1, 2, 3, 4, 5, 7, 10, 15, 20, 30, 40, 50

## Possible Predecessors

`GenContoursSkeletonXld`,
`LinesGauss`,
`LinesFacet`,
`EdgesSubPix`,
`ThresholdSubPix`

## Possible Successors

`GenPolygonsXld`

## See also

`GetContourXld`

## Module

Foundation
