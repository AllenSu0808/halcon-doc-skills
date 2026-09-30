# intersection_segments (Operator)

## Name

`intersection_segments` — Calculate the intersection point of two line segments

## Signature

`intersection_segments( : : Segment1Row1, Segment1Column1, Segment1Row2, Segment1Column2, Segment2Row1, Segment2Column1, Segment2Row2, Segment2Column2 : Row, Column, IsOverlapping)`

## Description

`intersection_segments` calculates the intersection point of two
line segments, which are defined by their endpoints
(*`Segment1Row1`*,*`Segment1Column1`*),
(*`Segment1Row2`*,*`Segment1Column2`*), and
(*`Segment2Row1`*,*`Segment2Column1`*),
(*`Segment2Row2`*,*`Segment2Column2`*) respectively.
The intersection point, if it exists, is returned in
(*`Row`*,*`Column`*).
If both segments have a part in common, *`IsOverlapping`* returns the
value 1, otherwise 0 is returned.
In this case the endpoints of the mutual segment are
returned in (*`Row`*,*`Column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Segment1Row1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point
of the first segment.

**`Segment1Column1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point
of the first segment.

**`Segment1Row2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point
of the first segment.

**`Segment1Column2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point
of the first segment.

**`Segment2Row1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point
of the second segment.

**`Segment2Column1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point
of the second segment.

**`Segment2Row2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point
of the second segment.

**`Segment2Column2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point
of the second segment.

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinate of the intersection point.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinate of the intersection point.

**`IsOverlapping`** (output_control)  integer `→`  (integer)

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
