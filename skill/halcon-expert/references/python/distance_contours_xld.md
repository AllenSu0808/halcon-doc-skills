# distance_contours_xld (Operator)

## Name

`distance_contours_xld` — Calculate the pointwise distance from one contour to another.

## Signature

`def distance_contours_xld(contour_from: HObject, contour_to: HObject, mode: str) -> HObject`

## Description

The operator `distance_contours_xld` calculates for each point in
*`contour_from`* the minimal distance to the contours in
*`contour_to`*.
The operator returns the contour *`contour_out`* which consists of
*`contour_from`* containing the computed distances in the
attribute *"distance"*.
The distances can be accessed by querying the attribute
*"distance"* with the operator [`get_contour_attrib_xld`](get_contour_attrib_xld.md).
See the operator reference of [`get_contour_attrib_xld`](get_contour_attrib_xld.md) for further
information about contour attributes.

The parameter
*`mode`* determines which distances are calculated for each point
in *`contour_from`*:
*"point_to_point"* calculates the minimal distance to the base
points of *`contour_to`*.
In contrast, *"point_to_segment"* calculates the minimum
distance to the contour segments in *`contour_to`* (see the figure
below).

![figure](../assets/102f6b49fc65c025.svg)

The dashed lines illustrate the calculated distances starting from a
point of *`contour_from`* on the left.
The distance $d_{1}$ corresponds to the
*"point_to_point"* mode, whereas the distance $d_{2}$
corresponds to the *"point_to_segment"* mode.

Note that in many applications the mode *"point_to_segment"*
suggests itself for an accurate result, whereas
*"point_to_point"* is considerably faster.
If m is the number of points in *`contour_from`*, and n the number
of points in *`contour_to`*, then `distance_contours_xld`
has complexity O(mlog(n)) for *"point_to_point"*, and O(mn) for
*"point_to_segment"*.
In case the template contour *`contour_to`* is repeatedly used, the
operators [`create_distance_transform_xld`](create_distance_transform_xld.md) and
[`apply_distance_transform_xld`](apply_distance_transform_xld.md) can be used as an alternative to
`distance_contours_xld`. For further details, please refer to
the documentation of [`create_distance_transform_xld`](create_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contour_from`** (input_object)  xld_cont(-array) `→` HObject

Contours for whose points the distances are
calculated.

**`contour_to`** (input_object)  xld_cont(-array) `→` HObject

Contours to which the distances are
calculated to.

**`contour_out`** (output_object)  xld_cont(-array) `→` HObject

Copy of *`contour_from`* containing the
distances as an attribute.

**`mode`** (input_control)  string `→` str

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

`get_contour_attrib_xld`,
`segment_contour_attrib_xld`

## Alternatives

`apply_distance_transform_xld`,
`distance_cc`,
`distance_cc_min`

## Module

Foundation
