# intersection_line_contour_xld (Operator)

## Name

`intersection_line_contour_xld` — Calculate the intersection points of a line and an XLD contour

## Signature

`intersection_line_contour_xld(Contour : : LineRow1, LineColumn1, LineRow2, LineColumn2 : Row, Column, IsOverlapping)`

## Description

`intersection_line_contour_xld` calculates the intersection points
of a line and an XLD *`Contour`*. The line is defined by the points
(*`LineRow1`*,*`LineColumn1`*) and
(*`LineRow2`*,*`LineColumn2`*).
The intersection points, if any, are returned in
(*`Row`*,*`Column`*).
If a part of the XLD contour lies on the line
*`IsOverlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the XLD segment
are returned in (*`Row`*,*`Column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (input_object)  xld_cont `→` object

XLD contour.

**`LineRow1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point of the line.

**`LineColumn1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point of the line.

**`LineRow2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point of the line.

**`LineColumn2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point of the line.

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinates of the intersection points.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinates of the intersection points.

**`IsOverlapping`** (output_control)  integer `→`  (integer)

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
