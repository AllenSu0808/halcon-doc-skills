# VectorToFundamentalMatrix (Operator)

## Name

`VectorToFundamentalMatrix` — Compute the fundamental matrix given a set of image point
correspondences and reconstruct 3D points.

## Signature

`static void HOperatorSet.VectorToFundamentalMatrix(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, HTuple method, out HTuple FMatrix, out HTuple covFMat, out HTuple error, out HTuple x, out HTuple y, out HTuple z, out HTuple w, out HTuple covXYZW)`

`HTuple HHomMat2D.VectorToFundamentalMatrix(HTuple rows1, HTuple cols1, HTuple rows2, HTuple cols2, HTuple covRR1, HTuple covRC1, HTuple covCC1, HTuple covRR2, HTuple covRC2, HTuple covCC2, string method, out double error, out HTuple x, out HTuple y, out HTuple z, out HTuple w, out HTuple covXYZW)`

## Description

For a stereo configuration with unknown camera parameters the geometric
relation between the two images is defined by the fundamental matrix.
The operator `VectorToFundamentalMatrix` determines the fundamental
matrix *`FMatrix`* from given point correspondences
(*`rows1`*,*`cols1`*), (*`rows2`*,*`cols2`*), that
fulfill the epipolar constraint:
$$\left(\begin{array}{c}\text{Cols2}\\ \text{Rows2}\\ 1\end{array}\right)^{\mathrm{T}} \\cdot \mathrm{FMatrix} \\left(\begin{array}{c}\text{Cols1}\\ \text{Rows1}\\ 1\end{array}\right) = 0 .$$ ![figure](../assets/e225b53fa907dd55.svg)

Note the column/row ordering in the point coordinates: since the fundamental
matrix encodes the projective relation between two stereo images embedded
in 3D space, the x/y notation must be compliant with the camera coordinate
system. Therefore, (x,y) coordinates correspond to (column,row) pairs.

For a general relative orientation of the two cameras the minimum number of
required point correspondences is eight. Then, *`method`* is chosen
to be *"normalized_dlt"* or *"gold_standard"*.
If left and right camera are identical and the relative orientation between
them is a pure translation then choose *`method`* equal to
*"trans_normalized_dlt"* or *"trans_gold_standard"*.
In this special case the minimum number of correspondences is only two.
The typical application of the motion being a pure translation is that of a
single fixed camera looking onto a moving conveyor belt.

The fundamental matrix is determined by minimizing a cost function.
To minimize the respective error different algorithms are available, and
the user can choose between the direct-linear-transformation
('normalized_dlt') and the gold-standard-algorithm ('gold_standard').
Like the motion case,
the algorithm can be selected with the parameter *`method`*.
For *`method`* = *"normalized_dlt"* or
*"trans_normalized_dlt"*, a linear algorithm minimizes an algebraic
error based on the above epipolar constraint.
This algorithm offers a good compromise between speed
and accuracy.
For *`method`* = *"gold_standard"* or
*"trans_gold_standard"*,
a mathematically optimal, but slower optimization is used, which
minimizes the geometric backprojection error of reconstructed
projective 3D points. In this case, in addition to the fundamental
matrix its
covariance matrix *`covFMat`* is output, along with the projective
coordinates (*`x`*,*`y`*,*`z`*,*`w`*) of the
reconstructed
points and their covariances *`covXYZW`*.
Let n be the number of points. Then the concatenated
covariances are stored in a 16xn tuple.

If an optimal gold-standard-algorithm is chosen the covariances of the image
points (*`covRR1`*, *`covRC1`*, *`covCC1`*, *`covRR2`*,
*`covRC2`*, *`covCC2`*) can be incorporated in the computation.
They can be provided for example by the operator [`PointsFoerstner`](points_foerstner.md).
If the point covariances are unknown, which is the default, empty tuples
are input. In this case the optimization algorithm internally assumes
uniform and equal covariances for all points.

The value *`error`* indicates the overall quality of the optimization
procedure and is the mean Euclidean distance in pixels between the
points and their corresponding epipolar lines.

If the correspondence between the points are not known,
[`MatchFundamentalMatrixRansac`](match_fundamental_matrix_ransac.md) should be used instead.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`rows1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (row coordinate).

Restriction:
`length(Rows1) >= 8 || length(Rows1) >= 2`

**`cols1`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (column coordinate).

Restriction:
`length(Cols1) == length(Rows1)`

**`rows2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 2 (row coordinate).

Restriction:
`length(Rows2) == length(Rows1)`

**`cols2`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Estimation algorithm.

Default:
"normalized_dlt"

List of values:
"gold_standard", "normalized_dlt", "trans_gold_standard", "trans_normalized_dlt"

**`FMatrix`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Computed fundamental matrix.

**`covFMat`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

9x9 covariance matrix of the
fundamental matrix.

**`error`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Root-Mean-Square of the epipolar distance error.

**`x`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the reconstructed points in
projective 3D space.

**`y`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the reconstructed points in
projective 3D space.

**`z`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the reconstructed points in
projective 3D space.

**`w`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

W coordinates of the reconstructed points in
projective 3D space.

**`covXYZW`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Covariance matrices of the reconstructed 3D points.

## Possible Predecessors

`MatchFundamentalMatrixRansac`

## Possible Successors

`GenBinocularProjRectification`

## Alternatives

`VectorToEssentialMatrix`,
`VectorToRelPose`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

3D Metrology
