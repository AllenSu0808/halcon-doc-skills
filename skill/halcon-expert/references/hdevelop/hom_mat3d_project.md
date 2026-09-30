# hom_mat3d_project (Operator)

## Name

`hom_mat3d_project` — Project an affine 3D transformation matrix to a 2D projective
transformation matrix.

## Signature

`hom_mat3d_project( : : HomMat3D, PrincipalPointRow, PrincipalPointCol, Focus : HomMat2D)`

## Description

`hom_mat3d_project` calculates a homogeneous projection matrix
from a homogeneous 3x4 transformation matrix
describing an affine transformation in 3D. The result can be used to
project a plane, in particular a plane containing an image. The
projection matrix defines a projective transformation between two
(two-dimensional) planes.

This can be used to create perspective distortions, which occur in a
projection of a plane rotated around an axis other than the z axis.
Usually, however, projective transformations are determined from
point correspondences (see [`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md),
[`hom_vector_to_proj_hom_mat2d`](hom_vector_to_proj_hom_mat2d.md), and
[`proj_match_points_ransac`](proj_match_points_ransac.md)).

Matrices for rotation, scale, and translation can be constructed
using the operators [`hom_mat3d_identity`](hom_mat3d_identity.md),
[`hom_mat3d_scale`](hom_mat3d_scale.md), [`hom_mat3d_rotate`](hom_mat3d_rotate.md),
[`hom_mat3d_translate`](hom_mat3d_translate.md) and [`pose_to_hom_mat3d`](pose_to_hom_mat3d.md).

Note that for 3D transformations the x-axis represents the column
axis while the y-axis represents the row axis (see also
[Calibration](toc_calibration.md)) while in [`projective_trans_image`](projective_trans_image.md),
the first row of *`HomMat2D`* contains the transformation of
the row axis and the second row contains the transformation of the
column axis of the image.

The point (*`PrincipalPointRow`*, *`PrincipalPointCol`*)
is the principal point of the projection and the point
(*`PrincipalPointRow`*, *`PrincipalPointCol`*, *0*)
can thus be interpreted as the position of the camera in a virtual
three-dimensional space. The direction of view is along the
positive z-axis.

In this virtual space the plane containing the input image as well
as the image plane are located at z=*`Focus`*, which is *`Focus`* pixels
away form the camera. As a result, using the identity matrix as the
input matrix *`HomMat3D`* leads to a matrix *`HomMat2D`*
which also represents the identity in 2D.

Consequently, the parameter *`Focus`* is the “focal distance”
of the virtual camera used and its unit is pixels. Its value
influences the degree of perspective distortions. The same input
matrix at a bigger focal distance results in weaker distortions than
at a low focal distance.

Let H be the affine 3D matrix with elements $h_{ij}$,
(r,c)=(*`PrincipalPointRow`*,*`PrincipalPointCol`*)
and f=*`Focus`*.

Then the projective transformation matrix is calculated as follows:
First, a 3x4 projection matrix is calculated as:
$$Q = \begin{pmatrix} f & 0 & c \\ 0 & f & r \\ 0 & 0 & 1 \ \end{pmatrix} \cdot \begin{pmatrix} 1 & 0 & 0 & -c \\ 0 & 1 & 0 & -r \\ 0 & 0 & 1 & 0 \ \end{pmatrix} \cdot \begin{pmatrix} h_{11} & h_{12} & h_{13} & h_{14} \\ h_{21} & h_{22} & h_{23} & h_{24} \\ h_{31} & h_{32} & h_{33} & h_{34} \\ 0 & 0 & 0 & 1 \ \end{pmatrix}$$ ![figure](../assets/b949f17cb07c4ada.svg)

Since the image of a plane containing points (x, y, f, 1)^T is to
be calculated the last two columns of Q can be joined:
$$R = \begin{pmatrix} r_{11} & r_{12} & r_{13} \\ r_{21} & r_{22} & r_{23} \\ r_{31} & r_{32} & r_{33} \end{pmatrix} = \begin{pmatrix} q_{11} & q_{12} & f\cdot q_{13} + q_{14} \\ q_{21} & q_{22} & f\cdot q_{23} + q_{24} \\ q_{31} & q_{32} & f\cdot q_{33} + q_{34} \end{pmatrix} = Q \cdot \begin{pmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{pmatrix}$$ ![figure](../assets/b247834f9962352c.svg)

Finally, the columns and rows of R are swapped in a way that the
first row of P contains the transformation of the row coordinates
and the second row contains the transformation of the column
coordinates so that P can be used directly in
[`projective_trans_image`](projective_trans_image.md):
$$P = \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix} \cdot R \cdot \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix}$$ ![figure](../assets/67b6fd0bb84fc94d.svg)

The overall transformation can be written as:
$$P = \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix} \cdot \begin{pmatrix}f & 0 & c\\0 & f & r\\0 & 0 & 1\end{pmatrix} \cdot \begin{pmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & -c\end{pmatrix} \cdot H \cdot \begin{pmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & f\end{pmatrix} \cdot \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix}$$ ![figure](../assets/0d20e8e223033de4.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HomMat3D`** (input_control)  hom_mat3d `→`  (real)

3×4 3D transformation matrix.

**`PrincipalPointRow`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the principal point.

Default:
256

Suggested values:
16, 32, 64, 128, 240, 256, 512

**`PrincipalPointCol`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the principal point.

Default:
256

Suggested values:
16, 32, 64, 128, 256, 320, 512

**`Focus`** (input_control)  number `→`  (real / integer)

Focal length in pixels.

Default:
256

Suggested values:
1, 2, 5, 256, 32768

**`HomMat2D`** (output_control)  hom_mat2d `→`  (real)

Homogeneous projective transformation matrix.

## Possible Predecessors

`hom_mat3d_identity`,
`hom_mat3d_rotate`,
`hom_mat3d_translate`,
`hom_mat3d_scale`

## Possible Successors

`projective_trans_image`,
`projective_trans_point_2d`,
`projective_trans_region`,
`projective_trans_contour_xld`,
`hom_mat2d_invert`

## Module

Foundation
