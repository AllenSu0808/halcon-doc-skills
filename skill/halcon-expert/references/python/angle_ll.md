# angle_ll (Operator)

## Name

`angle_ll` — Calculate the angle between two lines.

## Signature

`def angle_ll(row_a1: MaybeSequence[Union[float, int]], column_a1: MaybeSequence[Union[float, int]], row_a2: MaybeSequence[Union[float, int]], column_a2: MaybeSequence[Union[float, int]], row_b1: MaybeSequence[Union[float, int]], column_b1: MaybeSequence[Union[float, int]], row_b2: MaybeSequence[Union[float, int]], column_b2: MaybeSequence[Union[float, int]]) -> Sequence[float]`

`def angle_ll_s(row_a1: MaybeSequence[Union[float, int]], column_a1: MaybeSequence[Union[float, int]], row_a2: MaybeSequence[Union[float, int]], column_a2: MaybeSequence[Union[float, int]], row_b1: MaybeSequence[Union[float, int]], column_b1: MaybeSequence[Union[float, int]], row_b2: MaybeSequence[Union[float, int]], column_b2: MaybeSequence[Union[float, int]]) -> float`

## Description

The operator `angle_ll` calculates the angle between two lines.
As input the coordinates of two points on the first line
(*`row_a1`*,*`column_a1`*,
*`row_a2`*,*`column_a2`*) and on the second line
(*`row_b1`*,*`column_b1`*,
*`row_b2`*,*`column_b2`*) are expected.
The calculation is performed as follows: We interpret the lines
as vectors with starting points
*`row_a1`*,*`column_a1`* and
*`row_b1`*,*`column_b1`* and end points
*`row_a2`*,*`column_a2`* and
*`row_b2`*,*`column_b2`*, respectively.
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

**`row_a1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the first line.

**`column_a1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the first
line.

**`row_a2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the first line.

**`column_a2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the first
line.

**`row_b1`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the first point of the second line.

**`column_b1`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the first point of the second
line.

**`row_b2`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate of the second point of the second line.

**`column_b2`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate of the second point of the second
line.

**`angle`** (output_control)  angle.rad(-array) `→` Sequence[float]

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

`angle_ll` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`angle_lx`

## Module

Foundation
