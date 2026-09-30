# DistancePc (Operator)

## Name

`DistancePc` — Calculate the distance between a point and one contour.

## Signature

`static void HOperatorSet.DistancePc(HObject contour, HTuple row, HTuple column, out HTuple distanceMin, out HTuple distanceMax)`

`void HXLDCont.DistancePc(HTuple row, HTuple column, out HTuple distanceMin, out HTuple distanceMax)`

`void HXLDCont.DistancePc(double row, double column, out double distanceMin, out double distanceMax)`

## Description

The operator `DistancePc` calculates the distance between one or
several points and a single contour. As input the coordinates of the points
(*`row`*,*`column`*) and the contour (*`contour`*) are
expected. The parameters *`distanceMin`* and *`distanceMax`*
return the result of the calculation. Note that the result corresponds to the
distances between the points and the segments of the contour and not the
distances between the points and the base points of the contour (see also
[`DistanceContoursXld`](distance_contours_xld.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`contour`** (input_object)  xld_cont `→` [HXLDCont](HXLDCont.md)

Input contour.

**`row`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the point.

**`column`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the point.

**`distanceMin`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the point and the contour.

**`distanceMax`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the point and the contour.

## Result

`DistancePc` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistanceLc`,
`DistanceSc`,
`DistanceCc`,
`DistanceCcMin`

## See also

`DistancePr`,
`DistanceLr`,
`DistanceSr`,
`HammingDistance`,
`SelectXldPoint`,
`TestXldPoint`

## Module

Foundation
