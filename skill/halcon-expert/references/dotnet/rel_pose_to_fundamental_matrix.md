# RelPoseToFundamentalMatrix (Operator)

## Name

`RelPoseToFundamentalMatrix` — Compute the fundamental matrix from the relative orientation of two
cameras.

## Signature

`static void HOperatorSet.RelPoseToFundamentalMatrix(HTuple relPose, HTuple covRelPose, HTuple camPar1, HTuple camPar2, out HTuple FMatrix, out HTuple covFMat)`

`HHomMat2D HCamPar.RelPoseToFundamentalMatrix(HPose relPose, HTuple covRelPose, HCamPar camPar2, out HTuple covFMat)`

`HHomMat2D HPose.RelPoseToFundamentalMatrix(HTuple covRelPose, HCamPar camPar1, HCamPar camPar2, out HTuple covFMat)`

`HTuple HHomMat2D.RelPoseToFundamentalMatrix(HPose relPose, HTuple covRelPose, HCamPar camPar1, HCamPar camPar2)`

## Description

Cameras including lens distortions can be modeled by the following
set of parameters: the focal length f, two scaling factors
$s_{x},s_{y}$, the coordinates of the principal point
$(c_{x},c_{y})$ and the distortion coefficient
$\kappa$. For a more detailed description see the
chapter [Calibration](toc_calibration.md). Only cameras with a distortion
coefficient equal to zero project straight lines in the world onto
straight lines in the image. This is also true for telecentric
cameras and for cameras with tilt lenses.
`RelPoseToFundamentalMatrix` handles telecentric lenses
and tilt lenses correctly. However, for reasons of simplicity, these
lens types are ignored in the formulas below. If the distortion
coefficient is equal to zero, image projection is a linear mapping
and the camera, i.e., the set of internal parameters, can be
described by the camera matrix CamMat:
$$CamMat = \left(\begin{array}{ccc} \frac{f}{s_x} & 0 & c_x \\ 0 & \frac{f}{s_y} & c_y \\ 0 & 0 & 1 \end{array}\right).$$ ![figure](../assets/28f03f71e47f7bc4.svg)
Going from a nonlinear model to a linear model is an approximation
of the real underlying camera. For a variety of camera lenses,
especially lenses with long focal length, the error induced by this
approximation can be neglected. Following the formula
$E=([t]_{\times}R)^{T}$, the essential matrix
E is derived from the translation t and the
rotation R of the relative pose *`relPose`* (see also
operator [`VectorToRelPose`](vector_to_rel_pose.md)). In the linearized framework
the fundamental matrix can be calculated from the relative pose and
the camera matrices according to the formula presented under
[`EssentialToFundamentalMatrix`](essential_to_fundamental_matrix.md):
$$\texttt{FMatrix}=CamMat2^{-T}\cdot([t]_{\times}R)^{T}\cdot CamMat1^{-1}.$$
The transformation from a relative pose to a fundamental matrix goes
along with the propagation of the covariance matrices
*`covRelPose`* to *`covFMat`*. If *`covRelPose`* is
empty *`covFMat`* will be empty too.

The conversion operator `RelPoseToFundamentalMatrix` is
used especially for a subsequent visualization of the epipolar line
structure via the fundamental matrix, which depicts the underlying
stereo geometry.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`relPose`** (input_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Relative orientation of the cameras (3D pose).

**`covRelPose`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

6x6 covariance matrix of
relative pose.

Default:
[]

**`camPar1`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Parameters of the 1. camera.

**`camPar2`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Parameters of the 2. camera.

**`FMatrix`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Computed fundamental matrix.

**`covFMat`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

9x9 covariance matrix of the
fundamental matrix.

## Possible Predecessors

`VectorToRelPose`

## Alternatives

`EssentialToFundamentalMatrix`

## See also

`CalibrateCameras`

## Module

3D Metrology
