# VectorToRelPose (Operator)

## Name

`VectorToRelPose` — Compute the relative orientation between two cameras given image point
correspondences and known camera parameters and reconstruct 3D space points.

## Signature

`static void HOperatorSet.VectorToRelPose(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HTuple camPar1, HTuple camPar2, HTuple method, out HTuple relPose, out HTuple covRelPose, out HTuple error, out HTuple x, out HTuple y, out HTuple z, out HTuple covXYZ)`

`HPose HCamPar.VectorToRelPose(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HCamPar camPar2, string method, out HTuple covRelPose, out HTuple error, out HTuple x, out HTuple y, out HTuple z, out HTuple covXYZ)`

`HPose HCamPar.VectorToRelPose(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HCamPar camPar2, string method, out HTuple covRelPose, out double error, out HTuple x, out HTuple y, out HTuple z, out HTuple covXYZ)`

`HTuple HPose.VectorToRelPose(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HCamPar camPar1, HCamPar camPar2, string method, out HTuple error, out HTuple x, out HTuple y, out HTuple z, out HTuple covXYZ)`

`HTuple HPose.VectorToRelPose(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HCamPar camPar1, HCamPar camPar2, string method, out double error, out HTuple x, out HTuple y, out HTuple z, out HTuple covXYZ)`

## Description

For a stereo configuration with known camera parameters the geometric
relation between the two images is defined by the relative pose.
The operator `VectorToRelPose` computes the relative pose from
in general at least six point correspondences in the image pair.
*`relPose`* indicates the relative pose of camera 1 with respect
to camera 2 (see [`CreatePose`](create_pose.md) for more information about
poses and their representations.). This is in accordance with the
explicit calibration of a stereo setup using the operator
[`CalibrateCameras`](calibrate_cameras.md).
Now, let R,t be the rotation and translation
of the relative pose. Then, the essential matrix
E is defined as $E=([t]_{\times}R)^{T}$, where
$[t]_{\times}$ denotes the 3x3 skew-symmetric
matrix realizing the cross product with the vector t.
The pose can be determined from the epipolar constraint:

$$\left(\begin{array}{c}X_{2}\\Y_{2}\\1\end{array}\right)^{T} \cdot ( [t] \times R)^{T} \cdot \left(\begin{array}{c}X_{1}\\Y_{1}\\1\end{array}\right) = 0\quad\text{where}\quad [t]_{\times} = \left(\begin{array}{ccc}0 & -t_{z} & t_{y} \\ t_{z} & 0 & -t_{x} \\ -t_{y} & t_{x} & 0\end{array}\right).$$ ![figure](../assets/b9800f0e3c8505d7.svg)

Note, that the essential matrix is a projective entity and thus is
defined up to a scaling factor. From this follows that the
translation vector of the relative pose can only be determined up to
scale too. In fact, the computed translation vector will always be
normalized to unit length. As a consequence, a three-dimensional
reconstruction of the scene, here in terms of points given by their
coordinates (*`x`*,*`y`*,*`z`*), can be carried
out only up to a single global scaling factor. If the absolute 3D
coordinates of the reconstruction are to be achieved the unknown
scaling factor can be computed from a gauge, which has to be visible
in both images. For example, a simple gauge can be given by any
known distance between points in the scene.

The operator `VectorToRelPose` is designed to deal with
a camera model that includes lens distortions. This is in contrast to the
operator [`VectorToEssentialMatrix`](vector_to_essential_matrix.md), which encompasses only straight
line preserving cameras. The camera parameters are passed by the arguments
*`camPar1`*, *`camPar2`*. The
3D direction vectors $(X_{1},Y_{1},1)$ and
$(X_{2},Y_{2},1)$ are calculated from the point
coordinates (*`rows1`*,*`cols1`*) and
(*`rows2`*,*`cols2`*) by inverting the process of
projection (see [Calibration](toc_calibration.md)).
The point correspondences are typically determined by applying the operator
[`MatchRelPoseRansac`](match_rel_pose_ransac.md).

The parameter *`method`* decides whether the relative orientation
between the cameras is of a special type and which algorithm is to be applied
for its computation.
If *`method`* is either *"normalized_dlt"* or
*"gold_standard"* the relative orientation is arbitrary.
Choosing *"trans_normalized_dlt"* or *"trans_gold_standard"*
means that the relative motion between the cameras is a pure translation.
The typical application for this special motion case is the
scenario of a single fixed camera looking onto a moving conveyor belt.
In this case the minimum required number of corresponding points is just two
instead of six in the general case.

The relative pose is computed by a linear algorithm if
*"normalized_dlt"* or *"trans_normalized_dlt"* is chosen.
With *"gold_standard"* or *"trans_gold_standard"*
the algorithm gives a statistically optimal result.
Here, *"normalized_dlt"* and *"gold_standard"* stand for
direct-linear-transformation and gold-standard-algorithm respectively.
All methods return the coordinates (*`x`*,*`y`*,*`z`*)
of the reconstructed 3D points. The optimal methods also return
the covariances of the 3D points in *`covXYZ`*.
Let n be the number of points
then the 3x3 covariance matrices are concatenated and
stored in a tuple of length 9n.
Additionally, the optimal methods return the 6x6 covariance
matrix of the pose *`covRelPose`*.

If an optimal gold-standard-algorithm is chosen the covariances of the image
points (*`covRR1`*, *`covRC1`*, *`covCC1`*, *`covRR2`*,
*`covRC2`*, *`covCC2`*) can be incorporated in the computation.
They can be provided for example by the operator [`PointsFoerstner`](points_foerstner.md).
If the point covariances are unknown, which is the default, empty tuples
are input. In this case the optimization algorithm internally assumes
uniform and equal covariances for all points.

The value *`error`* indicates the overall quality of the optimization
process and is the root-mean-square Euclidean distance in pixels between the
points and their corresponding epipolar lines.

For the operator `VectorToRelPose` a special configuration
of scene points and cameras exists: if all 3D points lie in a single plane
and additionally are all closer to one of the two cameras then the solution
in the relative pose is not unique but twofold. As a consequence both
solutions are computed and returned by the operator.
This means that all output parameters are of double length and the values
of the second solution are simply concatenated behind the values of the
first one.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rows1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (row coordinate).

Restriction:
`length(Rows1) >= 6 || length(Rows1) >= 2`

**`cols1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (column coordinate).

Restriction:
`length(Cols1) == length(Rows1)`

**`rows2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (row coordinate).

Restriction:
`length(Rows2) == length(Rows1)`

**`cols2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (column coordinate).

Restriction:
`length(Cols2) == length(Rows1)`

**`covRR1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate variance of the points in image 1.

Default:
[]

**`covRC1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Covariance of the points in image 1.

Default:
[]

**`covCC1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate variance of the points in image 1.

Default:
[]

**`covRR2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate variance of the points in image 2.

Default:
[]

**`covRC2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Covariance of the points in image 2.

Default:
[]

**`covCC2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate variance of the points in image 2.

Default:
[]

**`camPar1`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Camera parameters of the 1st camera.

**`camPar2`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Camera parameters of the 2nd camera.

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Algorithm for the computation of the
relative pose and for special pose types.

Default:
"normalized_dlt"

List of values:
"gold_standard", "normalized_dlt", "trans_gold_standard", "trans_normalized_dlt"

**`relPose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Computed relative orientation of the cameras (3D pose).

**`covRelPose`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

6x6 covariance matrix of the
relative camera orientation.

**`error`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Root-Mean-Square of the epipolar distance error.

**`x`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the reconstructed 3D points.

**`y`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the reconstructed 3D points.

**`z`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the reconstructed 3D points.

**`covXYZ`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Covariance matrices of the reconstructed 3D points.

## Possible Predecessors

`MatchRelPoseRansac`

## Possible Successors

`GenBinocularRectificationMap`,
`RelPoseToFundamentalMatrix`

## Alternatives

`VectorToEssentialMatrix`,
`VectorToFundamentalMatrix`,
`BinocularCalibration`

## See also

`CameraCalibration`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
J.Chris McGlone (editor): “Manual of Photogrammetry”;
American Society for Photogrammetry and Remote Sensing ; 2004.

## Module

3D Metrology
