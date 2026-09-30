# hom_mat2d_rotate (Operator)

## Name

`hom_mat2d_rotate` — Add a rotation to a homogeneous 2D transformation matrix.

## Signature

`hom_mat2d_rotate( : : HomMat2D, Phi, Px, Py : HomMat2DRotate)`

## Description

`hom_mat2d_rotate` adds a rotation by the angle *`Phi`* to the
homogeneous 2D transformation matrix *`HomMat2D`* and returns the
resulting matrix in *`HomMat2DRotate`*. The rotation is described by a
2×2 rotation matrix R. It is
performed relative to the global (i.e., fixed) coordinate system; this
corresponds to the following chain of transformation matrices:

$$HomMat2DRotate = \left[\begin{array}{ccc}R & 0 & 0\\0 & 0 & 0\\0 & 0 & 1\end{array}\right] \cdot HomMat2D R = \left[\begin{array}{cc} \cos(\phi) & -\sin(\phi)\\ \sin(\phi) & \cos(\phi) \end{array}\right]$$ ![figure](../assets/a0e7ab92d78b3ae5.svg)

The point (*`Px`*,*`Py`*) is the fixed point of the transformation,
i.e., this point remains unchanged when transformed using
*`HomMat2DRotate`*. To obtain this behavior, first a translation is
added to the input transformation matrix that moves the fixed point onto the
origin of the global coordinate system. Then, the rotation is added, and
finally a translation that moves the fixed point back to its original
position. This corresponds to the following chain of transformations:

$$\mathrm{HomMat2DRotate} = \begin{bmatrix}1 & 0 & +P_x \\ 0 & 1 & +P_y \\ 0 & 0 & 1\end{bmatrix} \cdot \begin{bmatrix}R & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix} \cdot \begin{bmatrix}1 & 0 & -P_x \\ 0 & 1 & -P_y \\ 0 & 0 & 1\end{bmatrix} \cdot \mathrm{HomMat2D$$ ![figure](../assets/14a071b9e2acd25c.svg)

To perform the transformation in the local coordinate system, i.e.,
the one described by *`HomMat2D`*, use
[`hom_mat2d_rotate_local`](hom_mat2d_rotate_local.md).

## Attention

It should be noted that homogeneous transformation matrices refer to
a general right-handed mathematical coordinate system. If a
homogeneous transformation matrix is used to transform images,
regions, XLD contours, or any other data that has been extracted
from images, the row coordinates of the transformation must be
passed in the x coordinates, while the column coordinates must be
passed in the y coordinates. Consequently, the order of passing row
and column coordinates follows the usual order
(`Row`,`Column`). This convention is essential to
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

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Input transformation matrix.

**`Phi`** (input_control)  angle.rad `→`  (real / integer)

Rotation angle.

Default:
0.78

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.78, 1.57, 3.14

Value range:
`0
≤
Phi
≤
6.28318530718`

**`Px`** (input_control)  point.x `→`  (real / integer)

Fixed point of the transformation (x coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Py`** (input_control)  point.y `→`  (real / integer)

Fixed point of the transformation (y coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`HomMat2DRotate`** (output_control)  hom_mat2d `→`  (real)

Output transformation matrix.

## Result

If the parameters are valid, the operator `hom_mat2d_rotate` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`hom_mat2d_identity`,
`hom_mat2d_translate`,
`hom_mat2d_scale`,
`hom_mat2d_rotate`,
`hom_mat2d_slant`,
`hom_mat2d_reflect`

## Possible Successors

`hom_mat2d_translate`,
`hom_mat2d_scale`,
`hom_mat2d_rotate`,
`hom_mat2d_slant`,
`hom_mat2d_reflect`

## See also

`hom_mat2d_rotate_local`

## Module

Foundation
