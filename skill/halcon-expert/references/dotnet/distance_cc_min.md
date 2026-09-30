# DistanceCcMin (Operator)

## Name

`DistanceCcMin` — Calculate the minimum distance between two contours.

## Signature

`static void HOperatorSet.DistanceCcMin(HObject contour1, HObject contour2, HTuple mode, out HTuple distanceMin)`

`HTuple HXLDCont.DistanceCcMin(HXLDCont contour2, HTuple mode)`

`double HXLDCont.DistanceCcMin(HXLDCont contour2, string mode)`

## Description

`DistanceCcMin` calculates the minimum distance between
two contours *`contour1`* and *`contour2`*.
The minimum distance is returned in *`distanceMin`*.

The parameter *`mode`* sets the type of computing the distance.
*"point_to_point"* determines the distance between the closest
contour points, *"fast_point_to_segment"* calculates the
distance between the line segments adjacent to these points, and
*"point_to_segment"* determines the actual minimum
distance between the contour segments.

While *"point_to_point"* and *"fast_point_to_segment"*
are efficient algorithms with a complexity of n*log(n),
*"point_to_segment"* has quadratic complexity and thus
takes a longer time to execute, especially for contours with many line
segments.

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

**`contour1`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

First input contour.

**`contour2`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Second input contour.

**`mode`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string*)

Distance calculation mode.

Default:
"fast_point_to_segment"

List of values:
"fast_point_to_segment", "point_to_point", "point_to_segment"

**`distanceMin`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Minimum distance between the two contours.

## Example (C)

```
gen_contour_polygon_rounded_xld(Cont1, [0,100,100,0,0], [0,0,100,100,0],
                                [50,50,50,50,50], 0.5);
gen_contour_polygon_rounded_xld(Cont2, [41,91,91,41,41], [41,41,91,91,41],
                                [25,25,25,25,25], 0.5);
distance_cc_min(Cont1, Cont2, "fast_point_to_segment", &distance_min);
```

## Result

`DistanceCcMin` returns 2 (
H_MSG_TRUE)
.

## Alternatives

`DistanceSc`,
`DistancePc`,
`DistanceCc`,
`DistanceContoursXld`

## See also

`DistanceSr`,
`DistancePr`

## Module

Foundation
