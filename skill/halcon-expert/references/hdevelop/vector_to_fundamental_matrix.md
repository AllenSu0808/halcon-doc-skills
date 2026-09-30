# vector_to_fundamental_matrix (Operator)

## Name

`vector_to_fundamental_matrix` — Compute the fundamental matrix given a set of image point
correspondences and reconstruct 3D points.

## Signature

`vector_to_fundamental_matrix( : : Rows1, Cols1, Rows2, Cols2, CovRR1, CovRC1, CovCC1, CovRR2, CovRC2, CovCC2, Method : FMatrix, CovFMat, Error, X, Y, Z, W, CovXYZW)`

## Description

For a stereo configuration with unknown camera parameters the geometric
relation between the two images is defined by the fundamental matrix.
The operator `vector_to_fundamental_matrix` determines the fundamental
matrix *`FMatrix`* from given point correspondences
(*`Rows1`*,*`Cols1`*), (*`Rows2`*,*`Cols2`*), that
fulfill the epipolar constraint:
$$\left(\begin{array}{c}\text{Cols2}\\ \text{Rows2}\\ 1\end{array}\right)^{\mathrm{T}} \\cdot \mathrm{FMatrix} \\left(\begin{array}{c}\text{Cols1}\\ \text{Rows1}\\ 1\end{array}\right) = 0 .$$ ![figure](../assets/e225b53fa907dd55.svg)

Note the column/row ordering in the point coordinates: since the fundamental
matrix encodes the projective relation between two stereo images embedded
in 3D space, the x/y notation must be compliant with the camera coordinate
system. Therefore, (x,y) coordinates correspond to (column,row) pairs.

For a general relative orientation of the two cameras the minimum number of
required point correspondences is eight. Then, *`Method`* is chosen
to be *'normalized_dlt'* or *'gold_standard'*.
If left and right camera are identical and the relative orientation between
them is a pure translation then choose *`Method`* equal to
*'trans_normalized_dlt'* or *'trans_gold_standard'*.
In this special case the minimum number of correspondences is only two.
The typical application of the motion being a pure translation is that of a
single fixed camera looking onto a moving conveyor belt.

The fundamental matrix is determined by minimizing a cost function.
To minimize the respective error different algorithms are available, and
the user can choose between the direct-linear-transformation
('normalized_dlt') and the gold-standard-algorithm ('gold_standard').
Like the motion case,
the algorithm can be selected with the parameter *`Method`*.
For *`Method`* = *'normalized_dlt'* or
*'trans_normalized_dlt'*, a linear algorithm minimizes an algebraic
error based on the above epipolar constraint.
This algorithm offers a good compromise between speed
and accuracy.
For *`Method`* = *'gold_standard'* or
*'trans_gold_standard'*,
a mathematically optimal, but slower optimization is used, which
minimizes the geometric backprojection error of reconstructed
projective 3D points. In this case, in addition to the fundamental
matrix its
covariance matrix *`CovFMat`* is output, along with the projective
coordinates (*`X`*,*`Y`*,*`Z`*,*`W`*) of the
reconstructed
points and their covariances *`CovXYZW`*.
Let n be the number of points. Then the concatenated
covariances are stored in a 16xn tuple.

If an optimal gold-standard-algorithm is chosen the covariances of the image
points (*`CovRR1`*, *`CovRC1`*, *`CovCC1`*, *`CovRR2`*,
*`CovRC2`*, *`CovCC2`*) can be incorporated in the computation.
They can be provided for example by the operator [`points_foerstner`](points_foerstner.md).
If the point covariances are unknown, which is the default, empty tuples
are input. In this case the optimization algorithm internally assumes
uniform and equal covariances for all points.

The value *`Error`* indicates the overall quality of the optimization
procedure and is the mean Euclidean distance in pixels between the
points and their corresponding epipolar lines.

If the correspondence between the points are not known,
[`match_fundamental_matrix_ransac`](match_fundamental_matrix_ransac.md) should be used instead.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Rows1`** (input_control)  number-array `→`  (real / integer)

Input points in image 1 (row coordinate).

Restriction:
`length(Rows1) >= 8 || length(Rows1) >= 2`

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

**`Method`** (input_control)  string `→`  (string)

Estimation algorithm.

Default:
'normalized_dlt'

List of values:
'gold_standard', 'normalized_dlt', 'trans_gold_standard', 'trans_normalized_dlt'

**`FMatrix`** (output_control)  hom_mat2d `→`  (real)

Computed fundamental matrix.

**`CovFMat`** (output_control)  real-array `→`  (real)

9x9 covariance matrix of the
fundamental matrix.

**`Error`** (output_control)  real `→`  (real)

Root-Mean-Square of the epipolar distance error.

**`X`** (output_control)  real-array `→`  (real)

X coordinates of the reconstructed points in
projective 3D space.

**`Y`** (output_control)  real-array `→`  (real)

Y coordinates of the reconstructed points in
projective 3D space.

**`Z`** (output_control)  real-array `→`  (real)

Z coordinates of the reconstructed points in
projective 3D space.

**`W`** (output_control)  real-array `→`  (real)

W coordinates of the reconstructed points in
projective 3D space.

**`CovXYZW`** (output_control)  real-array `→`  (real)

Covariance matrices of the reconstructed 3D points.

## Possible Predecessors

`match_fundamental_matrix_ransac`

## Possible Successors

`gen_binocular_proj_rectification`

## Alternatives

`vector_to_essential_matrix`,
`vector_to_rel_pose`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

3D Metrology
