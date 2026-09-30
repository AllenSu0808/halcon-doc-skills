# intersection_lines (Operator)

## Name

`intersection_lines` — Calculate the intersection point of two lines

## Signature

`def intersection_lines(line_1row_1: Union[float, int], line_1column_1: Union[float, int], line_1row_2: Union[float, int], line_1column_2: Union[float, int], line_2row_1: Union[float, int], line_2column_1: Union[float, int], line_2row_2: Union[float, int], line_2column_2: Union[float, int]) -> Tuple[float, float, int]`

## Description

`intersection_lines` calculates the intersection point of two
lines, which are defined by two of their points
(*`line_1row_1`*,*`line_1column_1`*),
(*`line_1row_2`*,*`line_1column_2`*), and
(*`line_2row_1`*,*`line_2column_1`*),
(*`line_2row_2`*,*`line_2column_2`*) respectively.
The intersection point, if it exists, is returned in
(*`row`*,*`column`*).
If both lines are identical, *`is_overlapping`* returns the
value 1, otherwise 0 is returned. In this case no intersection point is
returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`line_1row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point of the first line.

**`line_1column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point of the first line.

**`line_1row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point of the first line.

**`line_1column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point of the first line.

**`line_2row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point of the second line.

**`line_2column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point of the second line.

**`line_2row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point of the second line.

**`line_2column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point of the second line.

**`row`** (output_control)  point.y `→` float

Row coordinate of the intersection point.

**`column`** (output_control)  point.x `→` float

Column coordinate of the intersection point.

**`is_overlapping`** (output_control)  integer `→` int

Are both lines identical?

## Result

If the parameters are valid, the operator `intersection_lines`
returns the value 2 (
H_MSG_TRUE)
.

## See also

`intersection_segments`,
`intersection_segment_line`,
`intersection_segment_contour_xld`,
`intersection_line_contour_xld`,
`intersection_contours_xld`

## Module

Foundation
