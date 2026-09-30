# get_circle_pose (Operator)

## Name

`get_circle_pose` — Determine the 3D pose of a circle from its perspective 2D projection.

## Signature

`get_circle_pose(Contour : : CameraParam, Radius, OutputType : Pose1, Pose2)`

## Description

Each ellipse in an image can be interpreted as the perspective projection
of a circle into the image. In fact, for a given radius of the circle,
there exist two differently oriented circles in 3D that result in
the same projection. `get_circle_pose` determines the 3D positions
and orientations of these two circles. First, each *`Contour`*
is approximated by an ellipse. Then, based on the internal camera
parameters (*`CameraParam`*) and the radius of the circle in 3D
(*`Radius`*), the 3D positions and orientations
(*`Pose1`*,*`Pose2`*) are determined in camera coordinates.

Depending on the value of the parameter *`OutputType`*, the
position and orientation is returned as a 3D pose
(*`OutputType`* = *'pose'*) or in the form of the
center of the 3D circle and the normal vector of the plane in which
the circle lies (*`OutputType`* = *'center_normal'*).
In the former case, the angle for the rotation around the z axis
is set to zero, because it cannot be determined.
In the latter case, the first three elements of the output parameters
*`Pose1`* and *`Pose2`* contain the position of the center
of the circle. The following three elements contain the normal vector.
The normal vectors are normalized and oriented such that they point away
from the optical center which is the origin of the camera coordinate
system. If *`OutputType`* is set to *'center_normal'*,
the output parameters *`Pose1`* and *`Pose2`* contain only
six elements which describe the position and orientation of the circle
instead of the seven elements of the 3D pose that are returned if
*`OutputType`* is set to *'pose'*.

If more than one contour is passed in *`Contour`*, *`Radius`*
must either contain a tuple that contains a value for each contour or
only one value which is then used for all contours. The resulting
positions and orientations are stored one after another in *`Pose1`*
and *`Pose2`*, i.e., *`Pose1`* and *`Pose2`* contain
first the pose or the position and the normal vector of the first
contour, followed by the respective values for the second contour
and so on.

## Attention

The accuracy of the determined poses depends heavily on the accuracy of
the extracted contours.
The extraction of curved edges using relatively large filter masks leads
to a slightly shifted edge position. Edge extraction approaches that
are based on the first derivative of the image function
(e.g., [`edges_sub_pix`](edges_sub_pix.md)) yield edges that are shifted towards the
center of curvature, i.e., extracted ellipses will be slightly to small.
Approaches that are based on the second derivative of the image function
([`laplace_of_gauss`](laplace_of_gauss.md) followed by [`zero_crossing_sub_pix`](zero_crossing_sub_pix.md))
result in edges that are shifted away from the center of curvature, i.e.,
extracted ellipses will be slightly too large.

These effects increase with the curvature of the edge and with the size
of the filter mask that is used for the edge extraction. Therefore, to
achieve high accuracy, the ellipses should appear large in the image
and the filter parameter should be chosen such that small filter masks
are used (see [`info_edges`](info_edges.md)).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Contour`** (input_object)  xld(-array) `→` object

Contours to be examined.

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`Radius`** (input_control)  number(-array) `→`  (real)

Radius of the circle in object space.

Number of elements:
Radius == Contour || Radius == 1

Restriction:
`Radius > 0.0`

**`OutputType`** (input_control)  string `→`  (string)

Type of output parameters.

Default:
'pose'

List of values:
'center_normal', 'pose'

**`Pose1`** (output_control)  real-array `→`  (real / integer)

3D pose of the first circle.

Number of elements:
Pose1 == 7 * Contour || Pose1 == 6 * Contour

**`Pose2`** (output_control)  real-array `→`  (real / integer)

3D pose of the second circle.

Number of elements:
Pose2 == 7 * Contour || Pose2 == 6 * Contour

## Result

`get_circle_pose` returns 2 (
H_MSG_TRUE)
if all parameter values are
correct and the position of the circle has been determined successfully.
If necessary, an exception is raised.

## Possible Predecessors

`edges_sub_pix`

## Alternatives

`find_marks_and_pose`,
`camera_calibration`

## See also

`get_rectangle_pose`,
`fit_ellipse_contour_xld`

## Module

3D Metrology
