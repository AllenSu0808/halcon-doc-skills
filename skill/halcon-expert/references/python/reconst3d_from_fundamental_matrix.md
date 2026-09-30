# reconst3d_from_fundamental_matrix (Operator)

## Name

`reconst3d_from_fundamental_matrix` — Compute the projective 3d reconstruction of points based on the fundamental
matrix.

## Signature

`def reconst3d_from_fundamental_matrix(rows_1: MaybeSequence[Union[float, int]], cols_1: MaybeSequence[Union[float, int]], rows_2: MaybeSequence[Union[float, int]], cols_2: MaybeSequence[Union[float, int]], cov_rr1: MaybeSequence[Union[float, int]], cov_rc1: MaybeSequence[Union[float, int]], cov_cc1: MaybeSequence[Union[float, int]], cov_rr2: MaybeSequence[Union[float, int]], cov_rc2: MaybeSequence[Union[float, int]], cov_cc2: MaybeSequence[Union[float, int]], fmatrix: Sequence[float], cov_fmat: Sequence[float]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def reconst3d_from_fundamental_matrix_s(rows_1: MaybeSequence[Union[float, int]], cols_1: MaybeSequence[Union[float, int]], rows_2: MaybeSequence[Union[float, int]], cols_2: MaybeSequence[Union[float, int]], cov_rr1: MaybeSequence[Union[float, int]], cov_rc1: MaybeSequence[Union[float, int]], cov_cc1: MaybeSequence[Union[float, int]], cov_rr2: MaybeSequence[Union[float, int]], cov_rc2: MaybeSequence[Union[float, int]], cov_cc2: MaybeSequence[Union[float, int]], fmatrix: Sequence[float], cov_fmat: Sequence[float]) -> Tuple[float, float, float, float, float]`

## Description

A pair of stereo images is called weakly calibrated if the fundamental
matrix, which defines the geometric relation between the two images,
is known. Given such a fundamental matrix *`fmatrix`*
and a set of corresponding points
(*`rows_1`*,*`cols_1`*) and (*`rows_2`*,*`cols_2`*) the
operator
`reconst3d_from_fundamental_matrix` determines the three-dimensional
space points projecting onto these image points. This 3D reconstruction is
purely projective and the projective coordinates are returned by the
four-vector (*`x`*,*`y`*,*`z`*,*`w`*). This type of
reconstruction is also known as projective triangulation.
If additionally the covariances *`cov_rr1`*, *`cov_rc1`*,
*`cov_cc1`* and *`cov_rr2`*, *`cov_rc2`*, *`cov_cc2`*
of the image points are given the covariances of the reconstructed
points *`cov_xyzw`* are computed too.
Let n be the number of points. Then the concatenated
covariances are stored in a 16xn tuple.
The computation of the covariances is more precise if the covariance
of the fundamental matrix *`cov_fmat`* is provided.

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

**`rows_1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input points in image 1 (row coordinate).

**`cols_1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input points in image 1 (column coordinate).

**`rows_2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input points in image 2 (row coordinate).

**`cols_2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input points in image 2 (column coordinate).

**`cov_rr1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate variance of the points in image 1.

Default:
[]

**`cov_rc1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Covariance of the points in image 1.

Default:
[]

**`cov_cc1`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate variance of the points in image 1.

Default:
[]

**`cov_rr2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Row coordinate variance of the points in image 2.

Default:
[]

**`cov_rc2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Covariance of the points in image 2.

Default:
[]

**`cov_cc2`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Column coordinate variance of the points in image 2.

Default:
[]

**`fmatrix`** (input_control)  hom_mat2d `→` Sequence[float]

Fundamental matrix.

**`cov_fmat`** (input_control)  real-array `→` Sequence[float]

9x9 covariance matrix of the
fundamental matrix.

Default:
[]

**`x`** (output_control)  real(-array) `→` Sequence[float]

X coordinates of the reconstructed points
in projective 3D space.

**`y`** (output_control)  real(-array) `→` Sequence[float]

Y coordinates of the reconstructed points
in projective 3D space.

**`z`** (output_control)  real(-array) `→` Sequence[float]

Z coordinates of the reconstructed points
in projective 3D space.

**`w`** (output_control)  real(-array) `→` Sequence[float]

W coordinates of the reconstructed points
in projective 3D space.

**`cov_xyzw`** (output_control)  real(-array) `→` Sequence[float]

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
