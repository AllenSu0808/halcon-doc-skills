# IntersectionLines (Operator)

## Name

`IntersectionLines` — Calculate the intersection point of two lines

## Signature

`static void HOperatorSet.IntersectionLines(HTuple line1Row1, HTuple line1Column1, HTuple line1Row2, HTuple line1Column2, HTuple line2Row1, HTuple line2Column1, HTuple line2Row2, HTuple line2Column2, out HTuple row, out HTuple column, out HTuple isOverlapping)`

## Description

`IntersectionLines` calculates the intersection point of two
lines, which are defined by two of their points
(*`line1Row1`*,*`line1Column1`*),
(*`line1Row2`*,*`line1Column2`*), and
(*`line2Row1`*,*`line2Column1`*),
(*`line2Row2`*,*`line2Column2`*) respectively.
The intersection point, if it exists, is returned in
(*`row`*,*`column`*).
If both lines are identical, *`isOverlapping`* returns the
value 1, otherwise 0 is returned. In this case no intersection point is
returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`line1Row1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the first line.

**`line1Column1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the first line.

**`line1Row2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the first line.

**`line1Column2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the first line.

**`line2Row1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the second line.

**`line2Column1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the second line.

**`line2Row2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the second line.

**`line2Column2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the second line.

**`row`** (output_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the intersection point.

**`column`** (output_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the intersection point.

**`isOverlapping`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Are both lines identical?

## Result

If the parameters are valid, the operator `IntersectionLines`
returns the value 2 (
H_MSG_TRUE)
.

## See also

`IntersectionSegments`,
`IntersectionSegmentLine`,
`IntersectionSegmentContourXld`,
`IntersectionLineContourXld`,
`IntersectionContoursXld`

## Module

Foundation
