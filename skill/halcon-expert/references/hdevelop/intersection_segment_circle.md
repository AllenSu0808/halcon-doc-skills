# intersection_segment_circle (Operator)

## Name

`intersection_segment_circle` — Calculate the intersection points of a segment and a circle or circular arc

## Signature

`intersection_segment_circle( : : SegmentRow1, SegmentColumn1, SegmentRow2, SegmentColumn2, CircleRow, CircleColumn, CircleRadius, CircleStartPhi, CircleEndPhi, CirclePointOrder : Row, Column)`

## Description

`intersection_segment_circle` calculates the intersection point of
a segment and a circle or circular arc. The segment is defined by its
endpoints (*`SegmentRow1`*,*`SegmentColumn1`*) and
(*`SegmentRow2`*,*`SegmentColumn2`*). The circle is defined
by its center (*`CircleRow`*,*`CircleColumn`*) and its radius
*`CircleRadius`*. In addition to that, a circular arc is characterized
by the angle of the start point *`CircleStartPhi`*, the angle of the
end point *`CircleEndPhi`*, and the point order
*`CirclePointOrder`* along the boundary.
If *`CirclePointOrder`* is set to *'positive'*, the circular arc
is defined counterclockwise.
If *`CirclePointOrder`* is set to *'negative'*, the circular arc
is defined clockwise.
The intersection points, if any, are returned in
(*`Row`*,*`Column`*).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SegmentRow1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the first point of the segment.

**`SegmentColumn1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the first point of the segment.

**`SegmentRow2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the second point of the segment.

**`SegmentColumn2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the second point of the segment.

**`CircleRow`** (input_control)  circle.center.y `→`  (real / integer)

Row coordinate of the center of the circle or
circular arc.

**`CircleColumn`** (input_control)  circle.center.x `→`  (real / integer)

Column coordinate of the center of the circle or
circular arc.

**`CircleRadius`** (input_control)  circle.radius `→`  (real / integer)

Radius of the circle or circular arc.

**`CircleStartPhi`** (input_control)  angle.rad `→`  (real)

Angle of the start point of the circle or
circular arc [rad].

Default:
0.0

**`CircleEndPhi`** (input_control)  angle.rad `→`  (real)

Angle of the end point of the circle or
circular arc [rad].

Default:
6.28318

**`CirclePointOrder`** (input_control)  string `→`  (string)

Point order along the circle or circular arc.

Default:
'positive'

List of values:
'negative', 'positive'

**`Row`** (output_control)  point.y(-array) `→`  (real)

Row coordinates of the intersection points.

**`Column`** (output_control)  point.x(-array) `→`  (real)

Column coordinates of the intersection points.

## Result

If the parameters are valid, the operator `intersection_segment_circle`
returns the value 2 (
H_MSG_TRUE)
.

## Alternatives

`intersection_circle_contour_xld`

## See also

`intersection_line_circle`

## Module

Foundation
