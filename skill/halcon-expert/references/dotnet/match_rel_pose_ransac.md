# MatchRelPoseRansac (Operator)

## Name

`MatchRelPoseRansac` — Compute the relative orientation between two cameras by automatically
finding correspondences between image points.

## Signature

`static void HOperatorSet.MatchRelPoseRansac(HObject image1, HObject image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple camPar1, HTuple camPar2, HTuple grayMatchMethod, HTuple maskSize, HTuple rowMove, HTuple colMove, HTuple rowTolerance, HTuple colTolerance, HTuple rotation, HTuple matchThreshold, HTuple estimationMethod, HTuple distanceThreshold, HTuple randSeed, out HTuple relPose, out HTuple covRelPose, out HTuple error, out HTuple points1, out HTuple points2)`

`HPose HImage.MatchRelPoseRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HCamPar camPar1, HCamPar camPar2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out HTuple covRelPose, out HTuple error, out HTuple points1, out HTuple points2)`

`HPose HImage.MatchRelPoseRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HCamPar camPar1, HCamPar camPar2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple covRelPose, out double error, out HTuple points1, out HTuple points2)`

`HPose HCamPar.MatchRelPoseRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HCamPar camPar2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out HTuple covRelPose, out HTuple error, out HTuple points1, out HTuple points2)`

`HPose HCamPar.MatchRelPoseRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HCamPar camPar2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple covRelPose, out double error, out HTuple points1, out HTuple points2)`

`HTuple HPose.MatchRelPoseRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HCamPar camPar1, HCamPar camPar2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out HTuple error, out HTuple points1, out HTuple points2)`

`HTuple HPose.MatchRelPoseRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HCamPar camPar1, HCamPar camPar2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out double error, out HTuple points1, out HTuple points2)`

## Description

Given a set of coordinates of characteristic points
(*`rows1`*,*`cols1`*) and (*`rows2`*,*`cols2`*)
in the stereo images *`image1`* and *`image2`*
along with known internal camera parameters *`camPar1`* and
*`camPar2`*,
`MatchRelPoseRansac` automatically determines the geometry
of the stereo setup and finds the correspondences between the characteristic
points. The geometry of the stereo setup is represented by the relative pose
*`relPose`* and all corresponding points have to fulfill the epipolar
constraint.
*`relPose`* indicates the relative pose of camera 1 with respect
to camera 2 (See [`CreatePose`](create_pose.md) for more information about
poses and their representations.). This is in accordance with the
explicit calibration of a stereo setup using the operator
[`CalibrateCameras`](calibrate_cameras.md).
Now, let R,t be the rotation and translation
of the relative pose. Then, the essential matrix
E is defined as $E=([t]_{\times}R)^{T}$, where
$[t]_{\times}$ denotes the 3x3 skew-symmetric
matrix realizing the cross product with the vector t. The
pose can be determined from the epipolar constraint:

$$\left(\begin{array}{c}X_{2}\\Y_{2}\\1\end{array}\right)^{T} \cdot ( [t] \times R)^{T} \cdot \left(\begin{array}{c}X_{1}\\Y_{1}\\1\end{array}\right) = 0\quad\text{where}\quad [t]_{\times} = \left(\begin{array}{ccc}0 & -t_{z} & t_{y} \\ t_{z} & 0 & -t_{x} \\ -t_{y} & t_{x} & 0\end{array}\right).$$ ![figure](../assets/b9800f0e3c8505d7.svg)

Note, that the essential matrix is a projective entity and thus is
defined up to a scaling factor. From this follows that the
translation vector of the relative pose can only be determined up to
scale too. In fact, the computed translation vector will always be
normalized to unit length. As a consequence, a subsequent
three-dimensional reconstruction of the scene, using for instance
[`VectorToRelPose`](vector_to_rel_pose.md), can be carried out only
up to a single global scaling factor.

The operator `MatchRelPoseRansac` is designed to deal with
a camera model, that includes lens distortions. This is in contrast
to the operator [`MatchEssentialMatrixRansac`](match_essential_matrix_ransac.md), which
encompasses only straight line preserving cameras. The camera
parameters are passed in *`camPar1`* and *`camPar2`*. The
3D direction vectors $(X_{1},Y_{1},1)$ and
$(X_{2},Y_{2},1)$ are calculated from the point
coordinates (*`rows1`*,*`cols1`*) and
(*`rows2`*,*`cols2`*) by inverting the process of
projection (see [Calibration](toc_calibration.md)).

The matching process is based on characteristic points, which can be
extracted with point operators like [`PointsFoerstner`](points_foerstner.md) or
[`PointsHarris`](points_harris.md).
The matching itself is carried out in two steps: first, gray value
correlations of mask windows around the input points in the first
and the second image are determined and an initial matching between
them is generated using the similarity of the windows in both images.
Then, the RANSAC algorithm is applied to find the relative pose
that maximizes the number of correspondences under the epipolar constraint.

The size of the mask windows is *`maskSize`* x *`maskSize`*. Three
metrics for the correlation can be selected. If
*`grayMatchMethod`* has the value *"ssd"*, the sum of
the squared gray value differences is used, *"sad"* means the
sum of absolute differences, and *"ncc"* is the normalized
cross correlation. For details please refer to
[`BinocularDisparity`](binocular_disparity.md). The metric is minimized (*"ssd"*,
*"sad"*) or maximized (*"ncc"*) over all possible
point pairs. A thus found matching is only accepted if the value of
the metric is below the value of *`matchThreshold`*
(*"ssd"*, *"sad"*) or above that value
(*"ncc"*).

To increase the speed of the algorithm, the search area for the
matching operations can be limited. Only points within a window of $2\cdot\texttt{RowTolerance}\times2\cdot\texttt{ColTolerance}$ points are considered. The offset of the
center of the search window in the second image with respect to the
position of the current point in the first image is given by
*`rowMove`* and *`colMove`*.

If the second camera is
rotated around the optical axis with respect to the first camera
the parameter *`rotation`* may contain an estimate for the
rotation angle or an angle interval in radians. A good guess will
increase the quality of the gray value matching. If the actual
rotation differs too much from the specified estimate the matching
will typically fail. In this case, an angle interval should be
specified, and *`rotation`* is a tuple with two elements. The
larger the given interval the slower the operator is since the
RANSAC algorithm is run over all angle increments within the
interval.

After the initial matching is completed a randomized search algorithm
(RANSAC) is used to determine the relative pose *`relPose`*.
It tries to find the relative pose that is consistent
with a maximum number of correspondences.
For a point to be accepted, the distance to its corresponding epipolar line
must not exceed the threshold *`distanceThreshold`*.

The parameter *`estimationMethod`* decides whether the relative
orientation between the cameras is of a special type and which algorithm is
to be applied for its computation.
If *`estimationMethod`* is either *"normalized_dlt"* or
*"gold_standard"* the relative orientation is arbitrary.
Choosing *"trans_normalized_dlt"* or *"trans_gold_standard"*
means that the relative motion between the cameras is a pure translation.
The typical application for this special motion case is the
scenario of a single fixed camera looking onto a moving conveyor belt.
In order to get a unique solution in the correspondence problem the minimum
required number of corresponding points is six in the general case and three
in the special, translational case.

The relative pose is computed by a linear algorithm if
*"normalized_dlt"* or *"trans_normalized_dlt"* is chosen.
With *"gold_standard"* or *"trans_gold_standard"*
the algorithm gives a statistically optimal result, and returns as well the
covariance of the relative pose *`covRelPose`*.
Here, *"normalized_dlt"* and *"gold_standard"* stand for
direct-linear-transformation and gold-standard-algorithm respectively.
Note, that in general the found correspondences differ depending on the
deployed estimation method.

The value *`error`* indicates the overall quality of the estimation
procedure and is the mean Euclidean distance in pixels between the
points and their corresponding epipolar lines.

Point pairs consistent with the mentioned constraints are considered to be
in correspondences. *`points1`* contains the indices of the
matched input points from the first image and *`points2`* contains
the indices of the corresponding points in the second image.

For the operator `MatchRelPoseRansac` a special
configuration of scene points and cameras exists: if all 3D points lie in a
single plane and additionally are all closer to one of the two cameras then
the solution in the essential matrix is not unique but twofold.
As a consequence both solutions are computed and returned by the operator.
This means that the output parameters *`relPose`*, *`covRelPose`*
and *`error`* are of double length and the values of the second
solution are simply concatenated behind the values of the first one.

The parameter *`randSeed`* can be used to control the
randomized nature of the RANSAC algorithm, and hence to obtain
reproducible results. If *`randSeed`* is set to a positive
number the operator yields the same result on every call with the
same parameters because the internally used random number generator
is initialized with the *`randSeed`*. If *`randSeed`* =
*0* the random number generator is initialized with the
current time. In this case the results may not be reproducible.
The value set for the HALCON system variable *"seed_rand"*
(see [`SetSystem`](set_system.md)) does not affect the results of
`MatchRelPoseRansac`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image1`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image 1.

**`image2`** (input_object)  singlechannelimage `→` [HImage](HImage.md) (byte / uint2)

Input image 2.

**`rows1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of characteristic points
in image 1.

Restriction:
`length(Rows1) >= 6 || length(Rows1) >= 3`

**`cols1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of characteristic points
in image 1.

Restriction:
`length(Cols1) == length(Rows1)`

**`rows2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of characteristic points
in image 2.

Restriction:
`length(Rows2) >= 6 || length(Rows2) >= 3`

**`cols2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of characteristic points
in image 2.

Restriction:
`length(Cols2) == length(Rows2)`

**`camPar1`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Parameters of the 1st camera.

**`camPar2`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Parameters of the 2nd camera.

**`grayMatchMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Gray value comparison metric.

Default:
"ssd"

List of values:
"ncc", "sad", "ssd"

**`maskSize`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Size of gray value masks.

Default:
10

Suggested values:
3, 7, 15

Value range:
`1
≤
maskSize`

**`rowMove`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Average row coordinate shift of corresponding points.

Default:
0

Value range:
`0
≤
rowMove
≤
200`

**`colMove`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Average column coordinate shift of
corresponding points.

Default:
0

Value range:
`0
≤
colMove
≤
200`

**`rowTolerance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Half height of matching search window.

Default:
200

Value range:
`1
≤
rowTolerance`

**`colTolerance`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Half width of matching search window.

Default:
200

Value range:
`1
≤
colTolerance`

**`rotation`** (input_control)  angle.rad(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Estimate of the relative orientation of the right image
with respect to the left image.

Default:
0.0

Suggested values:
0.0, 0.1, -0.1, 0.7854, 1.571, 3.142

**`matchThreshold`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long / double)

Threshold for gray value matching.

Default:
10

Suggested values:
10, 20, 50, 100, 0.9, 0.7

**`estimationMethod`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Algorithm for the computation of the
relative pose and for special pose types.

Default:
"normalized_dlt"

List of values:
"gold_standard", "normalized_dlt", "trans_gold_standard", "trans_normalized_dlt"

**`distanceThreshold`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Maximal deviation of a point from its epipolar line.

Default:
1

Value range:
`0.5
≤
distanceThreshold
≤
5`

Restriction:
`DistanceThreshold > 0`

**`randSeed`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Seed for the random number generator.

Default:
0

**`relPose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Computed relative orientation of the cameras
(3D pose).

**`covRelPose`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

6x6 covariance matrix of the
relative orientation.

**`error`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Root-Mean-Square of the epipolar distance error.

**`points1`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of matched input points in image 1.

**`points2`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of matched input points in image 2.

## Possible Predecessors

`PointsFoerstner`,
`PointsHarris`

## Possible Successors

`VectorToRelPose`,
`GenBinocularRectificationMap`

## See also

`BinocularCalibration`,
`MatchFundamentalMatrixRansac`,
`MatchEssentialMatrixRansac`,
`CreatePose`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

3D Metrology
