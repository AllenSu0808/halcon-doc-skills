# contour_point_num_xld (Operator)

## Name

`contour_point_num_xld` — Return the number of points in an XLD contour.

## Signature

`def contour_point_num_xld(contour: HObject) -> Sequence[int]`

`def contour_point_num_xld_s(contour: HObject) -> int`

## Description

`contour_point_num_xld` returns the length of the input
contour *`contour`*, i.e., its number of points, in
*`length`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont(-array) `→` HObject

Input XLD contour.

**`length`** (output_control)  integer(-array) `→` Sequence[int]

Number of contour points.

## Possible Predecessors

`gen_contours_skeleton_xld`,
`lines_gauss`,
`lines_facet`,
`edges_sub_pix`

## Possible Successors

`get_contour_xld`,
`get_contour_attrib_xld`

## Alternatives

`get_regress_params_xld`

## See also

`query_contour_attribs_xld`

## Module

Foundation
