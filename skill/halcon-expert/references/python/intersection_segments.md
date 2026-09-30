# intersection_segments (Operator)

## Name

`intersection_segments` — Calculate the intersection point of two line segments

## Signature

`def intersection_segments(segment_1row_1: Union[float, int], segment_1column_1: Union[float, int], segment_1row_2: Union[float, int], segment_1column_2: Union[float, int], segment_2row_1: Union[float, int], segment_2column_1: Union[float, int], segment_2row_2: Union[float, int], segment_2column_2: Union[float, int]) -> Tuple[Sequence[float], Sequence[float], int]`

`def intersection_segments_s(segment_1row_1: Union[float, int], segment_1column_1: Union[float, int], segment_1row_2: Union[float, int], segment_1column_2: Union[float, int], segment_2row_1: Union[float, int], segment_2column_1: Union[float, int], segment_2row_2: Union[float, int], segment_2column_2: Union[float, int]) -> Tuple[float, float, int]`

## Description

`intersection_segments` calculates the intersection point of two
line segments, which are defined by their endpoints
(*`segment_1row_1`*,*`segment_1column_1`*),
(*`segment_1row_2`*,*`segment_1column_2`*), and
(*`segment_2row_1`*,*`segment_2column_1`*),
(*`segment_2row_2`*,*`segment_2column_2`*) respectively.
The intersection point, if it exists, is returned in
(*`row`*,*`column`*).
If both segments have a part in common, *`is_overlapping`* returns the
value 1, otherwise 0 is returned.
In this case the endpoints of the mutual segment are
returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`segment_1row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point
of the first segment.

**`segment_1column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point
of the first segment.

**`segment_1row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point
of the first segment.

**`segment_1column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point
of the first segment.

**`segment_2row_1`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the first point
of the second segment.

**`segment_2column_1`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the first point
of the second segment.

**`segment_2row_2`** (input_control)  point.y `→` Union[float, int]

Row coordinate of the second point
of the second segment.

**`segment_2column_2`** (input_control)  point.x `→` Union[float, int]

Column coordinate of the second point
of the second segment.

**`row`** (output_control)  point.y(-array) `→` Sequence[float]

Row coordinate of the intersection point.

**`column`** (output_control)  point.x(-array) `→` Sequence[float]

Column coordinate of the intersection point.

**`is_overlapping`** (output_control)  integer `→` int

Do both segments have a part in common?

## Result

If the parameters are valid, the operator `intersection_segments`
returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`intersection_segment_contour_xld`,
`intersection_contours_xld`

## See also

`intersection_segment_line`,
`intersection_lines`,
`intersection_line_contour_xld`

## Module

Foundation
