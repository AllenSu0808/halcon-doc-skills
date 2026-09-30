# HomMat2dRotateLocal (Operator)

## Name

`HomMat2dRotateLocal` — Add a rotation to a homogeneous 2D transformation matrix.

## Signature

`static void HOperatorSet.HomMat2dRotateLocal(HTuple homMat2D, HTuple phi, out HTuple homMat2DRotate)`

`HHomMat2D HHomMat2D.HomMat2dRotateLocal(HTuple phi)`

`HHomMat2D HHomMat2D.HomMat2dRotateLocal(double phi)`

## Description

`HomMat2dRotateLocal` adds a rotation by the angle *`phi`* to
the homogeneous 2D transformation matrix *`homMat2D`* and returns the
resulting matrix in *`homMat2DRotate`*. The rotation is described by a
2×2 rotation matrix R. In
contrast to [`HomMat2dRotate`](hom_mat2d_rotate.md), it is performed relative to the local
coordinate system, i.e., the coordinate system described by
*`homMat2D`*; this corresponds to the following chain of transformation
matrices:

$$HomMat2DRotate = HomMat2D \cdot \begin{bmatrix} R & 0 \\ 0 & 1 \end{bmatrix} \;\; R = \begin{bmatrix} \cos(\Phi) & -\sin(\Phi) \\ \sin(\Phi) & \cos(\Phi) \end{bmatrix}$$ ![figure](../assets/69ed1d545fde7d0c.svg)

The fixed point of the transformation is the origin of the local
coordinate system, i.e., this point remains unchanged when
transformed using *`homMat2DRotate`*.

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

Note that homogeneous matrices are stored row-by-row as a tuple;
the last row is usually not stored because it is identical for all
homogeneous matrices that describe an affine transformation. For example,
the homogeneous matrix
$$\begin{bmatrix} ra & rb & tc \\ rd & re & tf \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/df89bc3c248f6e2e.svg)
is stored as the tuple [ra, rb, tc, rd, re, tf]. However, it is also
possible to process full 3×3 matrices, which represent
a projective 2D transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`phi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Rotation angle.

Default:
0.78

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.78, 1.57, 3.14

Value range:
`0
≤
phi
≤
6.28318530718`

**`homMat2DRotate`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

If the parameters are valid, the operator
`HomMat2dRotateLocal` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`HomMat2dIdentity`,
`HomMat2dTranslateLocal`,
`HomMat2dScaleLocal`,
`HomMat2dRotateLocal`,
`HomMat2dSlantLocal`,
`HomMat2dReflectLocal`

## Possible Successors

`HomMat2dTranslateLocal`,
`HomMat2dScaleLocal`,
`HomMat2dRotateLocal`,
`HomMat2dSlantLocal`,
`HomMat2dReflectLocal`

## See also

`HomMat2dRotate`

## Module

Foundation
