# distance_contours_xld (Operator)

## Name

`distance_contours_xld` — Calculate the pointwise distance from one contour to another.

## Signature

`distance_contours_xld(ContourFrom, ContourTo : ContourOut : Mode : )`

## Description

The operator `distance_contours_xld` calculates for each point in
*`ContourFrom`* the minimal distance to the contours in
*`ContourTo`*.
The operator returns the contour *`ContourOut`* which consists of
*`ContourFrom`* containing the computed distances in the
attribute *'distance'*.
The distances can be accessed by querying the attribute
*'distance'* with the operator [`get_contour_attrib_xld`](get_contour_attrib_xld.md).
See the operator reference of [`get_contour_attrib_xld`](get_contour_attrib_xld.md) for further
information about contour attributes.

The parameter
*`Mode`* determines which distances are calculated for each point
in *`ContourFrom`*:
*'point_to_point'* calculates the minimal distance to the base
points of *`ContourTo`*.
In contrast, *'point_to_segment'* calculates the minimum
distance to the contour segments in *`ContourTo`* (see the figure
below).

![figure](../assets/102f6b49fc65c025.svg)

The dashed lines illustrate the calculated distances starting from a
point of *`ContourFrom`* on the left.
The distance $d_{1}$ corresponds to the
*'point_to_point'* mode, whereas the distance $d_{2}$
corresponds to the *'point_to_segment'* mode.

Note that in many applications the mode *'point_to_segment'*
suggests itself for an accurate result, whereas
*'point_to_point'* is considerably faster.
If m is the number of points in *`ContourFrom`*, and n the number
of points in *`ContourTo`*, then `distance_contours_xld`
has complexity O(mlog(n)) for *'point_to_point'*, and O(mn) for
*'point_to_segment'*.
In case the template contour *`ContourTo`* is repeatedly used, the
operators [`create_distance_transform_xld`](create_distance_transform_xld.md) and
[`apply_distance_transform_xld`](apply_distance_transform_xld.md) can be used as an alternative to
`distance_contours_xld`. For further details, please refer to
the documentation of [`create_distance_transform_xld`](create_distance_transform_xld.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`ContourFrom`** (input_object)  xld_cont(-array) `→` object

Contours for whose points the distances are
calculated.

**`ContourTo`** (input_object)  xld_cont(-array) `→` object

Contours to which the distances are
calculated to.

**`ContourOut`** (output_object)  xld_cont(-array) `→` object

Copy of *`ContourFrom`* containing the
distances as an attribute.

**`Mode`** (input_control)  string `→`  (string)

Compute the distance to points ('point_to_point')
or to entire segments ('point_to_segment').

Default:
'point_to_point'

List of values:
'point_to_point', 'point_to_segment'

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
