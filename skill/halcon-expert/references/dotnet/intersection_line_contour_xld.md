# IntersectionLineContourXld (Operator)

## Name

`IntersectionLineContourXld` — Calculate the intersection points of a line and an XLD contour

## Signature

`static void HOperatorSet.IntersectionLineContourXld(HObject contour, HTuple lineRow1, HTuple lineColumn1, HTuple lineRow2, HTuple lineColumn2, out HTuple row, out HTuple column, out HTuple isOverlapping)`

## Description

`IntersectionLineContourXld` calculates the intersection points
of a line and an XLD *`contour`*. The line is defined by the points
(*`lineRow1`*,*`lineColumn1`*) and
(*`lineRow2`*,*`lineColumn2`*).
The intersection points, if any, are returned in
(*`row`*,*`column`*).
If a part of the XLD contour lies on the line
*`isOverlapping`* returns the value 1, otherwise 0 is returned.
In this case the endpoints of the XLD segment
are returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

XLD contour.

**`lineRow1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line.

**`lineColumn1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line.

**`lineRow2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line.

**`lineColumn2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line.

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the intersection points.

**`isOverlapping`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Does a part of the XLD contour lie on the line?

## Result

If the parameters are valid, the operator
`IntersectionLineContourXld` returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`IntersectionSegmentLine`

## See also

`IntersectionSegments`,
`IntersectionLines`,
`IntersectionSegmentContourXld`,
`IntersectionContoursXld`

## Module

Foundation
