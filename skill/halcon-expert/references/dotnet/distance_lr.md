# DistanceLr (Operator)

## Name

`DistanceLr` — Calculate the distance between a line and a region.

## Signature

`static void HOperatorSet.DistanceLr(HObject region, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`void HRegion.DistanceLr(HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`void HRegion.DistanceLr(double row1, double column1, double row2, double column2, out double distanceMin, out double distanceMax)`

## Description

The operator `DistanceLr` calculates the orthogonal
distance between a line and a region.
As input the coordinates of two points on a line
(*`row1`*,*`column1`*,
*`row2`*,*`column2`*) and a region are expected.
The parameters *`distanceMin`* and *`distanceMax`*
return the result of the calculation.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of distances is always *N*.

## Attention

Due to efficiency of `DistanceLr`
holes are ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region.

**`row1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line.

**`column1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line.

**`row2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line.

**`column2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line.

**`distanceMin`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the line and the region

**`distanceMax`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the line and the region

## Example (HDevelop)

```
gen_circle (Circle, 200, 200, 100.5)
Column1 := 300
Column2 := 400
for Row := 50 to 350 by 50
  gen_contour_polygon_xld (Line, [Row,Row], [Column1,Column2])
  distance_lr (Circle, Row, Column1, Row, Column2, DistanceMin, DistanceMax)
endfor
```

## Result

`DistanceLr` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistanceLc`,
`DistancePr`,
`DistanceSr`,
`DiameterRegion`

## See also

`HammingDistance`,
`SelectRegionPoint`,
`TestRegionPoint`,
`SmallestRectangle2`

## Module

Foundation
