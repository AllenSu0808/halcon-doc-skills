# intersection_lines (Operator)

## Name

`intersection_lines` — Calculate the intersection point of two lines

## Signature

`intersection_lines( : : Line1Row1, Line1Column1, Line1Row2, Line1Column2, Line2Row1, Line2Column1, Line2Row2, Line2Column2 : Row, Column, IsOverlapping)`

## Description

`intersection_lines` calculates the intersection point of two
lines, which are defined by two of their points
(*`Line1Row1`*,*`Line1Column1`*),
(*`Line1Row2`*,*`Line1Column2`*), and
(*`Line2Row1`*,*`Line2Column1`*),
(*`Line2Row2`*,*`Line2Column2`*) respectively.
The intersection point, if it exists, is returned in
(*`Row`*,*`Column`*).
If both lines are identical, *`IsOverlapping`* returns the
value 1, otherwise 0 is returned. In this case no intersection point is
returned in (*`Row`*,*`Column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Line1Row1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point of the first line.

**`Line1Column1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point of the first line.

**`Line1Row2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point of the first line.

**`Line1Column2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point of the first line.

**`Line2Row1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point of the second line.

**`Line2Column1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point of the second line.

**`Line2Row2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point of the second line.

**`Line2Column2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point of the second line.

**`Row`** (output_control)  point.y `→`  (real)

Row coordinate of the intersection point.

**`Column`** (output_control)  point.x `→`  (real)

Column coordinate of the intersection point.

**`IsOverlapping`** (output_control)  integer `→`  (integer)

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
