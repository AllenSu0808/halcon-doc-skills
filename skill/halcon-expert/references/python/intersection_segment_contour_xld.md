# intersection_segment_contour_xld (Operator)

## Name

`intersection_segment_contour_xld` — Calculate the intersection points of a segment and an XLD contour

## Signature

`def intersection_segment_contour_xld(contour: HObject, segment_row_1: Union[float, int], segment_column_1: Union[float, int], segment_row_2: Union[float, int], segment_column_2: Union[float, int]) -> Tuple[Sequence[float], Sequence[float], int]`

`def intersection_segment_contour_xld_s(contour: HObject, segment_row_1: Union[float, int], segment_column_1: Union[float, int], segment_row_2: Union[float, int], segment_column_2: Union[float, int]) -> Tuple[float, float, int]`

## Description

`intersection_segment_contour_xld` calculates the intersection points
of a segment and an XLD *`contour`*. The segment is defined by its
endpoints (*`segment_row_1`*,*`segment_column_1`*) and
(*`segment_row_2`*,*`segment_column_2`*).
The intersection points, if any, are returned in
(*`row`*,*`column`*).
If the segment and the XLD contour have a part in common
*`is_overlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual
segment are returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

XLD contour.

**`segment_row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point of the segment.

**`segment_column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point of the segment.

**`segment_row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point of the segment.

**`segment_column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point of the segment.

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinates of the intersection points.

**`is_overlapping`** (output_control)  integer `→` int

Do the segment and the XLD contour have a part in common?

## Result

If the parameters are valid, the operator
`intersection_segment_contour_xld` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`intersection_segments`,
`intersection_contours_xld`

## See also

`intersection_segment_line`,
`intersection_lines`,
`intersection_line_contour_xld`

## Module

Foundation
