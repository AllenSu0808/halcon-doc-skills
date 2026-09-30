# vector_to_proj_hom_mat2d_distortion (Operator)

## Name

`vector_to_proj_hom_mat2d_distortion` — Compute a projective transformation matrix and the radial distortion
coefficient using given image point correspondences.

## Signature

`def vector_to_proj_hom_mat2d_distortion(points_1row: Sequence[Union[float, int]], points_1col: Sequence[Union[float, int]], points_2row: Sequence[Union[float, int]], points_2col: Sequence[Union[float, int]], cov_rr1: Sequence[Union[float, int]], cov_rc1: Sequence[Union[float, int]], cov_cc1: Sequence[Union[float, int]], cov_rr2: Sequence[Union[float, int]], cov_rc2: Sequence[Union[float, int]], cov_cc2: Sequence[Union[float, int]], image_width: int, image_height: int, method: str) -> Tuple[Sequence[float], float, float]`

## Description

`vector_to_proj_hom_mat2d_distortion` determines the
projective transformation matrix *`hom_mat_2d`* and the radial
distortion coefficient *`kappa`*$(\kappa)$ from given
point correspondences (*`points_1row`*,*`points_1col`*),
(*`points_2row`*,*`points_2col`*) that optimally fulfill the
following equation:
$$\left(\begin{array}{c} r_{2} \\ c_{2} \\ 1 \end{array}\right) = \mathrm{HomMat2D} \cdot \left(\begin{array}{c} r_{1} \\ c_{1} \\ 1 \end{array}\right) \.$$ ![figure](../assets/c7511ca06df7f92b.svg)
Here, $(r_{1},c_{1})$ and $(r_{2},c_{2})$
denote image points that are obtained by undistorting the input
image points with the division model (see
[Calibration](toc_calibration.md)):
$$r = \frac{\tilde{r}}{1 + \kappa(\tilde{r}^2 + \tilde{c}^2)} c = \frac{\tilde{c}}{1 + \kappa(\tilde{r}^2 + \tilde{c}^2)}$$ ![figure](../assets/6ff1b1bb1ed9db6b.svg)
Here,
$(\tilde{r}_1,\tilde{c}_1) = (Points1Row - 0.5(ImageHeight - 1), Points1Col - 0.5(ImageWidth - 1))$ ![figure](../assets/70b5c2021cb0cc5a.svg)
and
$\left(r_{2},\tilde{c}_{2}\right) = \left(Points2Row - 0.5(ImageHeight - 1), Points2Col - 0.5(ImageWidth - 1)\right)$ ![figure](../assets/df87068ead585bc8.svg)
denote the distorted image points, specified relative to the image center.
Thus, `vector_to_proj_hom_mat2d_distortion` assumes that the
principal point of the camera, i.e., the center of the radial
distortions, lies at the center of the image. Note that the images
from which the points (*`points_1row`*,*`points_1col`*) and
(*`points_2row`*,*`points_2col`*) are extracted have to be
obtained with the same camera.

The returned *`kappa`* can be used to construct camera
parameters that can be used to rectify images or points (see
[`change_radial_distortion_cam_par`](change_radial_distortion_cam_par.md),
[`change_radial_distortion_image`](change_radial_distortion_image.md), and
[`change_radial_distortion_points`](change_radial_distortion_points.md)):
$$CamPar = [\'area_scan_telecentric_division\',1.0,Kappa,1.0,1.0,0.5(ImageWidth - 1),0.5(ImageHeight - 1),ImageWidth,ImageHeight]$$ ![figure](../assets/5371a5a65306c74a.svg)

The minimum number of required point correspondences is five.
`vector_to_proj_hom_mat2d_distortion` seeks to minimize the
transformation error between the point correspondences based on the
above equations. To achieve such a minimization, two different
algorithms are available. The algorithm to use can be chosen using
the parameter *`method`*. For *`method`* =
*"linear"*, a linear algorithm that minimizes an algebraic
error based on the above equations is used. This algorithm is very
fast and returns accurate results for small to moderate noise of the
point coordinates and for most distortions (except for small
distortions). For *`method`* = *"gold_standard"*, a
mathematically optimal but slower optimization is used, which
minimizes the geometric reprojection error. In general, it is
preferable to use *`method`* = *"gold_standard"*.

If *"gold_standard"* is used, the covariances of the image
points (*`cov_rr1`*, *`cov_rc1`*, *`cov_cc1`*,
*`cov_rr2`*, *`cov_rc2`*, *`cov_cc2`*) can be
incorporated into the computation. They can be provided, for
example, by the operator [`points_foerstner`](points_foerstner.md). If the point
covariances are unknown, which is the default, empty tuples are
passed. In this case, the optimization algorithm internally assumes
uniform and equal covariances for all points. If *"linear"*
is used, the covariances are ignored and the covariance parameters
can be left empty.

The value *`error`* indicates the overall quality of the
optimization procedure and is the mean symmetric euclidean distance
in pixels between the points and their corresponding transformed
points.

If the correspondence between the points has not been determined,
[`proj_match_points_distortion_ransac`](proj_match_points_distortion_ransac.md) or
[`proj_match_points_distortion_ransac_guided`](proj_match_points_distortion_ransac_guided.md) should be used to
determine the correspondence as well as the transformation.

## Attention

It should be noted that if a homogeneous transformation matrix is
used to transform images, regions, XLD contours, or any other data
that has been extracted from images, it is assumed that the origin
of the coordinate system of the homogeneous transformation matrix
lies in the upper left corner of a pixel. The image processing
operators that return point coordinates, however, assume a
coordinate system in which the origin lies in the center of a pixel.
Therefore, to obtain a consistent homogeneous transformation matrix,
0.5 must be added to the point coordinates before computing the
transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`points_1row`** (input_control)  point.y-array `→` Sequence[Union[float, int]]

Input points in image 1 (row coordinate).

Restriction:
`length(Points1Row) >= 5`

**`points_1col`** (input_control)  point.x-array `→` Sequence[Union[float, int]]

Input points in image 1 (column coordinate).

Restriction:
`length(Points1Col) == length(Points1Row)`

**`points_2row`** (input_control)  point.y-array `→` Sequence[Union[float, int]]

Input points in image 2 (row coordinate).

Restriction:
`length(Points2Row) == length(Points1Row)`

**`points_2col`** (input_control)  point.x-array `→` Sequence[Union[float, int]]

Input points in image 2 (column coordinate).

Restriction:
`length(Points2Col) == length(Points1Row)`

**`cov_rr1`** (input_control)  number-array `→` Sequence[Union[float, int]]

Row coordinate variance of the points in image 1.

Default:
[]

**`cov_rc1`** (input_control)  number-array `→` Sequence[Union[float, int]]

Covariance of the points in image 1.

Default:
[]

**`cov_cc1`** (input_control)  number-array `→` Sequence[Union[float, int]]

Column coordinate variance of the points in image 1.

Default:
[]

**`cov_rr2`** (input_control)  number-array `→` Sequence[Union[float, int]]

Row coordinate variance of the points in image 2.

Default:
[]

**`cov_rc2`** (input_control)  number-array `→` Sequence[Union[float, int]]

Covariance of the points in image 2.

Default:
[]

**`cov_cc2`** (input_control)  number-array `→` Sequence[Union[float, int]]

Column coordinate variance of the points in image 2.

Default:
[]

**`image_width`** (input_control)  integer `→` int

Width of the images from which the points were
extracted.

Restriction:
`ImageWidth > 0`

**`image_height`** (input_control)  integer `→` int

Height of the images from which the points were
extracted.

Restriction:
`ImageHeight > 0`

**`method`** (input_control)  string `→` str

Estimation algorithm.

Default:
"gold_standard"

List of values:
"gold_standard", "linear"

**`hom_mat_2d`** (output_control)  hom_mat2d `→` Sequence[float]

Homogeneous projective transformation matrix.

**`kappa`** (output_control)  real `→` float

Computed radial distortion coefficient.

**`error`** (output_control)  real `→` float

Root-Mean-Square transformation error.

## Possible Predecessors

`proj_match_points_distortion_ransac`,
`proj_match_points_distortion_ransac_guided`,
`points_foerstner`,
`points_harris`

## Possible Successors

`change_radial_distortion_cam_par`,
`change_radial_distortion_image`,
`change_radial_distortion_points`,
`projective_trans_image`,
`projective_trans_image_size`,
`projective_trans_region`,
`projective_trans_contour_xld`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## Alternatives

`vector_to_proj_hom_mat2d`,
`hom_vector_to_proj_hom_mat2d`

## See also

`calibrate_cameras`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Calibration
