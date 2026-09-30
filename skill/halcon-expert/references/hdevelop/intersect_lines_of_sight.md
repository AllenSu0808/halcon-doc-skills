# intersect_lines_of_sight (Operator)

## Name

`intersect_lines_of_sight` — Get a 3D point from the intersection of two lines of sight
within a binocular camera system.

## Signature

`intersect_lines_of_sight( : : CamParam1, CamParam2, RelPose, Row1, Col1, Row2, Col2 : X, Y, Z, Dist)`

## Description

Given two lines of sight from different cameras, specified by their
image points (*`Row1`*,*`Col1`*) of camera 1 and
(*`Row2`*,*`Col2`*) of camera 2,
`intersect_lines_of_sight` computes the 3D
point of intersection of these lines. The binocular camera system is
specified by its internal camera parameters *`CamParam1`* of the
projective camera 1 and *`CamParam2`* of the projective camera 2, and
the external parameters *`RelPose`*.
Latter one is of the form $ccs^1 P ccs^2$ ![figure](../assets/70dc27b5ce6d279e.svg)
and characterizes the relative pose of both cameras to each other,
thus defining a point transformation
from camera coordinate system 2 (*ccs2*) into camera coordinate
system 1 (*ccs1*), see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.
These camera parameters can be obtained, e.g., from
the operator [`calibrate_cameras`](calibrate_cameras.md), if the coordinates of the image
points (*`Row1`*,*`Col1`*) and (*`Row2`*,*`Col2`*)
refer to the respective original image coordinate system. In case of
rectified image coordinates ( e.g., obtained from rectified images),
the rectified camera parameters must be passed, as they are returned
by the operator
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). The 'point of
intersection' is defined by the point with the shortest distance to
both lines of sight. This point is returned in Cartesian coordinates
(*`X`*,*`Y`*,*`Z`*) of camera system 1 and its
distance to the lines of sight is passed in *`Dist`*.

## Attention

Stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CamParam1`** (input_control)  campar `→`  (real / integer / string)

Internal parameters of the projective camera 1.

**`CamParam2`** (input_control)  campar `→`  (real / integer / string)

Internal parameters of the projective camera 2.

**`RelPose`** (input_control)  pose `→`  (real / integer)

Point transformation from camera 2 to camera 1.

Number of elements:
7

**`Row1`** (input_control)  number(-array) `→`  (real / integer)

Row coordinate of a point in image 1.

**`Col1`** (input_control)  number(-array) `→`  (real / integer)

Column coordinate of a point in image 1.

**`Row2`** (input_control)  number(-array) `→`  (real / integer)

Row coordinate of the corresponding point in image 2.

**`Col2`** (input_control)  number(-array) `→`  (real / integer)

Column coordinate of the corresponding point in image 2.

**`X`** (output_control)  real(-array) `→`  (real)

X coordinate of the 3D point.

**`Y`** (output_control)  real(-array) `→`  (real)

Y coordinate of the 3D point.

**`Z`** (output_control)  real(-array) `→`  (real)

Z coordinate of the 3D point.

**`Dist`** (output_control)  real(-array) `→`  (real)

Distance of the 3D point to the lines of sight.

## Result

`intersect_lines_of_sight` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`binocular_calibration`

## See also

`disparity_to_point_3d`

## Module

3D Metrology
