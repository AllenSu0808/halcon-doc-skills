# VectorToFundamentalMatrixDistortion (Operator)

## Name

`VectorToFundamentalMatrixDistortion` — Compute the fundamental matrix and the radial distortion coefficient
given a set of image point correspondences and reconstruct 3D
points.

## Signature

`static void HOperatorSet.VectorToFundamentalMatrixDistortion(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HTuple imageWidth, HTuple imageHeight, HTuple method, out HTuple FMatrix, out HTuple kappa, out HTuple error, out HTuple x, out HTuple y, out HTuple z, out HTuple w)`

`double HHomMat2D.VectorToFundamentalMatrixDistortion(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, int imageWidth, int imageHeight, string method, out double error, out HTuple x, out HTuple y, out HTuple z, out HTuple w)`

## Description

For a stereo configuration with unknown camera parameters, the
geometric relation between the two images is defined by the
fundamental matrix. `VectorToFundamentalMatrixDistortion`
determines the fundamental matrix *`FMatrix`* and the radial
distortion coefficient *`kappa`*$(\kappa)$ from given
point correspondences (*`rows1`*,*`cols1`*),
(*`rows2`*,*`cols2`*) that fulfill the epipolar
constraint:
$$\left(\begin{array}{c} c_{2} \\ r_{2} \\ 1 \end{array}\right)^{\top} \cdot \mathrm{FMatrix} \cdot \left(\begin{array}{c} c_{1} \\ r_{1} \\ 1 \end{array}\right) = 0$$ ![figure](../assets/d16d0e58047ac6d1.svg)
Here, $(r_{1},c_{1})$ and $(r_{2},c_{2})$
denote image points that are obtained by undistorting the input
image points with the division model (see
[Calibration](toc_calibration.md)):
$$r = \frac{\tilde{r}}{1 + \kappa(\tilde{r}^2 + \tilde{c}^2)} c = \frac{\tilde{c}}{1 + \kappa(\tilde{r}^2 + \tilde{c}^2)}$$ ![figure](../assets/6ff1b1bb1ed9db6b.svg)
Here,
$(\tilde r_1, \tilde c_1) = (Rows1 - 0.5(ImageHeight - 1), Cols1 - 0.5(ImageWidth - 1))$ ![figure](../assets/2df7be9deefcf894.svg)
and
$(\tilde r_2, \tilde c_2) = (Rows2 - 0.5(ImageHeight - 1), Cols2 - 0.5(ImageWidth - 1))$ ![figure](../assets/33b4e82cfa6f0250.svg)
denote the distorted image points, specified relative to the image center.
Thus, `VectorToFundamentalMatrixDistortion` assumes that the
principal point of the camera, i.e., the center of the radial
distortions, lies at the center of the image.

The returned *`kappa`* can be used to construct camera
parameters that can be used to rectify images or points (see
[`ChangeRadialDistortionCamPar`](change_radial_distortion_cam_par.md),
[`ChangeRadialDistortionImage`](change_radial_distortion_image.md), and
[`ChangeRadialDistortionPoints`](change_radial_distortion_points.md)):
$$CamPar = [\'area_scan_telecentric_division\',0.0,Kappa,1.0,1.0,0.5(ImageWidth-1),0.5(ImageHeight-1),ImageWidth,ImageHeight]$$ ![figure](../assets/6efabfa8a5a09982.svg)

Note the column/row ordering in the point coordinates above: since
the fundamental matrix encodes the projective relation between two
stereo images embedded in 3D space, the x/y notation must be
compliant with the camera coordinate system. Therefore, (x,y)
coordinates correspond to (column,row) pairs.

For a general relative orientation of the two cameras, the minimum
number of required point correspondences is nine. Then,
*`method`* must be set to *"linear"* or
*"gold_standard"*. If the left and right cameras are
identical and the relative orientation between them is a pure
translation, *`method`* must be set to *"trans_linear"*
or *"trans_gold_standard"*. In this special case, the
minimum number of correspondences is only four. The typical
application of the motion being a pure translation is a single fixed
camera looking onto a moving conveyor belt.

The fundamental matrix is determined by minimizing a cost function.
To minimize the respective error, different algorithms are
available, and the user can choose between the linear
(*"linear"*) and the gold-standard algorithm
(*"gold_standard"*). Like the motion type, the algorithm can
be selected with the parameter *`method`*. For *`method`*
= *"linear"* or *"trans_linear"*, a linear algorithm
that minimizes an algebraic error based on the above epipolar
constraint is used. This algorithm is very fast. For the pure
translation case (*`method`* = *"trans_linear"*), the
linear method returns accurate results for small to moderate noise
of the point coordinates and for most distortions (except for very
small distortions). For a general relative orientation of the two
cameras (*`method`* = *"linear"*), the linear method
only returns accurate results for very small noise of the point
coordinates and for sufficiently large distortions. For
*`method`* = *"gold_standard"* or
*"trans_gold_standard"*, a mathematically optimal but slower
optimization is used, which minimizes the geometric reprojection
error of reconstructed projective 3D points. In this case, in
addition to the fundamental matrix and the distortion coefficient,
the projective coordinates
(*`x`*,*`y`*,*`z`*,*`w`*) of the reconstructed
points are returned. For a general relative orientation of the two
cameras, in general *`method`* = *"gold_standard"*
should be selected.

If an optimal gold-standard algorithm is chosen, the covariances of
the image points (*`covRR1`*, *`covRC1`*, *`covCC1`*,
*`covRR2`*, *`covRC2`*, *`covCC2`*) can be
incorporated into the computation. They can be provided, for
example, by the operator [`PointsFoerstner`](points_foerstner.md). If the point
covariances are unknown, which is the default, empty tuples are
passed. In this case, the optimization algorithm internally assumes
uniform and equal covariances for all points.

The value *`error`* indicates the overall quality of the
optimization procedure and is the mean symmetric Euclidean distance
in pixels between the points and their corresponding epipolar lines.

If the correspondence between the points is not known,
[`MatchFundamentalMatrixDistortionRansac`](match_fundamental_matrix_distortion_ransac.md) should be used
instead.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rows1`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (row coordinate).

Restriction:
`length(Rows1) >= 9 || length(Rows1) >= 4`

**`cols1`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (column coordinate).

Restriction:
`length(Cols1) == length(Rows1)`

**`rows2`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (row coordinate).

Restriction:
`length(Rows2) == length(Rows1)`

**`cols2`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

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
"gold_standard", "linear", "trans_gold_standard", "trans_linear"

**`FMatrix`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Computed fundamental matrix.

**`kappa`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Computed radial distortion coefficient.

**`error`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Root-Mean-Square epipolar distance error.

**`x`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the reconstructed points in projective
3D space.

**`y`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the reconstructed points in projective
3D space.

**`z`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the reconstructed points in projective
3D space.

**`w`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

W coordinates of the reconstructed points in projective
3D space.

## Possible Predecessors

`MatchFundamentalMatrixDistortionRansac`

## Possible Successors

`ChangeRadialDistortionCamPar`,
`ChangeRadialDistortionImage`,
`ChangeRadialDistortionPoints`,
`GenBinocularProjRectification`

## Alternatives

`VectorToFundamentalMatrix`,
`VectorToEssentialMatrix`,
`VectorToRelPose`

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

3D Metrology
