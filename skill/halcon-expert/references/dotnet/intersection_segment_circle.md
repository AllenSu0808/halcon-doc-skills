# IntersectionSegmentCircle (Operator)

## Name

`IntersectionSegmentCircle` — Calculate the intersection points of a segment and a circle or circular arc

## Signature

`static void HOperatorSet.IntersectionSegmentCircle(HTuple segmentRow1, HTuple segmentColumn1, HTuple segmentRow2, HTuple segmentColumn2, HTuple circleRow, HTuple circleColumn, HTuple circleRadius, HTuple circleStartPhi, HTuple circleEndPhi, HTuple circlePointOrder, out HTuple row, out HTuple column)`

## Description

`IntersectionSegmentCircle` calculates the intersection point of
a segment and a circle or circular arc. The segment is defined by its
endpoints (*`segmentRow1`*,*`segmentColumn1`*) and
(*`segmentRow2`*,*`segmentColumn2`*). The circle is defined
by its center (*`circleRow`*,*`circleColumn`*) and its radius
*`circleRadius`*. In addition to that, a circular arc is characterized
by the angle of the start point *`circleStartPhi`*, the angle of the
end point *`circleEndPhi`*, and the point order
*`circlePointOrder`* along the boundary.
If *`circlePointOrder`* is set to *"positive"*, the circular arc
is defined counterclockwise.
If *`circlePointOrder`* is set to *"negative"*, the circular arc
is defined clockwise.
The intersection points, if any, are returned in
(*`row`*,*`column`*).

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

**`circleRow`** (input_control)  circle.center.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the center of the circle or
circular arc.

**`circleColumn`** (input_control)  circle.center.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the center of the circle or
circular arc.

**`circleRadius`** (input_control)  circle.radius `→` [HTuple](HTuple.md) (*double* / int / long)

Radius of the circle or circular arc.

**`circleStartPhi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the start point of the circle or
circular arc [rad].

Default:
0.0

**`circleEndPhi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Angle of the end point of the circle or
circular arc [rad].

Default:
6.28318

**`circlePointOrder`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Point order along the circle or circular arc.

Default:
"positive"

List of values:
"negative", "positive"

**`row`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Row coordinates of the intersection points.

**`column`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Column coordinates of the intersection points.

## Result

If the parameters are valid, the operator `IntersectionSegmentCircle`
returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`IntersectionCircleContourXld`

## See also

`IntersectionLineCircle`

## Module

Foundation
