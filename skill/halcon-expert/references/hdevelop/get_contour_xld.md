# get_contour_xld (Operator)

## Name

`get_contour_xld` — Return the coordinates of an XLD contour.

## Signature

`get_contour_xld(Contour : : : Row, Col)`

## Description

`get_contour_xld` returns the following values of the XLD
contour *`Contour`*:

|  |  |
| --- | --- |
| *`Row`* | Row coordinate of the contour's points |
| *`Col`* | Column coordinate of the contour's points |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (input_object)  xld_cont `→` object

Input XLD contour.

**`Row`** (output_control)  point.y-array `→`  (real)

Row coordinate of the contour's points.

**`Col`** (output_control)  point.x-array `→`  (real)

Column coordinate of the contour's points.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## See also

`get_contour_attrib_xld`,
`query_contour_attribs_xld`,
`get_contour_global_attrib_xld`,
`query_contour_global_attribs_xld`,
`gen_contour_polygon_xld`

## Module

Foundation
