# distance_sl (Operator)

## Name

`distance_sl` — Calculate the distances between a line segment and a line.

## Signature

`distance_sl( : : RowA1, ColumnA1, RowA2, ColumnA2, RowB1, ColumnB1, RowB2, ColumnB2 : DistanceMin, DistanceMax)`

## Description

The operator `distance_sl` calculates the minimum and maximum
orthogonal distance between a line segment and a line.
As input the coordinates of two points on the line segment
(*`RowA1`*,*`ColumnA1`*,*`RowA2`*,*`ColumnA2`*)
and on the line
(*`RowB1`*,*`ColumnB1`*,*`RowB2`*,*`ColumnB2`*)
are expected. The parameters *`DistanceMin`* and
*`DistanceMax`* return the result of the calculation. If the line
segments are intersecting, *`DistanceMin`* returns zero.

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

**`RowA1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point of the line segment.

**`ColumnA1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the line segment.

**`RowA2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line segment.

**`ColumnA2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line segment.

**`RowB1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point of the line.

**`ColumnB1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the line.

**`RowB2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line.

**`ColumnB2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line.

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between the line segment and
the line.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

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

`distance_sl` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_pl`

## See also

`distance_ps`,
`distance_pp`

## Module

Foundation
