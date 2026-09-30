# DistanceLc (Operator)

## Name

`DistanceLc` — Calculate the distance between a line and one contour.

## Signature

`static void HOperatorSet.DistanceLc(HObject contour, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`void HXLDCont.DistanceLc(HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`void HXLDCont.DistanceLc(double row1, double column1, double row2, double column2, out double distanceMin, out double distanceMax)`

## Description

The operator `DistanceLc` calculates the orthogonal
distance between a line and the segments of a contour.
As input the coordinates of two points on a line
(*`row1`*,*`column1`*,
*`row2`*,*`column2`*) and a contour (*`contour`*)
are expected.
The parameters *`distanceMin`* and *`distanceMax`*
return the result of the calculation.

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

**`contour`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contour.

**`row1`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the first point of the line.

**`column1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line.

**`row2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line.

**`column2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line.

**`distanceMin`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the line and the contour.

**`distanceMax`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the line and the contour.

## Result

`DistanceLc` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistancePc`,
`DistanceSc`,
`DistanceCc`,
`DistanceCcMin`

## See also

`DistanceLr`,
`DistancePr`,
`DistanceSr`

## Module

Foundation
