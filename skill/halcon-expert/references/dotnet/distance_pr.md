# DistancePr (Operator)

## Name

`DistancePr` — Calculate the distance between a point and a region.

## Signature

`static void HOperatorSet.DistancePr(HObject region, HTuple row, HTuple column, out HTuple distanceMin, out HTuple distanceMax)`

`void HRegion.DistancePr(HTuple row, HTuple column, out HTuple distanceMin, out HTuple distanceMax)`

`void HRegion.DistancePr(double row, double column, out double distanceMin, out double distanceMax)`

## Description

The operator `DistancePr` calculates the distance
between a point and one region.
As input the coordinates of the points
(*`row`*,*`column`*) and a region are expected.
If a point is inside of the region, its minimum distance is zero.
The parameters
*`distanceMin`* and *`distanceMax`* return
the result of the calculation.

### Parameter Broadcasting

This operator supports parameter broadcasting.
This means that each parameter can be given as a tuple of length
*1* or *N*.
Parameters with tuple length *1* will be repeated internally
such that the number of distances is always *N*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Input region.

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the point.

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the point.

**`distanceMin`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the point and the region.

**`distanceMax`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the point and the region.

## Example (HDevelop)

```
gen_circle (Circle, 200, 200, 100.5)
draw_point (WindowHandle, Row, Column)
gen_cross_contour_xld (Cross, Row, Column, 15, 0)
distance_pr (Circle, Row, Column, DistanceMin, DistanceMax)
```

## Result

`DistancePr` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistancePc`,
`DistanceLr`,
`DistanceSr`,
`DiameterRegion`

## See also

`HammingDistance`,
`SelectRegionPoint`,
`TestRegionPoint`,
`SmallestRectangle2`

## Module

Foundation
