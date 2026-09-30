# match_essential_matrix_ransac (Operator)

## Name

`match_essential_matrix_ransac` — Compute the essential matrix for a pair of stereo images by automatically
finding correspondences between image points.

## Signature

`def match_essential_matrix_ransac(image_1: HObject, image_2: HObject, rows_1: Sequence[Union[float, int]], cols_1: Sequence[Union[float, int]], rows_2: Sequence[Union[float, int]], cols_2: Sequence[Union[float, int]], cam_mat_1: Sequence[Union[float, int]], cam_mat_2: Sequence[Union[float, int]], gray_match_method: str, mask_size: int, row_move: int, col_move: int, row_tolerance: int, col_tolerance: int, rotation: MaybeSequence[Union[float, int]], match_threshold: Union[int, float], estimation_method: str, distance_threshold: Union[float, int], rand_seed: int) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[int], Sequence[int]]`

`def match_essential_matrix_ransac_s(image_1: HObject, image_2: HObject, rows_1: Sequence[Union[float, int]], cols_1: Sequence[Union[float, int]], rows_2: Sequence[Union[float, int]], cols_2: Sequence[Union[float, int]], cam_mat_1: Sequence[Union[float, int]], cam_mat_2: Sequence[Union[float, int]], gray_match_method: str, mask_size: int, row_move: int, col_move: int, row_tolerance: int, col_tolerance: int, rotation: MaybeSequence[Union[float, int]], match_threshold: Union[int, float], estimation_method: str, distance_threshold: Union[float, int], rand_seed: int) -> Tuple[Sequence[float], Sequence[float], float, Sequence[int], Sequence[int]]`

## Description

Given a set of coordinates of characteristic points
(*`rows_1`*,*`cols_1`*) and
(*`rows_2`*,*`cols_2`*) in the stereo images
*`image_1`* and *`image_2`* along with known internal camera
parameters, specified by the camera matrices *`cam_mat_1`* and
*`cam_mat_2`*, `match_essential_matrix_ransac`
automatically determines the geometry of the stereo setup and finds
the correspondences between the characteristic points. The geometry
of the stereo setup is represented by the essential matrix
*`ematrix`* and all corresponding points have to fulfill the
epipolar constraint.

The operator `match_essential_matrix_ransac` is designed to deal with
a linear camera model.
The internal camera parameters are passed by the arguments
*`cam_mat_1`* and *`cam_mat_2`*, which are
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
example in [`calibrate_cameras`](calibrate_cameras.md). Alternatively, the elements
of the camera matrix can be described in a different way, see e.g.
[`stationary_camera_self_calibration`](stationary_camera_self_calibration.md).
Multiplied by the inverse of the camera matrices the direction
vectors in 3D space are obtained from the (projective) image
coordinates. For
known camera matrices the epipolar constraint is given by:

$$\left(\begin{array}{c}X_{2}\\Y_{2}\\1\end{array}\right)^{T} \cdot EM^atrix \cdot \left(\begin{array}{c}X_{1}\\Y_{1}\\1\end{array}\right) = 0$$ ![figure](../assets/0d676954b904b2ca.svg)

The matching process is based on characteristic points, which can be
extracted with point operators like [`points_foerstner`](points_foerstner.md) or
[`points_harris`](points_harris.md).
The matching itself is carried out in two steps: first, gray value
correlations of mask windows around the input points in the first
and the second image are determined and an initial matching between
them is generated using the similarity of the windows in both images.
Then, the RANSAC algorithm is applied to find the essential matrix
that maximizes the number of correspondences under the epipolar constraint.

The size of the mask windows is *`mask_size`* x *`mask_size`*. Three
metrics for the correlation can be selected. If
*`gray_match_method`* has the value *"ssd"*, the sum of
the squared gray value differences is used, *"sad"* means the
sum of absolute differences, and *"ncc"* is the normalized
cross correlation. For details please refer to
[`binocular_disparity`](binocular_disparity.md). The metric is minimized (*"ssd"*,
*"sad"*) or maximized (*"ncc"*) over all possible
point pairs. A thus found matching is only accepted if the value of
the metric is below the value of *`match_threshold`*
(*"ssd"*, *"sad"*) or above that value
(*"ncc"*).

To increase the speed of the algorithm, the search area for the
matching operations can be limited. Only points within a window of $2\cdot\texttt{RowTolerance}\times2\cdot\texttt{ColTolerance}$ points are considered. The offset of the
center of the search window in the second image with respect to the
position of the current point in the first image is given by
*`row_move`* and *`col_move`*.

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
*`ematrix`*. It tries to find the essential matrix that is consistent
with a maximum number of correspondences.
For a point to be accepted, the distance to its corresponding epipolar line
must not exceed the threshold *`distance_threshold`*.

The parameter *`estimation_method`* decides whether the relative
orientation between the cameras is of a special type and which algorithm is
to be applied for its computation.
If *`estimation_method`* is either *"normalized_dlt"* or
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
covariance of the essential matrix *`cov_emat`* as well.
Here, *"normalized_dlt"* and *"gold_standard"* stand for
direct-linear-transformation and gold-standard-algorithm respectively.
Note, that in general the found correspondences differ depending on the
deployed estimation method.

The value *`error`* indicates the overall quality of the estimation
procedure and is the mean Euclidean distance in pixels between the
points and their corresponding epipolar lines.

Point pairs consistent with the mentioned constraints are considered to be
in correspondences. *`points_1`* contains the indices of the
matched input points from the first image and *`points_2`* contains
the indices of the corresponding points in the second image.

For the operator `match_essential_matrix_ransac` a special
configuration of scene points and cameras exists: if all 3D points lie in a
single plane and additionally are all closer to one of the two cameras then
the solution in the essential matrix is not unique but twofold.
As a consequence both solutions are computed and returned by the operator.
This means that the output parameters *`ematrix`*, *`cov_emat`*
and *`error`* are of double length and the values of the second
solution are simply concatenated behind the values of the first one.

The parameter *`rand_seed`* can be used to control the
randomized nature of the RANSAC algorithm, and hence to obtain
reproducible results. If *`rand_seed`* is set to a positive
number the operator yields the same result on every call with the
same parameters because the internally used random number generator
is initialized with the *`rand_seed`*. If *`rand_seed`* =
*0* the random number generator is initialized with the
current time. In this case the results may not be reproducible.
The value set for the HALCON system variable *"seed_rand"*
(see [`set_system`](set_system.md)) does not affect the results of
`match_essential_matrix_ransac`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`image_1`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image 1.

**`image_2`** (input_object)  singlechannelimage `→` HObject (byte / uint2)

Input image 2.

**`rows_1`** (input_control)  number-array `→` Sequence[Union[float, int]]

Row coordinates of characteristic points
in image 1.

Restriction:
`length(Rows1) >= 6 || length(Rows1) >= 3`

**`cols_1`** (input_control)  number-array `→` Sequence[Union[float, int]]

Column coordinates of characteristic points
in image 1.

Restriction:
`length(Cols1) == length(Rows1)`

**`rows_2`** (input_control)  number-array `→` Sequence[Union[float, int]]

Row coordinates of characteristic points
in image 2.

Restriction:
`length(Rows2) >= 6 || length(Rows2) >= 3`

**`cols_2`** (input_control)  number-array `→` Sequence[Union[float, int]]

Column coordinates of characteristic points
in image 2.

Restriction:
`length(Cols2) == length(Rows2)`

**`cam_mat_1`** (input_control)  hom_mat2d `→` Sequence[Union[float, int]]

Camera matrix of the 1st camera.

**`cam_mat_2`** (input_control)  hom_mat2d `→` Sequence[Union[float, int]]

Camera matrix of the 2nd camera.

**`gray_match_method`** (input_control)  string `→` str

Gray value comparison metric.

Default:
"ssd"

List of values:
"ncc", "sad", "ssd"

**`mask_size`** (input_control)  integer `→` int

Size of gray value masks.

Default:
10

Suggested values:
3, 7, 15

Value range:
`1
≤
mask_size`

**`row_move`** (input_control)  integer `→` int

Average row coordinate shift of corresponding points.

Default:
0

Value range:
`0
≤
row_move
≤
200`

**`col_move`** (input_control)  integer `→` int

Average column coordinate shift of
corresponding points.

Default:
0

Value range:
`0
≤
col_move
≤
200`

**`row_tolerance`** (input_control)  integer `→` int

Half height of matching search window.

Default:
200

Value range:
`1
≤
row_tolerance`

**`col_tolerance`** (input_control)  integer `→` int

Half width of matching search window.

Default:
200

Value range:
`1
≤
col_tolerance`

**`rotation`** (input_control)  angle.rad(-array) `→` MaybeSequence[Union[float, int]]

Estimate of the relative orientation of the right image
with respect to the left image.

Default:
0.0

Suggested values:
0.0, 0.1, -0.1, 0.7854, 1.571, 3.142

**`match_threshold`** (input_control)  number `→` Union[int, float]

Threshold for gray value matching.

Default:
10

Suggested values:
10, 20, 50, 100, 0.9, 0.7

**`estimation_method`** (input_control)  string `→` str

Algorithm for the computation of the
essential matrix and for special camera orientations.

Default:
"normalized_dlt"

List of values:
"gold_standard", "normalized_dlt", "trans_gold_standard", "trans_normalized_dlt"

**`distance_threshold`** (input_control)  number `→` Union[float, int]

Maximal deviation of a point from its epipolar line.

Default:
1

Value range:
`0.5
≤
distance_threshold
≤
5`

Restriction:
`DistanceThreshold > 0`

**`rand_seed`** (input_control)  integer `→` int

Seed for the random number generator.

Default:
0

**`ematrix`** (output_control)  hom_mat2d `→` Sequence[float]

Computed essential matrix.

**`cov_emat`** (output_control)  real-array `→` Sequence[float]

9x9 covariance matrix of the
essential matrix.

**`error`** (output_control)  real(-array) `→` Sequence[float]

Root-Mean-Square of the epipolar distance error.

**`points_1`** (output_control)  integer-array `→` Sequence[int]

Indices of matched input points in image 1.

**`points_2`** (output_control)  integer-array `→` Sequence[int]

Indices of matched input points in image 2.

## Possible Predecessors

`points_foerstner`,
`points_harris`

## Possible Successors

`vector_to_essential_matrix`

## See also

`match_fundamental_matrix_ransac`,
`match_rel_pose_ransac`,
`stationary_camera_self_calibration`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

3D Metrology
