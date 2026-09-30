# intersect_lines_of_sight (Operator)

## Name

`intersect_lines_of_sight` — Get a 3D point from the intersection of two lines of sight
within a binocular camera system.

## Signature

`def intersect_lines_of_sight(cam_param_1: Sequence[Union[int, float, str]], cam_param_2: Sequence[Union[int, float, str]], rel_pose: Sequence[Union[int, float]], row_1: MaybeSequence[Union[int, float]], col_1: MaybeSequence[Union[int, float]], row_2: MaybeSequence[Union[int, float]], col_2: MaybeSequence[Union[int, float]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def intersect_lines_of_sight_s(cam_param_1: Sequence[Union[int, float, str]], cam_param_2: Sequence[Union[int, float, str]], rel_pose: Sequence[Union[int, float]], row_1: MaybeSequence[Union[int, float]], col_1: MaybeSequence[Union[int, float]], row_2: MaybeSequence[Union[int, float]], col_2: MaybeSequence[Union[int, float]]) -> Tuple[float, float, float, float]`

## Description

Given two lines of sight from different cameras, specified by their
image points (*`row_1`*,*`col_1`*) of camera 1 and
(*`row_2`*,*`col_2`*) of camera 2,
`intersect_lines_of_sight` computes the 3D
point of intersection of these lines. The binocular camera system is
specified by its internal camera parameters *`cam_param_1`* of the
projective camera 1 and *`cam_param_2`* of the projective camera 2, and
the external parameters *`rel_pose`*.
Latter one is of the form $ccs^1 P ccs^2$ ![figure](../assets/70dc27b5ce6d279e.svg)
and characterizes the relative pose of both cameras to each other,
thus defining a point transformation
from camera coordinate system 2 (*ccs2*) into camera coordinate
system 1 (*ccs1*), see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.
These camera parameters can be obtained, e.g., from
the operator [`calibrate_cameras`](calibrate_cameras.md), if the coordinates of the image
points (*`row_1`*,*`col_1`*) and (*`row_2`*,*`col_2`*)
refer to the respective original image coordinate system. In case of
rectified image coordinates ( e.g., obtained from rectified images),
the rectified camera parameters must be passed, as they are returned
by the operator
[`gen_binocular_rectification_map`](gen_binocular_rectification_map.md). The 'point of
intersection' is defined by the point with the shortest distance to
both lines of sight. This point is returned in Cartesian coordinates
(*`x`*,*`y`*,*`z`*) of camera system 1 and its
distance to the lines of sight is passed in *`dist`*.

## Attention

Stereo setups that contain cameras with and without hypercentric
lenses at the same time are not supported.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cam_param_1`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal parameters of the projective camera 1.

**`cam_param_2`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal parameters of the projective camera 2.

**`rel_pose`** (input_control)  pose `→` Sequence[Union[int, float]]

Point transformation from camera 2 to camera 1.

Number of elements:
7

**`row_1`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Row coordinate of a point in image 1.

**`col_1`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Column coordinate of a point in image 1.

**`row_2`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Row coordinate of the corresponding point in image 2.

**`col_2`** (input_control)  number(-array) `→` MaybeSequence[Union[int, float]]

Column coordinate of the corresponding point in image 2.

**`x`** (output_control)  real(-array) `→` Sequence[float]

X coordinate of the 3D point.

**`y`** (output_control)  real(-array) `→` Sequence[float]

Y coordinate of the 3D point.

**`z`** (output_control)  real(-array) `→` Sequence[float]

Z coordinate of the 3D point.

**`dist`** (output_control)  real(-array) `→` Sequence[float]

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
