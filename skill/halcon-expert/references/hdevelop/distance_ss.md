# distance_ss (Operator)

## Name

`distance_ss` — Calculate the distances between two line segments.

## Signature

`distance_ss( : : RowA1, ColumnA1, RowA2, ColumnA2, RowB1, ColumnB1, RowB2, ColumnB2 : DistanceMin, DistanceMax)`

## Description

The operator `distance_ss` calculates the minimum and maximum
distance between two line segments. As input the coordinates of the
start and end point of the
first line segment (*`RowA1`*,*`ColumnA1`*,
*`RowA2`*,*`ColumnA2`*) and of the second line segment
(*`RowB1`*,*`ColumnB1`*,*`RowB2`*,*`ColumnB2`*)
are used.
The parameters *`DistanceMin`* and *`DistanceMax`* return
the result of the calculation. If the line segments are intersecting,
*`DistanceMin`* returns zero.

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

Column of the first point of the line.

**`RowB2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line.

**`ColumnB2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line.

**`DistanceMin`** (output_control)  real(-array) `→`  (real)

Minimum distance between the line segments.

**`DistanceMax`** (output_control)  real(-array) `→`  (real)

Maximum distance between the line segments.

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
Row1 := 300
Column1 := 200
Row2 := 100
Column2 := 300
gen_contour_polygon_xld (Line1, [Row1,Row2], [Column1,Column2])
Column := 100
Offset := 30
for Row := 40 to 100 by 20
  gen_contour_polygon_xld (Line2, [Row, Row+Offset], \
                           [Column, Column+Offset])
  distance_ss (Row, Column, Row+Offset, Column+Offset, Row1, Column1, \
               Row2, Column2, DistanceMin, DistanceMax)
  Offset := Offset+50
endfor
```

## Result

`distance_ss` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_pp`

## See also

`distance_pl`,
`distance_ps`

## Module

Foundation
