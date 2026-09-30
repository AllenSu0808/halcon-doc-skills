# AffineTransPoint2d (Operator)

## Name

`AffineTransPoint2d` — Apply an arbitrary affine 2D transformation to points.

## Signature

`static void HOperatorSet.AffineTransPoint2d(HTuple homMat2D, HTuple px, HTuple py, out HTuple qx, out HTuple qy)`

`HTuple HHomMat2D.AffineTransPoint2d(HTuple px, HTuple py, out HTuple qy)`

`double HHomMat2D.AffineTransPoint2d(double px, double py, out double qy)`

## Description

`AffineTransPoint2d` applies an arbitrary affine 2D transformation,
i.e., scaling, rotation, translation, and slant (skewing), to the input
points (*`px`*,*`py`*) and returns the resulting points in
(*`qx`*,*`qy`*). The affine transformation is described by the
homogeneous transformation matrix given in *`homMat2D`*. This
corresponds to the following equation (input and output points as
homogeneous vectors):

$$\begin{pmatrix} Q_x \\ Q_y \\ 1 \end{pmatrix} = \mathrm{HomMat2D} \cdot \begin{pmatrix} P_x \\ P_y \\ 1 \end{pmatrix}$$ ![figure](../assets/142dc725bf475f23.svg)

If the points to transform are specified in standard image coordinates, their
*row* coordinates must be passed in *`px`* and their *column*
coordinates in *`py`*. This is necessary to obtain a right-handed
coordinate system for the image. In particular, this assures that rotations
are performed in the correct direction. Note that the (x,y) order of the
matrices quite naturally corresponds to the usual (row,column) order for
coordinates in the image.

The transformation matrix can be created using the operators
[`HomMat2dIdentity`](hom_mat2d_identity.md), [`HomMat2dRotate`](hom_mat2d_rotate.md),
[`HomMat2dTranslate`](hom_mat2d_translate.md), etc., or can be the result of operators like
[`VectorAngleToRigid`](vector_angle_to_rigid.md).

For example, if *`homMat2D`* corresponds to a rigid transformation,
i.e., if it consists of a rotation and a translation, the
points are transformed as follows:

$$\begin{pmatrix}Q_x\\Q_y\\1\end{pmatrix} = \begin{bmatrix}R & T\\0 & 1\end{bmatrix} \cdot \begin{pmatrix}P_x\\P_y\\1\end{pmatrix} = (R \cdot (\begin{pmatrix}P_x\\P_y\\1\end{pmatrix})) + T$$ ![figure](../assets/8751f45210ea5f75.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`px`** (input_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point(s) (x or row coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point(s) (y or column coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`qx`** (output_control)  point.x(-array) `→` [HTuple](HTuple.md) (*double*)

Output point(s) (x or row coordinate).

**`qy`** (output_control)  point.y(-array) `→` [HTuple](HTuple.md) (*double*)

Output point(s) (y or column coordinate).

## Result

If the matrix *`homMat2D`* represents an affine transformation
(i.e., not a projective transformation),
`AffineTransPoint2d` returns 2 (
H_MSG_TRUE)
. Otherwise, an exception
is raised.

## Possible Predecessors

`HomMat2dTranslate`,
`HomMat2dTranslateLocal`,
`HomMat2dScale`,
`HomMat2dScaleLocal`,
`HomMat2dRotate`,
`HomMat2dRotateLocal`,
`HomMat2dSlant`,
`HomMat2dSlantLocal`,
`HomMat2dReflect`,
`HomMat2dReflectLocal`

## Possible Successors

`HomMat2dTranslate`,
`HomMat2dTranslateLocal`,
`HomMat2dScale`,
`HomMat2dScaleLocal`,
`HomMat2dRotate`,
`HomMat2dRotateLocal`,
`HomMat2dSlant`,
`HomMat2dSlantLocal`,
`HomMat2dReflect`,
`HomMat2dReflectLocal`

## Module

Foundation
