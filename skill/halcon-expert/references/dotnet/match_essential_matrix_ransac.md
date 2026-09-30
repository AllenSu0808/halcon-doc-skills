# MatchEssentialMatrixRansac (Operator)

## Name

`MatchEssentialMatrixRansac` — Compute the essential matrix for a pair of stereo images by automatically
finding correspondences between image points.

## Signature

`static void HOperatorSet.MatchEssentialMatrixRansac(HObject image1, HObject image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple camMat1, HTuple camMat2, HTuple grayMatchMethod, HTuple maskSize, HTuple rowMove, HTuple colMove, HTuple rowTolerance, HTuple colTolerance, HTuple rotation, HTuple matchThreshold, HTuple estimationMethod, HTuple distanceThreshold, HTuple randSeed, out HTuple EMatrix, out HTuple covEMat, out HTuple error, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.MatchEssentialMatrixRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HHomMat2D camMat1, HHomMat2D camMat2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out HTuple covEMat, out HTuple error, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.MatchEssentialMatrixRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HHomMat2D camMat1, HHomMat2D camMat2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple covEMat, out double error, out HTuple points1, out HTuple points2)`

`HHomMat2D HHomMat2D.MatchEssentialMatrixRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HHomMat2D camMat2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out HTuple covEMat, out HTuple error, out HTuple points1, out HTuple points2)`

`HHomMat2D HHomMat2D.MatchEssentialMatrixRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HHomMat2D camMat2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple covEMat, out double error, out HTuple points1, out HTuple points2)`

## Description

Given a set of coordinates of characteristic points
(*`rows1`*,*`cols1`*) and
(*`rows2`*,*`cols2`*) in the stereo images
*`image1`* and *`image2`* along with known internal camera
parameters, specified by the camera matrices *`camMat1`* and
*`camMat2`*, `MatchEssentialMatrixRansac`
automatically determines the geometry of the stereo setup and finds
the correspondences between the characteristic points. The geometry
of the stereo setup is represented by the essential matrix
*`EMatrix`* and all corresponding points have to fulfill the
epipolar constraint.

The operator `MatchEssentialMatrixRansac` is designed to deal with
a linear camera model.
The internal camera parameters are passed by the arguments
*`camMat1`* and *`camMat2`*, which are
3x3 upper triangular matrices describing an affine
transformation. The relation between a vector (X,Y,1), representing the
direction from the camera to the viewed 3D space point and its (projective)
2D image coordinates (col,row,1) is:
$$\begin{pmatrix} col \\ row \\ 1 \end{pmatrix} = CamMat \cdot \begin{pmatrix} X \\ Y \\ 1 \end{pmatrix} \quad \text{where} \quad CamMat = \begin{pmatrix} f/s_x & s & c_x \\ 0 & f/s_y & c_y \\ 0 & 0 & 1 \end{pmatrix}.$$ ![figure](../assets/c8408b13b84e9903.svg)

Note the column/row ordering in the point coordinates which has to
be compliant with the x/y notation of the camera coordinate system.
The focal length is denoted by f, $s_{x},s_{y}$ are
scaling factors, s describes a skew factor and
$(c_{x},c_{y})$ indicates the principal point.
Mainly, these are the elements known from the camera parameters as used for
example in [`CalibrateCameras`](calibrate_cameras.md). Alternatively, the elements
of the camera matrix can be described in a different way, see e.g.
[`StationaryCameraSelfCalibration`](stationary_camera_self_calibration.md).
Multiplied by the inverse of the camera matrices the direction
vectors in 3D space are obtained from the (projective) image
coordinates. For
known camera matrices the epipolar constraint is given by:

$$\left(\begin{array}{c}X_{2}\\Y_{2}\\1\end{array}\right)^{T} \cdot EM^atrix \cdot \left(\begin{array}{c}X_{1}\\Y_{1}\\1\end{array}\right) = 0$$ ![figure](../assets/0d676954b904b2ca.svg)

The matching process is based on characteristic points, which can be
extracted with point operators like [`PointsFoerstner`](points_foerstner.md) or
[`PointsHarris`](points_harris.md).
The matching itself is carried out in two steps: first, gray value
correlations of mask windows around the input points in the first
and the second image are determined and an initial matching between
them is generated using the similarity of the windows in both images.
Then, the RANSAC algorithm is applied to find the essential matrix
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
(RANSAC) is used to determine the essential matrix
*`EMatrix`*. It tries to find the essential matrix that is consistent
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

The essential matrix is computed by a linear algorithm if
*"normalized_dlt"* or *"trans_normalized_dlt"* is chosen.
With *"gold_standard"* or *"trans_gold_standard"*
the algorithm gives a statistically optimal result, and returns the
covariance of the essential matrix *`covEMat`* as well.
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

For the operator `MatchEssentialMatrixRansac` a special
configuration of scene points and cameras exists: if all 3D points lie in a
single plane and additionally are all closer to one of the two cameras then
the solution in the essential matrix is not unique but twofold.
As a consequence both solutions are computed and returned by the operator.
This means that the output parameters *`EMatrix`*, *`covEMat`*
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
`MatchEssentialMatrixRansac`.

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

**`camMat1`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double* / int / long)

Camera matrix of the 1st camera.

**`camMat2`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double* / int / long)

Camera matrix of the 2nd camera.

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
essential matrix and for special camera orientations.

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

**`EMatrix`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Computed essential matrix.

**`covEMat`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

9x9 covariance matrix of the
essential matrix.

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

`VectorToEssentialMatrix`

## See also

`MatchFundamentalMatrixRansac`,
`MatchRelPoseRansac`,
`StationaryCameraSelfCalibration`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

3D Metrology
