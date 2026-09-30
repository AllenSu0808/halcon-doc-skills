# DistanceContoursXld (Operator)

## Name

`DistanceContoursXld` — Calculate the pointwise distance from one contour to another.

## Signature

`static void HOperatorSet.DistanceContoursXld(HObject contourFrom, HObject contourTo, out HObject contourOut, HTuple mode)`

`HXLDCont HXLDCont.DistanceContoursXld(HXLDCont contourTo, string mode)`

## Description

The operator `DistanceContoursXld` calculates for each point in
*`contourFrom`* the minimal distance to the contours in
*`contourTo`*.
The operator returns the contour *`contourOut`* which consists of
*`contourFrom`* containing the computed distances in the
attribute *"distance"*.
The distances can be accessed by querying the attribute
*"distance"* with the operator [`GetContourAttribXld`](get_contour_attrib_xld.md).
See the operator reference of [`GetContourAttribXld`](get_contour_attrib_xld.md) for further
information about contour attributes.

The parameter
*`mode`* determines which distances are calculated for each point
in *`contourFrom`*:
*"point_to_point"* calculates the minimal distance to the base
points of *`contourTo`*.
In contrast, *"point_to_segment"* calculates the minimum
distance to the contour segments in *`contourTo`* (see the figure
below).

![figure](../assets/102f6b49fc65c025.svg)

The dashed lines illustrate the calculated distances starting from a
point of *`contourFrom`* on the left.
The distance $d_{1}$ corresponds to the
*"point_to_point"* mode, whereas the distance $d_{2}$
corresponds to the *"point_to_segment"* mode.

Note that in many applications the mode *"point_to_segment"*
suggests itself for an accurate result, whereas
*"point_to_point"* is considerably faster.
If m is the number of points in *`contourFrom`*, and n the number
of points in *`contourTo`*, then `DistanceContoursXld`
has complexity O(mlog(n)) for *"point_to_point"*, and O(mn) for
*"point_to_segment"*.
In case the template contour *`contourTo`* is repeatedly used, the
operators [`CreateDistanceTransformXld`](create_distance_transform_xld.md) and
[`ApplyDistanceTransformXld`](apply_distance_transform_xld.md) can be used as an alternative to
`DistanceContoursXld`. For further details, please refer to
the documentation of [`CreateDistanceTransformXld`](create_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contourFrom`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contours for whose points the distances are
calculated.

**`contourTo`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contours to which the distances are
calculated to.

**`contourOut`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Copy of *`contourFrom`* containing the
distances as an attribute.

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Compute the distance to points ('point_to_point')
or to entire segments ('point_to_segment').

Default:
"point_to_point"

List of values:
"point_to_point", "point_to_segment"

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`GetContourAttribXld`,
`SegmentContourAttribXld`

## Alternatives

`ApplyDistanceTransformXld`,
`DistanceCc`,
`DistanceCcMin`

## Module

Foundation
