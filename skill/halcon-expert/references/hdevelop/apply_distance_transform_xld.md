# apply_distance_transform_xld (Operator)

## Name

`apply_distance_transform_xld` — Determine the pointwise distance of two contours using an XLD distance
transform.

## Signature

`apply_distance_transform_xld(Contour : ContourOut : DistanceTransformID : )`

## Description

The operator `apply_distance_transform_xld` determines for
each point in *`Contour`* the minimal distance to the reference contour
using its XLD distance transform *`DistanceTransformID`*.
The returned contour *`ContourOut`* consists of
*`Contour`* with the attribute *'distance'* containing the
calculated distances. They can be accessed by querying the attribute
*'distance'* with [`get_contour_attrib_xld`](get_contour_attrib_xld.md). See the operator
reference of [`get_contour_attrib_xld`](get_contour_attrib_xld.md) for further information about
contour attributes.

Note that the distances depend on the parameters of
[`create_distance_transform_xld`](create_distance_transform_xld.md):
The distances are clipped to the maximum distance specified by the parameter
MaxDistance. The parameter Mode determines whether the distances are
calculated *'point_to_point'* or *'point_to_segment'*.
For further details please refer to the documentation of
[`create_distance_transform_xld`](create_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (input_object)  xld_cont(-array) `→` object

Contour(s) for whose points the distances are
calculated.

**`ContourOut`** (output_object)  xld_cont(-array) `→` object

Copy of *`Contour`* containing the distances
as an attribute.

**`DistanceTransformID`** (input_control)  xld_dist_trans `→`  (handle)

Handle of the XLD distance transform of the
reference contour.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Predecessors

`create_distance_transform_xld`,
`read_distance_transform_xld`,
`deserialize_distance_transform_xld`,
`set_distance_transform_xld_param`

## Possible Successors

`get_contour_attrib_xld`,
`segment_contour_attrib_xld`

## Alternatives

`distance_contours_xld`

## See also

`get_contour_attrib_xld`,
`set_distance_transform_xld_param`,
`write_distance_transform_xld`,
`serialize_distance_transform_xld`,
`clear_distance_transform_xld`

## Module

Foundation
