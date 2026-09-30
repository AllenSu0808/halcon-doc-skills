# intersection_segment_contour_xld (Operator)

## Name

`intersection_segment_contour_xld` — Calculate the intersection points of a segment and an XLD contour

## Signature

`intersection_segment_contour_xld(Contour : : SegmentRow1, SegmentColumn1, SegmentRow2, SegmentColumn2 : Row, Column, IsOverlapping)`

## Description

`intersection_segment_contour_xld` calculates the intersection points
of a segment and an XLD *`Contour`*. The segment is defined by its
endpoints (*`SegmentRow1`*,*`SegmentColumn1`*) and
(*`SegmentRow2`*,*`SegmentColumn2`*).
The intersection points, if any, are returned in
(*`Row`*,*`Column`*).
If the segment and the XLD contour have a part in common
*`IsOverlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual
segment are returned in (*`Row`*,*`Column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (input_object)  xld_cont `→` object

XLD contour.

**`SegmentRow1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point of the segment.

**`SegmentColumn1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point of the segment.

**`SegmentRow2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point of the segment.

**`SegmentColumn2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point of the segment.

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinates of the intersection points.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinates of the intersection points.

**`IsOverlapping`** (output_control)  integer `→`  (integer)

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
