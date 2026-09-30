# create_distance_transform_xld (Operator)

## Name

`create_distance_transform_xld` — Create the XLD distance transform.

## Signature

`create_distance_transform_xld(Contour : : Mode, MaxDistance : DistanceTransformID)`

## Description

`create_distance_transform_xld` creates the XLD distance transform
of the reference contour *`Contour`* and returns the resulting handle
in *`DistanceTransformID`*.

Once the XLD distance transform has been created, the operator
[`apply_distance_transform_xld`](apply_distance_transform_xld.md) calculates pointwise distances
from test contours to the reference contour *`Contour`*. More
precisely, for each point of a test contour its minimal distance to the
contours in *`Contour`* is calculated.

The parameter *`Mode`* determines which distances
[`apply_distance_transform_xld`](apply_distance_transform_xld.md) calculates:
*'point_to_point'* calculates the minimum distance to the base
points of the *`Contour`*.
In contrast, *'point_to_segment'* calculates the minimum
distance to the contour segments in *`Contour`* (see the figure
below).

![figure](../assets/dc1799bd8b0c6f47.svg)

The dashed lines illustrate the calculated distances starting from
point 1 of the test contour on the left.
The distance $d_{1}$ corresponds to the
*'point_to_point'* mode, whereas the distance $d_{2}$
corresponds to the *'point_to_segment'* mode.
The gray area illustrates the area within *`MaxDistance`* around
the reference contour for which distances are calculated.
The distance of point 2 of the test contour would be set to
*`MaxDistance`* because it is outside of this area.

The parameter *`MaxDistance`* specifies a maximum distance from the
reference contour *`Contour`* which is of interest to the caller.
If the distance from a point of a test contour to the reference contour
exceeds *`MaxDistance`*, the output distance of
[`apply_distance_transform_xld`](apply_distance_transform_xld.md) is set to *`MaxDistance`*.

The operators `create_distance_transform_xld` and
[`apply_distance_transform_xld`](apply_distance_transform_xld.md) are an alternative to
[`distance_contours_xld`](distance_contours_xld.md), if the reference contour is repeatedly used.
`create_distance_transform_xld` stores for each pixel in a relevant
area around *`Contour`* its nearest points or segments (depending on
*`Mode`*) of the reference contour *`Contour`*. This allows
[`apply_distance_transform_xld`](apply_distance_transform_xld.md) to calculate the distances rather fast,
nearly independent of the number of points or segments of the reference
contour, the *`Mode`* and the position of the points of the test contour.
However, the preparation of the XLD distance transform can take several
seconds or minutes, depending on the number of points or segments of the
reference contour and the relevant area around *`Contour`* which can
be influenced by *`MaxDistance`*. Furthermore,
`create_distance_transform_xld` is faster, if *`Mode`* is set to
'point_to_point'.

[`get_distance_transform_xld_contour`](get_distance_transform_xld_contour.md) and
[`get_distance_transform_xld_param`](get_distance_transform_xld_param.md) can be used to get back the
reference contours and the parameters of the XLD distance
transform *`DistanceTransformID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`Contour`** (input_object)  xld_cont(-array) `→` object

Reference contour(s).

**`Mode`** (input_control)  string `→`  (string)

Compute the distance to points ('point_to_point')
or entire segments ('point_to_segment').

Default:
'point_to_point'

List of values:
'point_to_point', 'point_to_segment'

**`MaxDistance`** (input_control)  real `→`  (real / integer)

Maximum distance of interest.

Default:
20.0

**`DistanceTransformID`** (output_control)  xld_dist_trans `→`  (handle)

Handle of the XLD distance transform.

## Result

If all parameters are correct, the operator returns the
value 2 (
H_MSG_TRUE)
. Otherwise, an exception is raised.

## Possible Successors

`apply_distance_transform_xld`,
`write_distance_transform_xld`,
`serialize_distance_transform_xld`,
`clear_distance_transform_xld`

## See also

`distance_contours_xld`,
`get_distance_transform_xld_contour`,
`read_distance_transform_xld`,
`deserialize_distance_transform_xld`,
`get_distance_transform_xld_param`,
`set_distance_transform_xld_param`

## Module

Foundation
