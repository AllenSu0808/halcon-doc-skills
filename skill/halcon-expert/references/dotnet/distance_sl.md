# DistanceSl (Operator)

## Name

`DistanceSl` — Calculate the distances between a line segment and a line.

## Signature

`static void HOperatorSet.DistanceSl(HTuple rowA1, HTuple columnA1, HTuple rowA2, HTuple columnA2, HTuple rowB1, HTuple columnB1, HTuple rowB2, HTuple columnB2, out HTuple distanceMin, out HTuple distanceMax)`

`static void HMisc.DistanceSl(HTuple rowA1, HTuple columnA1, HTuple rowA2, HTuple columnA2, HTuple rowB1, HTuple columnB1, HTuple rowB2, HTuple columnB2, out HTuple distanceMin, out HTuple distanceMax)`

`static void HMisc.DistanceSl(double rowA1, double columnA1, double rowA2, double columnA2, double rowB1, double columnB1, double rowB2, double columnB2, out double distanceMin, out double distanceMax)`

## Description

The operator `DistanceSl` calculates the minimum and maximum
orthogonal distance between a line segment and a line.
As input the coordinates of two points on the line segment
(*`rowA1`*,*`columnA1`*,*`rowA2`*,*`columnA2`*)
and on the line
(*`rowB1`*,*`columnB1`*,*`rowB2`*,*`columnB2`*)
are expected. The parameters *`distanceMin`* and
*`distanceMax`* return the result of the calculation. If the line
segments are intersecting, *`distanceMin`* returns zero.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of computed distances is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`rowA1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line segment.

**`columnA1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line segment.

**`rowA2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line segment.

**`columnA2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line segment.

**`rowB1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line.

**`columnB1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line.

**`rowB2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line.

**`columnB2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line.

**`distanceMin`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the line segment and
the line.

**`distanceMax`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the line segment and
the line.

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
Row1 := 300
Column1 := 200
Row2 := 100
Column2 := 400
gen_contour_polygon_xld (Line1, [Row1,Row2], [Column1,Column2])
dev_display (Line1)
Column := 50
Row := 100
Offset := 0
for RowEnd := 100 to 500 by 100
  gen_contour_polygon_xld (Line2, [Row,RowEnd], \
                           [Column+Offset,Column+Offset])
  dev_display (Line1)
  distance_sl (Row, Column+Offset, RowEnd, Column+Offset, Row1, Column1, \
               Row2, Column2,DistanceMin, DistanceMax)
  Offset := Offset+40
endfor
```

## Result

`DistanceSl` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistancePl`

## See also

`DistancePs`,
`DistancePp`

## Module

Foundation
