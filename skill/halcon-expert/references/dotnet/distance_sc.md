# DistanceSc (Operator)

## Name

`DistanceSc` — Calculate the distance between a line segment and one contour.

## Signature

`static void HOperatorSet.DistanceSc(HObject contour, HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`void HXLDCont.DistanceSc(HTuple row1, HTuple column1, HTuple row2, HTuple column2, out HTuple distanceMin, out HTuple distanceMax)`

`void HXLDCont.DistanceSc(double row1, double column1, double row2, double column2, out double distanceMin, out double distanceMax)`

## Description

The operator `DistanceSc` calculates the distance between
a line segment and the line segments of a contour.
*`row1`*, *`column1`*, *`row2`*, *`column2`*
are the start and end coordinates of a line segment,
*`contour`* represents the input contour.
The parameters *`distanceMin`* and *`distanceMax`*
contain the resulting distances.

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

Row coordinate of the first point of the line segment.

**`column1`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the first point of the line segment.

**`row2`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the second point of the line segment.

**`column2`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the second point of the line segment.

**`distanceMin`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the line segment and
the contour.

**`distanceMax`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Maximum distance between the line segment and
the contour.

## Result

[`DistanceSr`](distance_sr.md) returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistanceLc`,
`DistancePc`,
`DistanceCc`,
`DistanceCcMin`

## See also

`DistanceSr`,
`DistanceLr`,
`DistancePr`,
`SelectXldPoint`,
`TestXldPoint`

## Module

Foundation
