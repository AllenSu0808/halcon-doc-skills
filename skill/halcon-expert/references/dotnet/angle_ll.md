# AngleLl (Operator)

## Name

`AngleLl` — Calculate the angle between two lines.

## Signature

`static void HOperatorSet.AngleLl(HTuple rowA1, HTuple columnA1, HTuple rowA2, HTuple columnA2, HTuple rowB1, HTuple columnB1, HTuple rowB2, HTuple columnB2, out HTuple angle)`

`static HTuple HMisc.AngleLl(HTuple rowA1, HTuple columnA1, HTuple rowA2, HTuple columnA2, HTuple rowB1, HTuple columnB1, HTuple rowB2, HTuple columnB2)`

`static double HMisc.AngleLl(double rowA1, double columnA1, double rowA2, double columnA2, double rowB1, double columnB1, double rowB2, double columnB2)`

## Description

The operator `AngleLl` calculates the angle between two lines.
As input the coordinates of two points on the first line
(*`rowA1`*,*`columnA1`*,
*`rowA2`*,*`columnA2`*) and on the second line
(*`rowB1`*,*`columnB1`*,
*`rowB2`*,*`columnB2`*) are expected.
The calculation is performed as follows: We interpret the lines
as vectors with starting points
*`rowA1`*,*`columnA1`* and
*`rowB1`*,*`columnB1`* and end points
*`rowA2`*,*`columnA2`* and
*`rowB2`*,*`columnB2`*, respectively.
Rotating the vector A counter clockwise onto the
vector B (the center of rotation
is the intersection point of the two lines) yields the angle.
The result depends on the order of the points and on the
order of the lines.
The parameter *`angle`* returns the angle in radians,
ranging from $$-\pi\le\texttt{Angle}\le\pi$$.

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

**`rowA1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the first line.

**`columnA1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the first
line.

**`rowA2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the first line.

**`columnA2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the first
line.

**`rowB1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the second line.

**`columnB1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the second
line.

**`rowB2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the second line.

**`columnB2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the second
line.

**`angle`** (output_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double*)

Angle between the lines [rad].

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
RowA1 := 255
ColumnA1 := 10
RowA2 := 255
ColumnA2 := 501
gen_contour_polygon_xld (Contour, [RowA1,RowA2], [ColumnA1,ColumnA2])
RowB1 := 255
ColumnB1 := 255
for I := 5 to 360 by 5
  RowB2 := 255 - sin(rad(I)) * 200
  ColumnB2 := 255 + cos(rad(I)) * 200
  gen_contour_polygon_xld (Contour, [RowB1,RowB2], [ColumnB1,ColumnB2])
  angle_ll (RowA1, ColumnA1, RowA2, ColumnA2,\
            RowB1, ColumnB1, RowB2, ColumnB2, Angle)
  AngleDeg := deg(Angle)
endfor
```

## Result

`AngleLl` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`AngleLx`

## Module

Foundation
