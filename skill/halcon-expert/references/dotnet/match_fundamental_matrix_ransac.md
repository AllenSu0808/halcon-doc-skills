# MatchFundamentalMatrixRansac (Operator)

## Name

`MatchFundamentalMatrixRansac` — Compute the fundamental matrix for a pair of stereo images by
automatically finding correspondences between image
points.

## Signature

`static void HOperatorSet.MatchFundamentalMatrixRansac(HObject image1, HObject image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple grayMatchMethod, HTuple maskSize, HTuple rowMove, HTuple colMove, HTuple rowTolerance, HTuple colTolerance, HTuple rotation, HTuple matchThreshold, HTuple estimationMethod, HTuple distanceThreshold, HTuple randSeed, out HTuple FMatrix, out HTuple covFMat, out HTuple error, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.MatchFundamentalMatrixRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out HTuple covFMat, out double error, out HTuple points1, out HTuple points2)`

`HHomMat2D HImage.MatchFundamentalMatrixRansac(HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out HTuple covFMat, out double error, out HTuple points1, out HTuple points2)`

`HTuple HHomMat2D.MatchFundamentalMatrixRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, HTuple rotation, HTuple matchThreshold, string estimationMethod, HTuple distanceThreshold, int randSeed, out double error, out HTuple points1, out HTuple points2)`

`HTuple HHomMat2D.MatchFundamentalMatrixRansac(HImage image1, HImage image2, HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, string grayMatchMethod, int maskSize, int rowMove, int colMove, int rowTolerance, int colTolerance, double rotation, int matchThreshold, string estimationMethod, double distanceThreshold, int randSeed, out double error, out HTuple points1, out HTuple points2)`

## Description

Given a set of coordinates of characteristic points
(*`rows1`*,*`cols1`*) and
(*`rows2`*,*`cols2`*) in the stereo images
*`image1`* and *`image2`*,
`MatchFundamentalMatrixRansac` automatically finds the
correspondences between the characteristic points and determines the
geometry of the stereo setup. For unknown cameras the geometry of the
stereo setup is represented by the fundamental matrix *`FMatrix`*
and all corresponding points have to fulfill the epipolar
constraint, namely:
$$\left( \begin{array}{c} Cols2\\ Rows2\\ 1 \end{array} \right)^{T} \cdot FMatrix \cdot \left( \begin{array}{c} Cols1\\ Rows1\\ 1 \end{array} \right) = 0 .$$ ![figure](../assets/b69e7601de8b5cef.svg)

Note the column/row ordering in the point coordinates: because the
fundamental matrix encodes the projective relation between two
stereo images embedded in 3D space, the x/y notation has to be
compliant with the camera coordinate system. So, (x,y) coordinates
correspond to (column,row) pairs.

The matching process is based on characteristic points, which can be
extracted with point operators like [`PointsFoerstner`](points_foerstner.md) or
[`PointsHarris`](points_harris.md).
The matching itself is carried out in two steps: first, gray value
correlations of mask windows around the input points in the first
and the second image are determined and an initial matching between
them is generated using the similarity of the windows in both images.
Then, the RANSAC algorithm is applied to find the fundamental matrix
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

To increase the speed of the algorithm the search area for the
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
specified and *`rotation`* is a tuple with two elements. The
larger the given interval the slower the operator is since the
RANSAC algorithm is run over all angle increments within the
interval.

After the initial matching is completed a randomized search algorithm
(RANSAC) is used to determine the fundamental matrix
*`FMatrix`*. It tries to find the matrix that is consistent
with a maximum number of correspondences.
For a point to be accepted, the distance to its corresponding epipolar line
must not exceed the threshold *`distanceThreshold`*.

The parameter *`estimationMethod`* decides whether the relative
orientation between the cameras is of a special type and which algorithm is
to be applied for its computation.
If *`estimationMethod`* is either *"normalized_dlt"* or
*"gold_standard"* the relative orientation is arbitrary.
If left and right camera are identical and the relative orientation between
them is a pure translation then choose *`estimationMethod`* equal to
*"trans_normalized_dlt"* or *"trans_gold_standard"*.
The typical application for this special motion case is the
scenario of a single fixed camera looking onto a moving conveyor belt.
In order to get a unique solution in the correspondence problem the minimum
required number of corresponding points is eight in the general case and
three in the special, translational case.

The fundamental matrix is computed by a linear algorithm if
*"normalized_dlt"* or *"trans_normalized_dlt"* is chosen.
With *"gold_standard"* or *"trans_gold_standard"*
the algorithm gives a statistically optimal result, and returns as well the
covariance of the fundamental matrix *`covFMat`*.
Here, *"normalized_dlt"* and *"gold_standard"* stand for
direct-linear-transformation and gold-standard-algorithm respectively.

The value *`error`* indicates the overall quality of the estimation
procedure and is the mean Euclidean distance in pixels between the
points and their corresponding epipolar lines.

Point pairs consistent with the mentioned constraints are considered to be
in correspondences. *`points1`* contains the indices of the
matched input points from the first image and *`points2`* contains
the indices of the corresponding points in the second image.

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
`MatchFundamentalMatrixRansac`.

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
`length(Rows1) >= 8 || length(Rows1) >= 3`

**`cols1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of characteristic points
in image 1.

Restriction:
`length(Cols1) == length(Rows1)`

**`rows2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of characteristic points
in image 2.

Restriction:
`length(Rows2) >= 8 || length(Rows2) >= 3`

**`cols2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of characteristic points
in image 2.

Restriction:
`length(Cols2) == length(Rows2)`

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
fundamental matrix and for special camera orientations.

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

**`FMatrix`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Computed fundamental matrix.

**`covFMat`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

9x9 covariance matrix of the
fundamental matrix.

**`error`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Root-Mean-Square of the epipolar distance error.

**`points1`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of matched input points in image 1.

**`points2`** (output_control)  integer-array `→` [HTuple](HTuple.md) (*int* / long)

Indices of matched input points in image 2.

## Possible Predecessors

`PointsFoerstner`,
`PointsHarris`

## Possible Successors

`VectorToFundamentalMatrix`,
`GenBinocularProjRectification`

## See also

`MatchEssentialMatrixRansac`,
`MatchRelPoseRansac`,
`ProjMatchPointsRansac`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

3D Metrology
