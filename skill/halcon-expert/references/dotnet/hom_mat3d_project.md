# HomMat3dProject (Operator)

## Name

`HomMat3dProject` — Project an affine 3D transformation matrix to a 2D projective
transformation matrix.

## Signature

`static void HOperatorSet.HomMat3dProject(HTuple homMat3D, HTuple principalPointRow, HTuple principalPointCol, HTuple focus, out HTuple homMat2D)`

`HHomMat2D HHomMat3D.HomMat3dProject(HTuple principalPointRow, HTuple principalPointCol, HTuple focus)`

`HHomMat2D HHomMat3D.HomMat3dProject(double principalPointRow, double principalPointCol, double focus)`

## Description

`HomMat3dProject` calculates a homogeneous projection matrix
from a homogeneous 3x4 transformation matrix
describing an affine transformation in 3D. The result can be used to
project a plane, in particular a plane containing an image. The
projection matrix defines a projective transformation between two
(two-dimensional) planes.

This can be used to create perspective distortions, which occur in a
projection of a plane rotated around an axis other than the z axis.
Usually, however, projective transformations are determined from
point correspondences (see [`VectorToProjHomMat2d`](vector_to_proj_hom_mat2d.md),
[`HomVectorToProjHomMat2d`](hom_vector_to_proj_hom_mat2d.md), and
[`ProjMatchPointsRansac`](proj_match_points_ransac.md)).

Matrices for rotation, scale, and translation can be constructed
using the operators [`HomMat3dIdentity`](hom_mat3d_identity.md),
[`HomMat3dScale`](hom_mat3d_scale.md), [`HomMat3dRotate`](hom_mat3d_rotate.md),
[`HomMat3dTranslate`](hom_mat3d_translate.md) and [`PoseToHomMat3d`](pose_to_hom_mat3d.md).

Note that for 3D transformations the x-axis represents the column
axis while the y-axis represents the row axis (see also
[Calibration](toc_calibration.md)) while in [`ProjectiveTransImage`](projective_trans_image.md),
the first row of *`homMat2D`* contains the transformation of
the row axis and the second row contains the transformation of the
column axis of the image.

The point (*`principalPointRow`*, *`principalPointCol`*)
is the principal point of the projection and the point
(*`principalPointRow`*, *`principalPointCol`*, *0*)
can thus be interpreted as the position of the camera in a virtual
three-dimensional space. The direction of view is along the
positive z-axis.

In this virtual space the plane containing the input image as well
as the image plane are located at z=*`focus`*, which is *`focus`* pixels
away form the camera. As a result, using the identity matrix as the
input matrix *`homMat3D`* leads to a matrix *`homMat2D`*
which also represents the identity in 2D.

Consequently, the parameter *`focus`* is the “focal distance”
of the virtual camera used and its unit is pixels. Its value
influences the degree of perspective distortions. The same input
matrix at a bigger focal distance results in weaker distortions than
at a low focal distance.

Let H be the affine 3D matrix with elements $h_{ij}$,
(r,c)=(*`principalPointRow`*,*`principalPointCol`*)
and f=*`focus`*.

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
[`ProjectiveTransImage`](projective_trans_image.md):
$$P = \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix} \cdot R \cdot \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix}$$ ![figure](../assets/67b6fd0bb84fc94d.svg)

The overall transformation can be written as:
$$P = \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix} \cdot \begin{pmatrix}f & 0 & c\\0 & f & r\\0 & 0 & 1\end{pmatrix} \cdot \begin{pmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & -c\end{pmatrix} \cdot H \cdot \begin{pmatrix}1 & 0 & 0\\0 & 1 & 0\\0 & 0 & f\end{pmatrix} \cdot \begin{pmatrix}0 & 1 & 0\\1 & 0 & 0\\0 & 0 & 1\end{pmatrix}$$ ![figure](../assets/0d20e8e223033de4.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

3×4 3D transformation matrix.

**`principalPointRow`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the principal point.

Default:
256

Suggested values:
16, 32, 64, 128, 240, 256, 512

**`principalPointCol`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the principal point.

Default:
256

Suggested values:
16, 32, 64, 128, 256, 320, 512

**`focus`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Focal length in pixels.

Default:
256

Suggested values:
1, 2, 5, 256, 32768

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

## Possible Predecessors

`HomMat3dIdentity`,
`HomMat3dRotate`,
`HomMat3dTranslate`,
`HomMat3dScale`

## Possible Successors

`ProjectiveTransImage`,
`ProjectiveTransPoint2d`,
`ProjectiveTransRegion`,
`ProjectiveTransContourXld`,
`HomMat2dInvert`

## Module

Foundation
