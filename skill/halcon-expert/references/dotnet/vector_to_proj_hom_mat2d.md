# VectorToProjHomMat2d (Operator)

## Name

`VectorToProjHomMat2d` — Compute a projective transformation matrix using given point
correspondences.

## Signature

`static void HOperatorSet.VectorToProjHomMat2d(HTuple px, HTuple py, HTuple qx, HTuple qy, HTuple method, HTuple covXX1, HTuple covYY1, HTuple covXY1, HTuple covXX2, HTuple covYY2, HTuple covXY2, out HTuple homMat2D, out HTuple covariance)`

`HTuple HHomMat2D.VectorToProjHomMat2d(HTuple px, HTuple py, HTuple qx, HTuple qy, string method, HTuple covXX1, HTuple covYY1, HTuple covXY1, HTuple covXX2, HTuple covYY2, HTuple covXY2)`

## Description

`VectorToProjHomMat2d` determines the homogeneous
projective transformation matrix *`homMat2D`* that optimally
fulfills the following equations given by at least 4 point
correspondences
$$\text{HomMat2D} \cdot \begin{pmatrix} P_x \\ P_y \\ 1 \end{pmatrix} = \begin{pmatrix} Q_x \\ Q_y \\ 1 \end{pmatrix}.$$ ![figure](../assets/fc13bb48fb3ace35.svg)
If fewer than 4 pairs of points (*`px`*,*`py`*),
(*`qx`*,*`qy`*) are given, there exists no unique
solution, if exactly 4 pairs are supplied the matrix
*`homMat2D`* transforms them in exactly the desired way, and if
there are more than 4 point pairs given,
`VectorToProjHomMat2d` seeks to minimize the
transformation error. To achieve such a minimization, several
different algorithms are available. The algorithm to use can be
chosen using the parameter *`method`*.
*`method`*=*"dlt"* uses a fast and simple, but also
rather inaccurate error estimation algorithm while
*`method`*=*"normalized_dlt"* offers a good compromise
between speed and accuracy. Finally,
*`method`*=*"gold_standard"* performs a mathematically
optimal but slower optimization.

If *"gold_standard"* is used and the input points have been
obtained from an operator like [`PointsFoerstner`](points_foerstner.md), which
provides a covariance matrix for each of the points, which specifies
the accuracy of the points, this can be taken into account by using
the input parameters *`covYY1`*, *`covXX1`*,
*`covXY1`* for the points in the first image and
*`covYY2`*, *`covXX2`*, *`covXY2`* for the points in
the second image. The covariances are symmetric 2×2
matrices. *`covXX1`*/*`covXX2`* and
*`covYY1`*/*`covYY2`* are a list of diagonal entries while
*`covXY1`*/*`covXY2`* contains the non-diagonal entries
which appear twice in a symmetric matrix. If a different
*`method`* than *"gold_standard"* is used or the
covariances are unknown the covariance parameters can be left
empty.

In contrast to [`HomVectorToProjHomMat2d`](hom_vector_to_proj_hom_mat2d.md), points at
infinity cannot be used to determine the transformation in
`VectorToProjHomMat2d`. If this is necessary,
[`HomVectorToProjHomMat2d`](hom_vector_to_proj_hom_mat2d.md) must be used. If the
correspondence between the points has not been determined,
[`ProjMatchPointsRansac`](proj_match_points_ransac.md) should be used to determine the
correspondence as well as the transformation.

If the points to transform are specified in standard image
coordinates, their *row* coordinates must be passed in
*`px`* and their *column* coordinates in *`py`*. This
is necessary to obtain a right-handed coordinate system for the
image. In particular, this assures that rotations are performed in
the correct direction. Note that the (x,y) order of the
matrices quite naturally corresponds to the usual (row,column) order
for coordinates in the image.

## Attention

It should be noted that homogeneous transformation matrices refer to
a general right-handed mathematical coordinate system. If a
homogeneous transformation matrix is used to transform images,
regions, XLD contours, or any other data that has been extracted
from images, the row coordinates of the transformation must be
passed in the x coordinates, while the column coordinates must be
passed in the y coordinates. Consequently, the order of passing row
and column coordinates follows the usual order
(`row`,`column`). This convention is essential to
obtain a right-handed coordinate system for the transformation of
iconic data, and consequently to ensure in particular that rotations
are performed in the correct mathematical direction.

Furthermore, it should be noted that if a homogeneous transformation
matrix is used to transform images, regions, XLD contours, or any
other data that has been extracted from images, it is assumed that
the origin of the coordinate system of the homogeneous
transformation matrix lies in the upper left corner of a pixel. The
image processing operators that return point coordinates, however,
assume a coordinate system in which the origin lies in the center of
a pixel. Therefore, to obtain a consistent homogeneous
transformation matrix, 0.5 must be added to the point coordinates
before computing the transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`px`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (row coordinate).

**`py`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double* / int / long)

Input points in image 1 (column coordinate).

**`qx`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

Input points in image 2 (row coordinate).

**`qy`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Input points in image 2 (column coordinate).

**`method`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Estimation algorithm.

Default:
"normalized_dlt"

List of values:
"dlt", "gold_standard", "normalized_dlt"

**`covXX1`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate variance of the points in image 1.

Default:
[]

**`covYY1`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate variance of the points in image 1.

Default:
[]

**`covXY1`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Covariance of the points in image 1.

Default:
[]

**`covXX2`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Row coordinate variance of the points in image 2.

Default:
[]

**`covYY2`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Column coordinate variance of the points in image 2.

Default:
[]

**`covXY2`** (input_control)  real-array `→` [HTuple](HTuple.md) (*double*)

Covariance of the points in image 2.

Default:
[]

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

**`covariance`** (output_control)  real-array `→` [HTuple](HTuple.md) (*double*)

9×9 covariance matrix of the
projective transformation matrix.

## Possible Predecessors

`ProjMatchPointsRansac`,
`ProjMatchPointsRansacGuided`,
`PointsFoerstner`,
`PointsHarris`

## Possible Successors

`ProjectiveTransImage`,
`ProjectiveTransImageSize`,
`ProjectiveTransRegion`,
`ProjectiveTransContourXld`,
`ProjectiveTransPoint2d`,
`ProjectiveTransPixel`

## Alternatives

`HomVectorToProjHomMat2d`,
`ProjMatchPointsRansac`,
`ProjMatchPointsRansacGuided`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Calibration
