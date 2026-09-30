# VectorToProjHomMat2dDistortion (Operator)

## Name

`VectorToProjHomMat2dDistortion` — Compute a projective transformation matrix and the radial distortion
coefficient using given image point correspondences.

## Signature

`static void HOperatorSet.VectorToProjHomMat2dDistortion(HTuple points1Row, HTuple points1Col, HTuple points2Row, HTuple points2Col, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HTuple imageWidth, HTuple imageHeight, HTuple method, out HTuple homMat2D, out HTuple kappa, out HTuple error)`

`double HHomMat2D.VectorToProjHomMat2dDistortion(HTuple points1Row, HTuple points1Col, HTuple points2Row, HTuple points2Col, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, int imageWidth, int imageHeight, string method, out double error)`

## Description

`VectorToProjHomMat2dDistortion` determines the
projective transformation matrix *`homMat2D`* and the radial
distortion coefficient *`kappa`*$(\kappa)$ from given
point correspondences (*`points1Row`*,*`points1Col`*),
(*`points2Row`*,*`points2Col`*) that optimally fulfill the
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
Thus, `VectorToProjHomMat2dDistortion` assumes that the
principal point of the camera, i.e., the center of the radial
distortions, lies at the center of the image. Note that the images
from which the points (*`points1Row`*,*`points1Col`*) and
(*`points2Row`*,*`points2Col`*) are extracted have to be
obtained with the same camera.

The returned *`kappa`* can be used to construct camera
parameters that can be used to rectify images or points (see
[`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md),
[`ChangeRadialDistortionImage`](change_radial_distortion_image.md), and
[`ChangeRadialDistortionPoints`](change_radial_distortion_points.md)):
$$CamPar = [\'area_scan_telecentric_division\',1.0,Kappa,1.0,1.0,0.5(ImageWidth - 1),0.5(ImageHeight - 1),ImageWidth,ImageHeight]$$ ![figure](../assets/5371a5a65306c74a.svg)

The minimum number of required point correspondences is five.
`VectorToProjHomMat2dDistortion` seeks to minimize the
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
points (*`covRR1`*, *`covRC1`*, *`covCC1`*,
*`covRR2`*, *`covRC2`*, *`covCC2`*) can be
incorporated into the computation. They can be provided, for
example, by the operator [`PointsFoerstner`](points_foerstner.md). If the point
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
[`ProjMatchPointsDistortionRansac`](proj_match_points_distortion_ransac.md) or
[`ProjMatchPointsDistortionRansacGuided`](proj_match_points_distortion_ransac_guided.md) should be used to
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

**`points1Row`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (row coordinate).

Restriction:
`length(Points1Row) >= 5`

**`points1Col`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (column coordinate).

Restriction:
`length(Points1Col) == length(Points1Row)`

**`points2Row`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (row coordinate).

Restriction:
`length(Points2Row) == length(Points1Row)`

**`points2Col`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (column coordinate).

Restriction:
`length(Points2Col) == length(Points1Row)`

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

**`imageWidth`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Width of the images from which the points were
extracted.

Restriction:
`ImageWidth > 0`

**`imageHeight`** (input_control)  integer `→` [HTuple](HTuple.md) (*int* / long)

Height of the images from which the points were
extracted.

Restriction:
`ImageHeight > 0`

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Estimation algorithm.

Default:
"gold_standard"

List of values:
"gold_standard", "linear"

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

**`kappa`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Computed radial distortion coefficient.

**`error`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Root-Mean-Square transformation error.

## Possible Predecessors

`ProjMatchPointsDistortionRansac`,
`ProjMatchPointsDistortionRansacGuided`,
`PointsFoerstner`,
`PointsHarris`

## Possible Successors

`ChangeRadialDistortionCamPar`,
`ChangeRadialDistortionImage`,
`ChangeRadialDistortionPoints`,
`ProjectiveTransImage`,
`ProjectiveTransImageSize`,
`ProjectiveTransRegion`,
`ProjectiveTransContourXld`,
`ProjectiveTransPoint2d`,
`ProjectiveTransPixel`

## Alternatives

`VectorToProjHomMat2d`,
`HomVectorToProjHomMat2d`

## See also

`CalibrateCameras`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Calibration
