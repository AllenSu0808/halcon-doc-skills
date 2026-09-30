# DistanceSr (Operator)

## Name

`DistanceSr` — Calculate the distance between a line segment and one region.

## Signature

`static void HOperatorSet.DistanceSr(HObject region, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`void HRegion.DistanceSr(HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`void HRegion.DistanceSr(double row1, double column1, double row2, double column2, out double distanceMin, out double distanceMax)`

## Description

The operator `DistanceSr` calculates the distance between
a line segment and a region.
*`row1`*, *`column1`*, *`row2`*, *`column2`*
are the start and end coordinates of a line segment.
The parameters *`distanceMin`* and *`distanceMax`*
contain the resulting distances.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of distances is always *N*.

## Attention

To enhance `DistanceSr`,
holes are ignored.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region.

**`row1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line segment.

**`column1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line segment.

**`row2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line segment.

**`column2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line segment.

**`distanceMin`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the line segment and
the region.

**`distanceMax`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the line segment and
the region.

## Example (HDevelop)

```
gen_circle (Circle, 200, 200, 100.5)
Column1 := 300
Column2 := 400
for Row := 50 to 350 by 50
  gen_contour_polygon_xld (Line, [Row,Row], [Column1,Column2])
  distance_sr (Circle, Row, Column1, Row, Column2, DistanceMin, DistanceMax)
endfor
```

## Result

`DistanceSr` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistanceSc`,
`DistanceLr`,
`DistancePr`,
`DiameterRegion`

## See also

`HammingDistance`,
`SelectRegionPoint`,
`TestRegionPoint`,
`SmallestRectangle2`

## Module

Foundation
