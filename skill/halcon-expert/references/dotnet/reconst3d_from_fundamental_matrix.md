# Reconst3dFromFundamentalMatrix (Operator)

## Name

`Reconst3dFromFundamentalMatrix` — Compute the projective 3d reconstruction of points based on the fundamental
matrix.

## Signature

`static void HOperatorSet.Reconst3dFromFundamentalMatrix(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HTuple FMatrix, HTuple covFMat, out HTuple x, out HTuple y, out HTuple z, out HTuple w, out HTuple covXYZW)`

`void HHomMat2D.Reconst3dFromFundamentalMatrix(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HTuple covFMat, out HTuple x, out HTuple y, out HTuple z, out HTuple w, out HTuple covXYZW)`

`void HHomMat2D.Reconst3dFromFundamentalMatrix(double rows1, double cols1, double rows2, double cols2, double covRR1, double covRC1, double covCC1, double covRR2, double covRC2, double covCC2, HTuple covFMat, out double x, out double y, out double z, out double w, out double covXYZW)`

## Description

A pair of stereo images is called weakly calibrated if the fundamental
matrix, which defines the geometric relation between the two images,
is known. Given such a fundamental matrix *`FMatrix`*
and a set of corresponding points
(*`rows1`*,*`cols1`*) and (*`rows2`*,*`cols2`*) the
operator
`Reconst3dFromFundamentalMatrix` determines the three-dimensional
space points projecting onto these image points. This 3D reconstruction is
purely projective and the projective coordinates are returned by the
four-vector (*`x`*,*`y`*,*`z`*,*`w`*). This type of
reconstruction is also known as projective triangulation.
If additionally the covariances *`covRR1`*, *`covRC1`*,
*`covCC1`* and *`covRR2`*, *`covRC2`*, *`covCC2`*
of the image points are given the covariances of the reconstructed
points *`covXYZW`* are computed too.
Let n be the number of points. Then the concatenated
covariances are stored in a 16xn tuple.
The computation of the covariances is more precise if the covariance
of the fundamental matrix *`covFMat`* is provided.

The operator `Reconst3dFromFundamentalMatrix` is typically used
after [`MatchFundamentalMatrixRansac`](match_fundamental_matrix_ransac.md) to perform 3d
reconstruction.
This will save computational cost compared with the deployment of
[`VectorToFundamentalMatrix`](vector_to_fundamental_matrix.md).

`Reconst3dFromFundamentalMatrix` is the projective equivalent to the
Euclidean reconstruction operator [`IntersectLinesOfSight`](intersect_lines_of_sight.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rows1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (row coordinate).

**`cols1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (column coordinate).

**`rows2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (row coordinate).

**`cols2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (column coordinate).

**`covRR1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate variance of the points in image 1.

Default:
[]

**`covRC1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Covariance of the points in image 1.

Default:
[]

**`covCC1`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate variance of the points in image 1.

Default:
[]

**`covRR2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate variance of the points in image 2.

Default:
[]

**`covRC2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Covariance of the points in image 2.

Default:
[]

**`covCC2`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate variance of the points in image 2.

Default:
[]

**`FMatrix`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Fundamental matrix.

**`covFMat`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

9x9 covariance matrix of the
fundamental matrix.

Default:
[]

**`x`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

X coordinates of the reconstructed points
in projective 3D space.

**`y`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the reconstructed points
in projective 3D space.

**`z`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the reconstructed points
in projective 3D space.

**`w`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

W coordinates of the reconstructed points
in projective 3D space.

**`covXYZW`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Covariance matrices of the reconstructed points.

## Possible Predecessors

`MatchFundamentalMatrixRansac`

## Alternatives

`VectorToFundamentalMatrix`,
`IntersectLinesOfSight`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.

## Module

3D Metrology
