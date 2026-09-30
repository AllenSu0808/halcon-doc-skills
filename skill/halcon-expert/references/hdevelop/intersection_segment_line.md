# intersection_segment_line (Operator)

## Name

`intersection_segment_line` — Calculate the intersection point of a segment and a line

## Signature

`intersection_segment_line( : : SegmentRow1, SegmentColumn1, SegmentRow2, SegmentColumn2, LineRow1, LineColumn1, LineRow2, LineColumn2 : Row, Column, IsOverlapping)`

## Description

`intersection_segment_line` calculates the intersection point of a
segment and a line. The segment is defined by its endpoints
(*`SegmentRow1`*,*`SegmentColumn1`*) and
(*`SegmentRow2`*,*`SegmentColumn2`*). The line is defined by
the two points (*`LineRow1`*,*`LineColumn1`*) and
(*`LineRow2`*,*`LineColumn2`*).
The intersection point, if it exists, is returned in
(*`Row`*,*`Column`*).
If the segment and the line have a part in common, *`IsOverlapping`*
returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual
segment are returned in (*`Row`*,*`Column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SegmentRow1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point of the segment.

**`SegmentColumn1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point of the segment.

**`SegmentRow2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point of the segment.

**`SegmentColumn2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point of the segment.

**`LineRow1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point of the line.

**`LineColumn1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point of the line.

**`LineRow2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point of the line.

**`LineColumn2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point of the line.

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the intersection point.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the intersection point.

**`IsOverlapping`** (output_control)  integer `→`  (integer)

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
