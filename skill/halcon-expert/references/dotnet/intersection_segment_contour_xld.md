# IntersectionSegmentContourXld (Operator)

## Name

`IntersectionSegmentContourXld` — Calculate the intersection points of a segment and an XLD contour

## Signature

`static void HOperatorSet.IntersectionSegmentContourXld(HObject contour, HTuple segmentRow1, HTuple segmentColumn1, HTuple segmentRow2, HTuple segmentColumn2, out HTuple row, out HTuple column, out HTuple isOverlapping)`

## Description

`IntersectionSegmentContourXld` calculates the intersection points
of a segment and an XLD *`contour`*. The segment is defined by its
endpoints (*`segmentRow1`*,*`segmentColumn1`*) and
(*`segmentRow2`*,*`segmentColumn2`*).
The intersection points, if any, are returned in
(*`row`*,*`column`*).
If the segment and the XLD contour have a part in common
*`isOverlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the mutual
segment are returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

XLD contour.

**`segmentRow1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the segment.

**`segmentColumn1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the segment.

**`segmentRow2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the segment.

**`segmentColumn2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the segment.

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the intersection points.

**`isOverlapping`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Do the segment and the XLD contour have a part in common?

## Result

If the parameters are valid, the operator
`IntersectionSegmentContourXld` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`IntersectionSegments`,
`IntersectionContoursXld`

## See also

`IntersectionSegmentLine`,
`IntersectionLines`,
`IntersectionLineContourXld`

## Module

Foundation
