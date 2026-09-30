# IntersectLinesOfSight (Operator)

## Name

`IntersectLinesOfSight` — Get a 3D point from the intersection of two lines of sight
within a binocular camera system.

## Signature

`static void HOperatorSet.IntersectLinesOfSight(HTuple camParam1, HTuple camParam2, HTuple relPose, HTuple row1, HTuple col1, HTuple row2, HTuple col2, out HTuple x, out HTuple y, out HTuple z, out HTuple dist)`

`void HCamPar.IntersectLinesOfSight(HCamPar camParam2, HPose relPose, HTuple row1, HTuple col1, HTuple row2, HTuple col2, out HTuple x, out HTuple y, out HTuple z, out HTuple dist)`

`void HCamPar.IntersectLinesOfSight(HCamPar camParam2, HPose relPose, double row1, double col1, double row2, double col2, out double x, out double y, out double z, out double dist)`

`void HPose.IntersectLinesOfSight(HCamPar camParam1, HCamPar camParam2, HTuple row1, HTuple col1, HTuple row2, HTuple col2, out HTuple x, out HTuple y, out HTuple z, out HTuple dist)`

`void HPose.IntersectLinesOfSight(HCamPar camParam1, HCamPar camParam2, double row1, double col1, double row2, double col2, out double x, out double y, out double z, out double dist)`

## Description

Given two lines of sight from different cameras, specified by their
image points (*`row1`*,*`col1`*) of camera 1 and
(*`row2`*,*`col2`*) of camera 2,
`IntersectLinesOfSight` computes the 3D
point of intersection of these lines. The binocular camera system is
specified by its internal camera parameters *`camParam1`* of the
projective camera 1 and *`camParam2`* of the projective camera 2, and
the external parameters *`relPose`*.
Latter one is of the form $ccs^1 P ccs^2$ ![figure](../assets/70dc27b5ce6d279e.svg)
and characterizes the relative pose of both cameras to each other,
thus defining a point transformation
from camera coordinate system 2 (*ccs2*) into camera coordinate
system 1 (*ccs1*), see [Transformations / Poses](toc_transformations_poses.md) and
`“Solution Guide III-C - 3D Vision”`.
These camera parameters can be obtained, e.g., from
the operator [`CalibrateCameras`](calibrate_cameras.md), if the coordinates of the image
points (*`row1`*,*`col1`*) and (*`row2`*,*`col2`*)
refer to the respective original image coordinate system. In case of
rectified image coordinates ( e.g., obtained from rectified images),
the rectified camera parameters must be passed, as they are returned
by the operator
[`GenBinocularRectificationMap`](gen_binocular_rectification_map.md). The 'point of
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

**`camParam1`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal parameters of the projective camera 1.

**`camParam2`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal parameters of the projective camera 2.

**`relPose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Point transformation from camera 2 to camera 1.

Number of elements:
7

**`row1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of a point in image 1.

**`col1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of a point in image 1.

**`row2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the corresponding point in image 2.

**`col2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the corresponding point in image 2.

**`x`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinate of the 3D point.

**`y`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinate of the 3D point.

**`z`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinate of the 3D point.

**`dist`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Distance of the 3D point to the lines of sight.

## Result

`IntersectLinesOfSight` returns 2 (
H_MSG_TRUE)
if all parameter values
are correct. If necessary, an exception is raised.

## Possible Predecessors

`BinocularCalibration`

## See also

`DisparityToPoint3d`

## Module

3D Metrology
