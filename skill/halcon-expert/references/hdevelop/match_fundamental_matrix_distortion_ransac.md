# match_fundamental_matrix_distortion_ransac (Operator)

## Name

`match_fundamental_matrix_distortion_ransac` — Compute the fundamental matrix and the radial distortion coefficient
for a pair of stereo images by automatically finding correspondences
between image points.

## Signature

`match_fundamental_matrix_distortion_ransac(Image1, Image2 : : Rows1, Cols1, Rows2, Cols2, GrayMatchMethod, MaskSize, RowMove, ColMove, RowTolerance, ColTolerance, Rotation, MatchThreshold, EstimationMethod, DistanceThreshold, RandSeed : FMatrix, Kappa, Error, Points1, Points2)`

## Description

Given a set of coordinates of characteristic points
(*`Rows1`*,*`Cols1`*) and
(*`Rows2`*,*`Cols2`*) in the stereo images
*`Image1`* and *`Image2`*, which must be of identical
size, `match_fundamental_matrix_distortion_ransac`
automatically finds the correspondences between the characteristic
points and determines the geometry of the stereo setup. For unknown
cameras the geometry of the stereo setup is represented by the
fundamental matrix *`FMatrix`* and the radial distortion
coefficient *`Kappa`*$(\kappa)$. All corresponding points
must fulfill the epipolar constraint:
$$\left(\begin{array}{c} c_{2} \\ r_{2} \\ 1 \end{array}\right)^{\top} \cdot \mathrm{FMatrix} \cdot \left(\begin{array}{c} c_{1} \\ r_{1} \\ 1 \end{array}\right) = 0$$ ![figure](../assets/d16d0e58047ac6d1.svg)
Here, $(r_{1},c_{1})$ and $(r_{2},c_{2})$
denote image points that are obtained by undistorting the input
image points with the division model (see
[Calibration](toc_calibration.md)):
$$r = \frac{\tilde{r}}{1 + \kappa(\tilde{r}^2 + \tilde{c}^2)} c = \frac{\tilde{c}}{1 + \kappa(\tilde{r}^2 + \tilde{c}^2)}$$ ![figure](../assets/6ff1b1bb1ed9db6b.svg)
Here,
$(\tilde{r}_1, \tilde{c}_1) = (Rows1 - 0.5(h - 1), Cols1 - 0.5(w - 1))$ ![figure](../assets/d2fcb4cda5ac5181.svg)
and
$(\tilde{r}_{2}, \tilde{c}_{2}) = (Rows2 - 0.5(h - 1), Cols2 - 0.5(w - 1))$ ![figure](../assets/6b550dd0ce20a38d.svg)
denote the distorted image points, specified relative to the image center,
and w and h denote the width and height of the input images.
Thus, `match_fundamental_matrix_distortion_ransac` assumes that the
principal point of the camera, i.e., the center of the radial
distortions, lies at the center of the image.

The returned *`Kappa`* can be used to construct camera
parameters that can be used to rectify images or points (see
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md),
[`change_radial_distortion_image`](change_radial_distortion_image.md), and
[`change_radial_distortion_points`](change_radial_distortion_points.md)):
$$CamPar = [\'area_scan_telecentric_division\',0.0,Kappa,1.0,1.0,0.5(w-1),0.5(h-1),w,h]$$ ![figure](../assets/5fa3b91cde84ff8c.svg)

Note the column/row ordering in the point coordinates above: since
the fundamental matrix encodes the projective relation between two
stereo images embedded in 3D space, the x/y notation must be
compliant with the camera coordinate system. Therefore, (x,y)
coordinates correspond to (column,row) pairs.

The matching process is based on characteristic points, which can be
extracted with point operators like [`points_foerstner`](points_foerstner.md) or
[`points_harris`](points_harris.md). The matching itself is carried out in two
steps: first, gray value correlations of mask windows around the
input points in the first and the second image are determined and an
initial matching between them is generated using the similarity of
the windows in both images. Then, the RANSAC algorithm is applied
to find the fundamental matrix and radial distortion coefficient
that maximizes the number of correspondences under the epipolar
constraint.

The size of the mask windows used for the matching is
*`MaskSize`* x
*`MaskSize`*. Three metrics for the correlation can be
selected. If *`GrayMatchMethod`* has the value *'ssd'*,
the sum of the squared gray value differences is used,
*'sad'* means the sum of absolute differences, and
*'ncc'* is the normalized cross correlation. For details
please refer to [`binocular_disparity`](binocular_disparity.md). The metric is
minimized (*'ssd'*, *'sad'*) or maximized
(*'ncc'*) over all possible point pairs. A matching thus
found is only accepted if the value of the metric is below the value
of *`MatchThreshold`* (*'ssd'*, *'sad'*) or above
that value (*'ncc'*).

To increase the speed of the algorithm the search area for the match
candidates can be limited to a rectangle by specifying its size and
offset. Only points within a window of $2\cdot\texttt{RowTolerance}\times2\cdot\texttt{ColTolerance}$ points are considered. The offset of the
center of the search window in the second image with respect to the
position of the current point in the first image is given by
*`RowMove`* and *`ColMove`*.

If the second camera is rotated around the optical axis with respect
to the first camera, the parameter *`Rotation`* may contain an
estimate for the rotation angle or an angle interval in radians. A
good guess will increase the quality of the gray value matching. If
the actual rotation differs too much from the specified estimate,
the matching will typically fail. In this case, an angle interval
should be specified and *`Rotation`* is a tuple with two
elements. The larger the given interval is the slower is the
operator is since the RANSAC algorithm is run over all
(automatically determined) angle increments within the interval.

After the initial matching has been completed, a randomized search
algorithm (RANSAC) is used to determine the fundamental matrix
*`FMatrix`* and the radial distortion coefficient
*`Kappa`*. It tries to find the parameters that are consistent
with a maximum number of correspondences. For a point to be
accepted, the distance in pixels to its corresponding epipolar line
must not exceed the threshold *`DistanceThreshold`*.

The parameter *`EstimationMethod`* decides whether the relative
orientation between the cameras is of a special type and which
algorithm is to be applied for its computation. If
*`EstimationMethod`* is either *'linear'* or
*'gold_standard'*, the relative orientation is arbitrary. If
the left and right cameras are identical and the relative
orientation between them is a pure translation,
*`EstimationMethod`* can be set to *'trans_linear'* or
*'trans_gold_standard'*. The typical application for this
special motion case is the scenario of a single fixed camera looking
onto a moving conveyor belt. In order to get a unique solution for
the correspondence problem, the minimum required number of
corresponding points is nine in the general case and four in the
special translational case.

The fundamental matrix is computed by a linear algorithm if
*`EstimationMethod`* is set to *'linear'* or
*'trans_linear'*. This algorithm is very fast. For the pure
translation case (*`EstimationMethod`* =
*'trans_linear'*), the linear method returns accurate results
for small to moderate noise of the point coordinates and for most
distortions (except for very small distortions). For a general
relative orientation of the two cameras (*`EstimationMethod`*
= *'linear'*), the linear method only returns accurate
results for very small noise of the point coordinates and for
sufficiently large distortions. For *`EstimationMethod`* =
*'gold_standard'* or *'trans_gold_standard'*, a
mathematically optimal but slower optimization is used, which
minimizes the geometric reprojection error of reconstructed
projective 3D points. For a general relative orientation of the two
cameras, in general *`EstimationMethod`* =
*'gold_standard'* should be selected.

The value *`Error`* indicates the overall quality of the
estimation procedure and is the mean symmetric Euclidean distance in
pixels between the points and their corresponding epipolar lines.

Point pairs consistent with the above constraints are considered to
be corresponding points. *`Points1`* contains the indices of
the matched input points from the first image and *`Points2`*
contains the indices of the corresponding points in the second
image.

The parameter *`RandSeed`* can be used to control the
randomized nature of the RANSAC algorithm, and hence to obtain
reproducible results. If *`RandSeed`* is set to a positive
number, the operator returns the same result on every call with the
same parameters because the internally used random number generator
is initialized with *`RandSeed`*. If *`RandSeed`* =
*0*, the random number generator is initialized with the
current time. In this case the results may not be reproducible.
The value set for the HALCON system variable *'seed_rand'*
(see [`set_system`](set_system.md)) does not affect the results of
`match_fundamental_matrix_distortion_ransac`.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Image1`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image 1.

**`Image2`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image 2.

**`Rows1`** (input_control)  point.y-array `→`  (real / integer)

Input points in image 1 (row coordinate).

Restriction:
`length(Rows1) >= 9 || length(Rows1) >= 4`

**`Cols1`** (input_control)  point.x-array `→`  (real / integer)

Input points in image 1 (column coordinate).

Restriction:
`length(Cols1) == length(Rows1)`

**`Rows2`** (input_control)  point.y-array `→`  (real / integer)

Input points in image 2 (row coordinate).

Restriction:
`length(Rows2) >= 9 || length(Rows2) >= 4`

**`Cols2`** (input_control)  point.x-array `→`  (real / integer)

Input points in image 2 (column coordinate).

Restriction:
`length(Cols2) == length(Rows2)`

**`GrayMatchMethod`** (input_control)  string `→`  (string)

Gray value match metric.

Default:
'ncc'

List of values:
'ncc', 'sad', 'ssd'

**`MaskSize`** (input_control)  integer `→`  (integer)

Size of gray value masks.

Default:
10

Suggested values:
3, 7, 15

Value range:
`1
≤
MaskSize`

**`RowMove`** (input_control)  integer `→`  (integer)

Average row coordinate offset of corresponding points.

Default:
0

**`ColMove`** (input_control)  integer `→`  (integer)

Average column coordinate offset of corresponding points.

Default:
0

**`RowTolerance`** (input_control)  integer `→`  (integer)

Half height of matching search window.

Default:
200

Restriction:
`RowTolerance >= 1`

**`ColTolerance`** (input_control)  integer `→`  (integer)

Half width of matching search window.

Default:
200

Restriction:
`ColTolerance >= 1`

**`Rotation`** (input_control)  angle.rad(-array) `→`  (real / integer)

Estimate of the relative rotation of the second image
with respect to the first image.

Default:
0.0

Suggested values:
0.0, 0.1, -0.1, 0.7854, 1.571, 3.142

**`MatchThreshold`** (input_control)  number `→`  (integer / real)

Threshold for gray value matching.

Default:
0.7

Suggested values:
0.9, 0.7, 0.5, 10, 20, 50, 100

**`EstimationMethod`** (input_control)  string `→`  (string)

Algorithm for the computation of the fundamental
matrix and for special camera orientations.

Default:
'gold_standard'

List of values:
'gold_standard', 'linear', 'trans_gold_standard', 'trans_linear'

**`DistanceThreshold`** (input_control)  number `→`  (real / integer)

Maximal deviation of a point from its epipolar line.

Default:
1

Restriction:
`DistanceThreshold > 0`

**`RandSeed`** (input_control)  integer `→`  (integer)

Seed for the random number generator.

Default:
0

**`FMatrix`** (output_control)  hom_mat2d `→`  (real)

Computed fundamental matrix.

**`Kappa`** (output_control)  real `→`  (real)

Computed radial distortion coefficient.

**`Error`** (output_control)  real `→`  (real)

Root-Mean-Square epipolar distance error.

**`Points1`** (output_control)  integer-array `→`  (integer)

Indices of matched input points in image 1.

**`Points2`** (output_control)  integer-array `→`  (integer)

Indices of matched input points in image 2.

## Example (HDevelop)

```
points_foerstner (Image1, 1, 2, 3, 200, 0.1, 'gauss', 'true', \
                  Rows1, Cols1, _, _, _, _, _, _, _, _)
points_foerstner (Image2, 1, 2, 3, 200, 0.1, 'gauss', 'true', \
                  Rows2, Cols2, _, _, _, _, _, _, _, _)
match_fundamental_matrix_distortion_ransac (Image1, Image2, \
                                            Rows1, Cols1, Rows2, \
                                            Cols2, 'ncc', 10, 0, 0, \
                                            100, 200, 0, 0.5, \
                                            'trans_gold_standard', \
                                            1, 42, FMatrix, Kappa, \
                                            Error, Points1, Points2)
get_image_size (Image1, Width, Height)
CamParDist := ['area_scan_division',0.0,Kappa,1.0,1.0,\
               0.5*(Width-1),0.5*Height-1,Width,Height]
change_radial_distortion_cam_par ('fixed', CamParDist, 0, CamPar)
change_radial_distortion_image (Image1, Image1, Image1Rect, \
                                CamParDist, CamPar)
change_radial_distortion_image (Image2, Image2, Image2Rect, \
                                CamParDist, CamPar)
gen_binocular_proj_rectification (Map1, Map2, FMatrix, [], Width, \
                                  Height, Width, Height, 1, \
                                  'bilinear_map', _, H1, H2)
map_image (Image1Rect, Map1, Image1Mapped)
map_image (Image2Rect, Map2, Image2Mapped)
binocular_disparity_mg (Image1Mapped, Image2Mapped, Disparity, \
                        Score, 1, 30, 8, 0, 'false', \
                        'default_parameters', 'fast_accurate')
```

## Possible Predecessors

`points_foerstner`,
`points_harris`

## Possible Successors

`vector_to_fundamental_matrix_distortion`,
`change_radial_distortion_cam_par`,
`change_radial_distortion_image`,
`change_radial_distortion_points`,
`gen_binocular_proj_rectification`

## See also

`match_fundamental_matrix_ransac`,
`match_essential_matrix_ransac`,
`match_rel_pose_ransac`,
`proj_match_points_ransac`,
`calibrate_cameras`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

3D Metrology
