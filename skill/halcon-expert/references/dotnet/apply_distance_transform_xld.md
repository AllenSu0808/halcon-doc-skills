# ApplyDistanceTransformXld (Operator)

## Name

`ApplyDistanceTransformXld` — Determine the pointwise distance of two contours using an XLD distance
transform.

## Signature

`static void HOperatorSet.ApplyDistanceTransformXld(HObject contour, out HObject contourOut, HTuple distanceTransformID)`

`HXLDCont HXLDDistTrans.ApplyDistanceTransformXld(HXLDCont contour)`

## Description

The operator `ApplyDistanceTransformXld` determines for
each point in *`contour`* the minimal distance to the reference contour
using its XLD distance transform *`distanceTransformID`*.
The returned contour *`contourOut`* consists of
*`contour`* with the attribute *"distance"* containing the
calculated distances. They can be accessed by querying the attribute
*"distance"* with [`GetContourAttribXld`](get_contour_attrib_xld.md). See the operator
reference of [`GetContourAttribXld`](get_contour_attrib_xld.md) for further information about
contour attributes.

Note that the distances depend on the parameters of
[`CreateDistanceTransformXld`](create_distance_transform_xld.md):
The distances are clipped to the maximum distance specified by the parameter
MaxDistance. The parameter Mode determines whether the distances are
calculated *"point_to_point"* or *"point_to_segment"*.
For further details please refer to the documentation of
[`CreateDistanceTransformXld`](create_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Contour(s) for whose points the distances are
calculated.

**`contourOut`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Copy of *`contour`* containing the distances
as an attribute.

**`distanceTransformID`** (input_control)  xld_dist_trans `→` [HXLDDistTrans](HXLDDistTrans.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the XLD distance transform of the
reference contour.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`CreateDistanceTransformXld`,
`ReadDistanceTransformXld`,
`DeserializeDistanceTransformXld`,
`SetDistanceTransformXldParam`

## Possible Successors

`GetContourAttribXld`,
`SegmentContourAttribXld`

## Alternatives

`DistanceContoursXld`

## See also

`GetContourAttribXld`,
`SetDistanceTransformXldParam`,
`WriteDistanceTransformXld`,
`SerializeDistanceTransformXld`,
`ClearDistanceTransformXld`

## Module

Foundation
