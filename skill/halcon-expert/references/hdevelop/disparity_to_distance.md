# disparity_to_distance (Operator)

## Name

`disparity_to_distance` — Transform a disparity value into a distance value in a rectified
binocular stereo system.

## Signature

`disparity_to_distance( : : CamParamRect1, CamParamRect2, RelPoseRect, Disparity : Distance)`

## Description

`disparity_to_distance` transforms a disparity value into a
distance of an object point to the binocular stereo system. The
cameras of this system must be rectified and are defined by the
rectified internal parameters *`CamParamRect1`* of camera 1 and
*`CamParamRect2`* of camera 2, and the external parameters
*`RelPoseRect`*. Latter specifies the relative pose of both
cameras to each other by defining a point transformation from
rectified camera system 2 to rectified camera system 1. These
parameters can be obtained from the operator
[`calibrate_cameras`](calibrate_cameras.md) and
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). The disparity value
*`Disparity`* is defined by the column difference of the image
coordinates of two corresponding points on an epipolar line
according to the equation $d=c_{2}-c_{1}$(see also [`binocular_disparity`](binocular_disparity.md)). This value characterises
a set of 3D object points of an equal distance to a plane being
parallel to the rectified image plane of the stereo system.
The distance to the subset plane z=0 which is parallel to
the rectified image plane and contains the optical centers of both
cameras is returned in *`Distance`*.

## Attention

If using cameras with telecentric lenses, the *`Distance`* is
not defined as the distance of a point to the camera but as the
distance from the point to the plane, defined by the y-axes of both
cameras and their baseline (see
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)).

For a stereo setup of mixed type (i.e., for a stereo setup in which
one of the original cameras is a perspective camera and the other
camera is a telecentric camera; see
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md)), the rectifying plane of
the two cameras is in a position with respect to the object that
would lead to very unintuitive distances. Therefore,
`disparity_to_distance` does not support stereo setups of
mixed type. For stereo setups of mixed type,
[`disparity_to_point_3d`](disparity_to_point_3d.md) should be used instead.

Additionally, stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CamParamRect1`** (input_control)  campar `→`  (real / integer / string)

Rectified internal camera parameters of camera 1.

**`CamParamRect2`** (input_control)  campar `→`  (real / integer / string)

Rectified internal camera parameters of camera 2.

**`RelPoseRect`** (input_control)  pose `→`  (real / integer)

Point transformation from the rectified camera 2 to
the rectified camera 1.

Number of elements:
7

**`Disparity`** (input_control)  number(-array) `→`  (real / integer)

Disparity between the images of the world point.

**`Distance`** (output_control)  real(-array) `→`  (real)

Distance of a world point to the rectified camera
system.

## Result

`disparity_to_distance` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`binocular_calibration`,
`gen_binocular_rectification_map`,
`map_image`,
`binocular_disparity`

## Alternatives

`binocular_distance`

## See also

`distance_to_disparity`,
`disparity_to_point_3d`

## Module

3D Metrology
