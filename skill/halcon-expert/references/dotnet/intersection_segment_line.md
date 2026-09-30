# IntersectionSegmentLine (Operator)

## Name

`IntersectionSegmentLine` — Calculate the intersection point of a segment and a line

## Signature

`static void HOperatorSet.IntersectionSegmentLine(HTuple segmentRow1, HTuple segmentColumn1, HTuple segmentRow2, HTuple segmentColumn2, HTuple lineRow1, HTuple lineColumn1, HTuple lineRow2, HTuple lineColumn2, out HTuple row, out HTuple column, out HTuple isOverlapping)`

## Description

`IntersectionSegmentLine` calculates the intersection point of a
segment and a line. The segment is defined by its endpoints
(*`segmentRow1`*,*`segmentColumn1`*) and
(*`segmentRow2`*,*`segmentColumn2`*). The line is defined by
the two points (*`lineRow1`*,*`lineColumn1`*) and
(*`lineRow2`*,*`lineColumn2`*).
The intersection point, if it exists, is returned in
(*`row`*,*`column`*).
If the segment and the line have a part in common, *`isOverlapping`*
returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual
segment are returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`segmentRow1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the segment.

**`segmentColumn1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the segment.

**`segmentRow2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the segment.

**`segmentColumn2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the segment.

**`lineRow1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line.

**`lineColumn1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line.

**`lineRow2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line.

**`lineColumn2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line.

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the intersection point.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the intersection point.

**`isOverlapping`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Do the segment and the line have a part in common?

## Result

If the parameters are valid, the operator `IntersectionSegmentLine`
returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`IntersectionLineContourXld`

## See also

`IntersectionSegments`,
`IntersectionLines`,
`IntersectionSegmentContourXld`,
`IntersectionContoursXld`

## Module

Foundation
