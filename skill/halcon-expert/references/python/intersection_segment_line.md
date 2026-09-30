# intersection_segment_line (Operator)

## Name

`intersection_segment_line` — Calculate the intersection point of a segment and a line

## Signature

`def intersection_segment_line(segment_row_1: Union[float, int], segment_column_1: Union[float, int], segment_row_2: Union[float, int], segment_column_2: Union[float, int], line_row_1: Union[float, int], line_column_1: Union[float, int], line_row_2: Union[float, int], line_column_2: Union[float, int]) -> Tuple[Sequence[float], Sequence[float], int]`

`def intersection_segment_line_s(segment_row_1: Union[float, int], segment_column_1: Union[float, int], segment_row_2: Union[float, int], segment_column_2: Union[float, int], line_row_1: Union[float, int], line_column_1: Union[float, int], line_row_2: Union[float, int], line_column_2: Union[float, int]) -> Tuple[float, float, int]`

## Description

`intersection_segment_line` calculates the intersection point of a
segment and a line. The segment is defined by its endpoints
(*`segment_row_1`*,*`segment_column_1`*) and
(*`segment_row_2`*,*`segment_column_2`*). The line is defined by
the two points (*`line_row_1`*,*`line_column_1`*) and
(*`line_row_2`*,*`line_column_2`*).
The intersection point, if it exists, is returned in
(*`row`*,*`column`*).
If the segment and the line have a part in common, *`is_overlapping`*
returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual
segment are returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`segment_row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point of the segment.

**`segment_column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point of the segment.

**`segment_row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point of the segment.

**`segment_column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point of the segment.

**`line_row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point of the line.

**`line_column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point of the line.

**`line_row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point of the line.

**`line_column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point of the line.

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinate of the intersection point.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinate of the intersection point.

**`is_overlapping`** (output_control)  integer `→` int

Do the segment and the line have a part in common?

## Result

If the parameters are valid, the operator `intersection_segment_line`
returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`intersection_line_contour_xld`

## See also

`intersection_segments`,
`intersection_lines`,
`intersection_segment_contour_xld`,
`intersection_contours_xld`

## Module

Foundation
