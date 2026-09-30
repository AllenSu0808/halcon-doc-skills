# IntersectionSegments (Operator)

## Name

`IntersectionSegments` — Calculate the intersection point of two line segments

## Signature

`static void HOperatorSet.IntersectionSegments(HTuple segment1Row1, HTuple segment1Column1, HTuple segment1Row2, HTuple segment1Column2, HTuple segment2Row1, HTuple segment2Column1, HTuple segment2Row2, HTuple segment2Column2, out HTuple row, out HTuple column, out HTuple isOverlapping)`

## Description

`IntersectionSegments` calculates the intersection point of two
line segments, which are defined by their endpoints
(*`segment1Row1`*,*`segment1Column1`*),
(*`segment1Row2`*,*`segment1Column2`*), and
(*`segment2Row1`*,*`segment2Column1`*),
(*`segment2Row2`*,*`segment2Column2`*) respectively.
The intersection point, if it exists, is returned in
(*`row`*,*`column`*).
If both segments have a part in common, *`isOverlapping`* returns the
value 1, otherwise 0 is returned.
In this case the endpoints of the mutual segment are
returned in (*`row`*,*`column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`segment1Row1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point
of the first segment.

**`segment1Column1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point
of the first segment.

**`segment1Row2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point
of the first segment.

**`segment1Column2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point
of the first segment.

**`segment2Row1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point
of the second segment.

**`segment2Column1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point
of the second segment.

**`segment2Row2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point
of the second segment.

**`segment2Column2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point
of the second segment.

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinate of the intersection point.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinate of the intersection point.

**`isOverlapping`** (output_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Do both segments have a part in common?

## Result

If the parameters are valid, the operator `IntersectionSegments`
returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`IntersectionSegmentContourXld`,
`IntersectionContoursXld`

## See also

`IntersectionSegmentLine`,
`IntersectionLines`,
`IntersectionLineContourXld`

## Module

Foundation
