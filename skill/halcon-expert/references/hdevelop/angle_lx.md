# angle_lx (Operator)

## Name

`angle_lx` — Calculate the angle between one line and the horizontal axis.

## Signature

`angle_lx( : : Row1, Column1, Row2, Column2 : Angle)`

## Description

The operator `angle_lx` calculates the angle between one line
and the horizontal axis.
As input the coordinates of two points on the line
(*`Row1`*,*`Column1`*,
*`Row2`*,*`Column2`*) are expected.
The calculation is performed as follows: We interpret the line
as a vector with starting point
*`Row1`*,*`Column1`* and end point
*`Row2`*,*`Column2`*.
The starting point is on the horizontal axis and defines the center of
rotation in the following consideration.
If the end point is above the horizontal axis, the angle (with positive sign)
results from the rotation of the horizontal axis in counter clockwise
direction onto the vector.
If the end point is below the horizontal axis, the angle (with negative sign)
results from the rotation of the horizontal axis in clockwise
direction onto the vector.
The result depends on the order of the two points defining the line.
The parameter *`Angle`* returns the angle in radians, ranging
from $$-\pi\le\texttt{Angle}<\pi$$.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of computed angles is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`Row1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate the first point of the line.

**`Column1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the line.

**`Row2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line.

**`Column2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line.

**`Angle`** (output_control)  angle.rad(-array) `→`  (real)

Angle between the line and the horizontal axis [rad].

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
RowA1 := 255
ColumnA1 := 10
RowA2 := 255
ColumnA2 := 501
gen_contour_polygon_xld (Contour, [RowA1,RowA2], [ColumnA1,ColumnA2])
Row1 := 255
Column1 := 255
for I := 5 to 360 by 5
  Row2 := 255 - sin(rad(I)) * 200
  Column2 := 255 + cos(rad(I)) * 200
  gen_contour_polygon_xld (Contour, [Row1,Row2], [Column1,Column2])
  angle_lx (Row1, Column1, Row2, Column2, Angle)
  AngleDeg := deg(Angle)
endfor
```

## Result

`angle_lx` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`angle_ll`

## Module

Foundation
