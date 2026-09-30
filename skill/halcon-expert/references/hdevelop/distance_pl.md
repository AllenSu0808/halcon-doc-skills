# distance_pl (Operator)

## Name

`distance_pl` — Calculate the distance between one point and one line.

## Signature

`distance_pl( : : Row, Column, Row1, Column1, Row2, Column2 : Distance)`

## Description

The operator `distance_pl` calculates the orthogonal distance
between points (*`Row`*,*`Column`*) and lines,
given by two arbitrary points on the line.
The result is passed in *`Distance`*.

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

**`Row`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the point.

**`Column`** (input_control)  point.x(-array) `→`  (real / integer)

Column of the point.

**`Row1`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the first point of the line.

**`Column1`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the first point of the line.

**`Row2`** (input_control)  point.y(-array) `→`  (real / integer)

Row coordinate of the second point of the line.

**`Column2`** (input_control)  point.x(-array) `→`  (real / integer)

Column coordinate of the second point of the line.

**`Distance`** (output_control)  real(-array) `→`  (real)

Distance between the points.

## Example (HDevelop)

```
dev_open_window (0, 0, 512, 512, 'black', WindowHandle)
draw_point (WindowHandle, Row, Column)
gen_cross_contour_xld (Cross, Row, Column, 15, 0)
draw_line (WindowHandle, Row1, Column1, Row2, Column2)
gen_contour_polygon_xld (Contour, [Row1,Row2], [Column1,Column2])
distance_pl (Row, Column, Row1, Column1, Row2, Column2, Distance)
```

## Result

`distance_pl` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`distance_ps`

## See also

`distance_pp`,
`distance_pr`

## Module

Foundation
