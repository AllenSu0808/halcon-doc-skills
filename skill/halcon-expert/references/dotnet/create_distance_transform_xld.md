# CreateDistanceTransformXld (Operator)

## Name

`CreateDistanceTransformXld` — Create the XLD distance transform.

## Signature

`static void HOperatorSet.CreateDistanceTransformXld(HObject contour, HTuple mode, HTuple maxDistance, out HTuple distanceTransformID)`

`public HXLDDistTrans(HXLDCont contour, string mode, HTuple maxDistance)`

`public HXLDDistTrans(HXLDCont contour, string mode, double maxDistance)`

`void HXLDDistTrans.CreateDistanceTransformXld(HXLDCont contour, string mode, HTuple maxDistance)`

`void HXLDDistTrans.CreateDistanceTransformXld(HXLDCont contour, string mode, double maxDistance)`

## Description

`CreateDistanceTransformXld` creates the XLD distance transform
of the reference contour *`contour`* and returns the resulting handle
in *`distanceTransformID`*.

Once the XLD distance transform has been created, the operator
[`ApplyDistanceTransformXld`](apply_distance_transform_xld.md) calculates pointwise distances
from test contours to the reference contour *`contour`*. More
precisely, for each point of a test contour its minimal distance to the
contours in *`contour`* is calculated.

The parameter *`mode`* determines which distances
[`ApplyDistanceTransformXld`](apply_distance_transform_xld.md) calculates:
*"point_to_point"* calculates the minimum distance to the base
points of the *`contour`*.
In contrast, *"point_to_segment"* calculates the minimum
distance to the contour segments in *`contour`* (see the figure
below).

![figure](../assets/dc1799bd8b0c6f47.svg)

The dashed lines illustrate the calculated distances starting from
point 1 of the test contour on the left.
The distance $d_{1}$ corresponds to the
*"point_to_point"* mode, whereas the distance $d_{2}$
corresponds to the *"point_to_segment"* mode.
The gray area illustrates the area within *`maxDistance`* around
the reference contour for which distances are calculated.
The distance of point 2 of the test contour would be set to
*`maxDistance`* because it is outside of this area.

The parameter *`maxDistance`* specifies a maximum distance from the
reference contour *`contour`* which is of interest to the caller.
If the distance from a point of a test contour to the reference contour
exceeds *`maxDistance`*, the output distance of
[`ApplyDistanceTransformXld`](apply_distance_transform_xld.md) is set to *`maxDistance`*.

The operators `CreateDistanceTransformXld` and
[`ApplyDistanceTransformXld`](apply_distance_transform_xld.md) are an alternative to
[`DistanceContoursXld`](distance_contours_xld.md), if the reference contour is repeatedly used.
`CreateDistanceTransformXld` stores for each pixel in a relevant
area around *`contour`* its nearest points or segments (depending on
*`mode`*) of the reference contour *`contour`*. This allows
[`ApplyDistanceTransformXld`](apply_distance_transform_xld.md) to calculate the distances rather fast,
nearly independent of the number of points or segments of the reference
contour, the *`mode`* and the position of the points of the test contour.
However, the preparation of the XLD distance transform can take several
seconds or minutes, depending on the number of points or segments of the
reference contour and the relevant area around *`contour`* which can
be influenced by *`maxDistance`*. Furthermore,
`CreateDistanceTransformXld` is faster, if *`mode`* is set to
'point_to_point'.

[`GetDistanceTransformXldContour`](get_distance_transform_xld_contour.md) and
[`GetDistanceTransformXldParam`](get_distance_transform_xld_param.md) can be used to get back the
reference contours and the parameters of the XLD distance
transform *`distanceTransformID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`contour`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Reference contour(s).

**`mode`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Compute the distance to points ('point_to_point')
or entire segments ('point_to_segment').

Default:
"point_to_point"

List of values:
"point_to_point", "point_to_segment"

**`maxDistance`** (input_control)  real `→` [HTuple](HTuple.md) (*double* / int / long)

Maximum distance of interest.

Default:
20.0

**`distanceTransformID`** (output_control)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`ApplyDistanceTransformXld`,
`WriteDistanceTransformXld`,
`SerializeDistanceTransformXld`,
`ClearDistanceTransformXld`

## See also

`DistanceContoursXld`,
`GetDistanceTransformXldContour`,
`ReadDistanceTransformXld`,
`DeserializeDistanceTransformXld`,
`GetDistanceTransformXldParam`,
`SetDistanceTransformXldParam`

## Module

Foundation
