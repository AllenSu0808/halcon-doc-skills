# get_contour_xld (Operator)

## Name

`get_contour_xld` — Return the coordinates of an XLD contour.

## Signature

`def get_contour_xld(contour: HObject) -> Tuple[Sequence[float], Sequence[float]]`

## Description

`get_contour_xld` returns the following values of the XLD
contour *`contour`*:

|  |  |
| --- | --- |
| *`row`* | Row coordinate of the contour's points |
| *`col`* | Column coordinate of the contour's points |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

Input XLD contour.

**`row`** (output_control)  point.y-array `→` Sequence[float]

Row coordinate of the contour's points.

**`col`** (output_control)  point.x-array `→` Sequence[float]

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
