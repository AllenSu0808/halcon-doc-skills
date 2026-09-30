# reconst3d_from_fundamental_matrix (Operator)

## Name

`reconst3d_from_fundamental_matrix` — Compute the projective 3d reconstruction of points based on the fundamental
matrix.

## Signature

`reconst3d_from_fundamental_matrix( : : Rows1, Cols1, Rows2, Cols2, CovRR1, CovRC1, CovCC1, CovRR2, CovRC2, CovCC2, FMatrix, CovFMat : X, Y, Z, W, CovXYZW)`

## Description

A pair of stereo images is called weakly calibrated if the fundamental
matrix, which defines the geometric relation between the two images,
is known. Given such a fundamental matrix *`FMatrix`*
and a set of corresponding points
(*`Rows1`*,*`Cols1`*) and (*`Rows2`*,*`Cols2`*) the
operator
`reconst3d_from_fundamental_matrix` determines the three-dimensional
space points projecting onto these image points. This 3D reconstruction is
purely projective and the projective coordinates are returned by the
four-vector (*`X`*,*`Y`*,*`Z`*,*`W`*). This type of
reconstruction is also known as projective triangulation.
If additionally the covariances *`CovRR1`*, *`CovRC1`*,
*`CovCC1`* and *`CovRR2`*, *`CovRC2`*, *`CovCC2`*
of the image points are given the covariances of the reconstructed
points *`CovXYZW`* are computed too.
Let n be the number of points. Then the concatenated
covariances are stored in a 16xn tuple.
The computation of the covariances is more precise if the covariance
of the fundamental matrix *`CovFMat`* is provided.

The operator `reconst3d_from_fundamental_matrix` is typically used
after [`match_fundamental_matrix_ransac`](match_fundamental_matrix_ransac.md) to perform 3d
reconstruction.
This will save computational cost compared with the deployment of
[`vector_to_fundamental_matrix`](vector_to_fundamental_matrix.md).

`reconst3d_from_fundamental_matrix` is the projective equivalent to the
Euclidean reconstruction operator [`intersect_lines_of_sight`](intersect_lines_of_sight.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Rows1`** (input_control)  number(-array) `→`  (real / integer)

Input points in image 1 (row coordinate).

**`Cols1`** (input_control)  number(-array) `→`  (real / integer)

Input points in image 1 (column coordinate).

**`Rows2`** (input_control)  number(-array) `→`  (real / integer)

Input points in image 2 (row coordinate).

**`Cols2`** (input_control)  number(-array) `→`  (real / integer)

Input points in image 2 (column coordinate).

**`CovRR1`** (input_control)  number(-array) `→`  (real / integer)

Row coordinate variance of the points in image 1.

Default:
[]

**`CovRC1`** (input_control)  number(-array) `→`  (real / integer)

Covariance of the points in image 1.

Default:
[]

**`CovCC1`** (input_control)  number(-array) `→`  (real / integer)

Column coordinate variance of the points in image 1.

Default:
[]

**`CovRR2`** (input_control)  number(-array) `→`  (real / integer)

Row coordinate variance of the points in image 2.

Default:
[]

**`CovRC2`** (input_control)  number(-array) `→`  (real / integer)

Covariance of the points in image 2.

Default:
[]

**`CovCC2`** (input_control)  number(-array) `→`  (real / integer)

Column coordinate variance of the points in image 2.

Default:
[]

**`FMatrix`** (input_control)  hom_mat2d `→`  (real)

Fundamental matrix.

**`CovFMat`** (input_control)  real-array `→`  (real)

9x9 covariance matrix of the
fundamental matrix.

Default:
[]

**`X`** (output_control)  real(-array) `→`  (real)

X coordinates of the reconstructed points
in projective 3D space.

**`Y`** (output_control)  real(-array) `→`  (real)

Y coordinates of the reconstructed points
in projective 3D space.

**`Z`** (output_control)  real(-array) `→`  (real)

Z coordinates of the reconstructed points
in projective 3D space.

**`W`** (output_control)  real(-array) `→`  (real)

W coordinates of the reconstructed points
in projective 3D space.

**`CovXYZW`** (output_control)  real(-array) `→`  (real)

Covariance matrices of the reconstructed points.

## Possible Predecessors

`match_fundamental_matrix_ransac`

## Alternatives

`vector_to_fundamental_matrix`,
`intersect_lines_of_sight`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.

## Module

3D Metrology
