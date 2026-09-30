# vector_to_essential_matrix (Operator)

## Name

`vector_to_essential_matrix` — Compute the essential matrix given image point correspondences
and known camera matrices and reconstruct 3D points.

## Signature

`vector_to_essential_matrix( : : Rows1, Cols1, Rows2, Cols2, CovRR1, CovRC1, CovCC1, CovRR2, CovRC2, CovCC2, CamMat1, CamMat2, Method : EMatrix, CovEMat, Error, X, Y, Z, CovXYZ)`

## Description

For a stereo configuration with known camera matrices the geometric relation
between the two images is defined by the essential matrix.
The operator `vector_to_essential_matrix` determines the essential
matrix *`EMatrix`* from in general at least six given point
correspondences, that fulfill the epipolar constraint:

$$\left(\begin{array}{c}X_{2}\\Y_{2}\\1\end{array}\right)^{\mathrm{T}} \,·\, EMatrix \,· \,\left(\begin{array}{c}X_{1}\\Y_{1}\\1\end{array}\right) \,=\, 0$$ ![figure](../assets/aee5fd9d63f6e4b8.svg)

The operator `vector_to_essential_matrix` is designed to deal
only with a linear camera model. This is in contrast to the
operator [`vector_to_rel_pose`](vector_to_rel_pose.md), that encompasses lens distortions too.
The internal camera parameters are passed by the arguments
*`CamMat1`* and *`CamMat2`*, which are
3x3 upper triangular matrices describing an affine
transformation. The relation between the vector (X,Y,1), defining the
direction from the camera to the viewed 3D point, and its (projective)
2D image coordinates (col,row,1) is:

$$\begin{pmatrix} col \\ row \\ 1 \end{pmatrix} = CamMat \cdot \begin{pmatrix} X \\ Y \\ 1 \end{pmatrix} \quad \text{where} \quad CamMat = \begin{pmatrix} f/s_x & s & c_x \\ 0 & f/s_y & c_y \\ 0 & 0 & 1 \end{pmatrix}.$$ ![figure](../assets/c8408b13b84e9903.svg)
The focal length is denoted by f, $s_{x},s_{y}$
are scaling
factors, s describes a skew factor and $(c_{x},c_{y})$
indicates the principal point.
Mainly, these are the elements known from the camera parameters as used for
example in [`calibrate_cameras`](calibrate_cameras.md). Alternatively, the elements
of the camera matrix can be described in a different way, see e.g.
[`stationary_camera_self_calibration`](stationary_camera_self_calibration.md).

The point correspondences
(*`Rows1`*,*`Cols1`*) and (*`Rows2`*,*`Cols2`*)
are typically found by applying the operator
[`match_essential_matrix_ransac`](match_essential_matrix_ransac.md). Multiplying the image
coordinates by the inverse of the camera matrices results in the 3D
direction vectors, which can then be inserted in the epipolar constraint.

The parameter *`Method`* decides whether the relative orientation
between the cameras is of a special type and which algorithm is to be applied
for its computation.
If *`Method`* is either *'normalized_dlt'* or
*'gold_standard'* the relative orientation is arbitrary.
Choosing *'trans_normalized_dlt'* or *'trans_gold_standard'*
means that the relative motion between the cameras is a pure translation.
The typical application for this special motion case is the
scenario of a single fixed camera looking onto a moving conveyor belt.
In this case the minimum required number of corresponding points is just two
instead of six in the general case.

The essential matrix is computed by a linear algorithm if
*'normalized_dlt'* or *'trans_normalized_dlt'* is chosen.
With *'gold_standard'* or *'trans_gold_standard'*
the algorithm gives a statistically optimal result.
Here, *'normalized_dlt'* and *'gold_standard'* stand for
direct-linear-transformation and gold-standard-algorithm respectively.
All methods return the coordinates (*`X`*,*`Y`*,*`Z`*)
of the reconstructed 3D points. The optimal methods also return
the covariances of the 3D points in *`CovXYZ`*.
Let n be the number of points
then the 3x3 covariance matrices are concatenated and
stored in a tuple of length 9n.
Additionally, the optimal methods return the
covariance of the essential matrix *`CovEMat`*.

If an optimal gold-standard-algorithm is chosen the covariances of the image
points (*`CovRR1`*, *`CovRC1`*, *`CovCC1`*, *`CovRR2`*,
*`CovRC2`*, *`CovCC2`*) can be incorporated in the computation.
They can be provided for example by the operator [`points_foerstner`](points_foerstner.md).
If the point covariances are unknown, which is the default, empty tuples
are input. In this case the optimization algorithm internally assumes
uniform and equal covariances for all points.

The value *`Error`* indicates the overall quality of the optimization
process and is the root-mean-square Euclidean distance in pixels between the
points and their corresponding epipolar lines.

For the operator `vector_to_essential_matrix` a special configuration
of scene points and cameras exists: if all 3D points lie in a single plane
and additionally are all closer to one of the two cameras then the solution
in the essential matrix is not unique but twofold.
As a consequence both solutions are computed and returned by the operator.
This means that all output parameters are of double length and the values
of the second solution are simply concatenated behind the values of the
first one.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Rows1`** (input_control)  number-array `→`  (real / integer)

Input points in image 1 (row coordinate).

Restriction:
`length(Rows1) >= 6 || length(Rows1) >= 2`

**`Cols1`** (input_control)  number-array `→`  (real / integer)

Input points in image 1 (column coordinate).

Restriction:
`length(Cols1) == length(Rows1)`

**`Rows2`** (input_control)  number-array `→`  (real / integer)

Input points in image 2 (row coordinate).

Restriction:
`length(Rows2) == length(Rows1)`

**`Cols2`** (input_control)  number-array `→`  (real / integer)

Input points in image 2 (column coordinate).

Restriction:
`length(Cols2) == length(Rows1)`

**`CovRR1`** (input_control)  number-array `→`  (real / integer)

Row coordinate variance of the points in image 1.

Default:
[]

**`CovRC1`** (input_control)  number-array `→`  (real / integer)

Covariance of the points in image 1.

Default:
[]

**`CovCC1`** (input_control)  number-array `→`  (real / integer)

Column coordinate variance of the points in image 1.

Default:
[]

**`CovRR2`** (input_control)  number-array `→`  (real / integer)

Row coordinate variance of the points in image 2.

Default:
[]

**`CovRC2`** (input_control)  number-array `→`  (real / integer)

Covariance of the points in image 2.

Default:
[]

**`CovCC2`** (input_control)  number-array `→`  (real / integer)

Column coordinate variance of the points in image 2.

Default:
[]

**`CamMat1`** (input_control)  hom_mat2d `→`  (real / integer)

Camera matrix of the 1st camera.

**`CamMat2`** (input_control)  hom_mat2d `→`  (real / integer)

Camera matrix of the 2nd camera.

**`Method`** (input_control)  string `→`  (string)

Algorithm for the computation of the
essential matrix and for special camera orientations.

Default:
'normalized_dlt'

List of values:
'gold_standard', 'normalized_dlt', 'trans_gold_standard', 'trans_normalized_dlt'

**`EMatrix`** (output_control)  hom_mat2d `→`  (real)

Computed essential matrix.

**`CovEMat`** (output_control)  real-array `→`  (real)

9x9 covariance matrix of the
essential matrix.

**`Error`** (output_control)  real(-array) `→`  (real)

Root-Mean-Square of the epipolar distance error.

**`X`** (output_control)  real-array `→`  (real)

X coordinates of the reconstructed 3D points.

**`Y`** (output_control)  real-array `→`  (real)

Y coordinates of the reconstructed 3D points.

**`Z`** (output_control)  real-array `→`  (real)

Z coordinates of the reconstructed 3D points.

**`CovXYZ`** (output_control)  real-array `→`  (real)

Covariance matrices of the reconstructed 3D points.

## Possible Predecessors

`match_essential_matrix_ransac`

## Possible Successors

`essential_to_fundamental_matrix`

## Alternatives

`vector_to_rel_pose`,
`vector_to_fundamental_matrix`

## See also

`stationary_camera_self_calibration`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2003.
  
J.Chris McGlone (editor): “Manual of Photogrammetry”;
American Society for Photogrammetry and Remote Sensing ; 2004.

## Module

3D Metrology
