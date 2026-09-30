# intersection_line_contour_xld (Operator)

## Name

`intersection_line_contour_xld` — Calculate the intersection points of a line and an XLD contour

## Signature

`def intersection_line_contour_xld(contour: HObject, line_row_1: Union[float, int], line_column_1: Union[float, int], line_row_2: Union[float, int], line_column_2: Union[float, int]) -> Tuple[Sequence[float], Sequence[float], int]`

`def intersection_line_contour_xld_s(contour: HObject, line_row_1: Union[float, int], line_column_1: Union[float, int], line_row_2: Union[float, int], line_column_2: Union[float, int]) -> Tuple[float, float, int]`

## Description

`intersection_line_contour_xld` calculates the intersection points
of a line and an XLD *`contour`*. The line is defined by the points
(*`line_row_1`*,*`line_column_1`*) and
(*`line_row_2`*,*`line_column_2`*).
The intersection points, if any, are returned in
(*`row`*,*`column`*).
If a part of the XLD contour lies on the line
*`is_overlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the XLD segment
are returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` HObject

XLD contour.

**`line_row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point of the line.

**`line_column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point of the line.

**`line_row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point of the line.

**`line_column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point of the line.

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinates of the intersection points.

**`is_overlapping`** (output_control)  integer `→` int

Does a part of the XLD contour lie on the line?

## Result

If the parameters are valid, the operator
`intersection_line_contour_xld` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`intersection_segment_line`

## See also

`intersection_segments`,
`intersection_lines`,
`intersection_segment_contour_xld`,
`intersection_contours_xld`

## Module

Foundation
