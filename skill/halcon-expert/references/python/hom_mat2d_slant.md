# hom_mat2d_slant (Operator)

## Name

`hom_mat2d_slant` — Add a slant to a homogeneous 2D transformation matrix.

## Signature

`def hom_mat2d_slant(hom_mat_2d: Sequence[float], theta: Union[float, int], axis: str, px: Union[float, int], py: Union[float, int]) -> Sequence[float]`

## Description

`hom_mat2d_slant` adds a slant by the angle *`theta`* to the
homogeneous 2D transformation matrix *`hom_mat_2d`* and returns the
resulting matrix in *`hom_mat_2dslant`*. A slant is an affine
transformation in which one coordinate axis remains fixed, while the other
coordinate axis is rotated counterclockwise by an angle *`theta`*. The
parameter *`axis`* determines which coordinate axis is slanted. For
*`axis`* = *"x"*, the x-axis is slanted and the y-axis remains
fixed, while for *`axis`* = *"y"* the y-axis is slanted and the
x-axis remains fixed. The slanting is performed relative to the global (i.e.,
fixed) coordinate system; this corresponds to the following chains of
transformation matrices:

$$Axis = {\'x'}: HomMat2DSInt = \begin{bmatrix} \cos(\Theta) & 0 & 0 \\ sin(\Theta) & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot .HomMat2D Axis = {\'y'}: HomMat2DSInt = \begin{bmatrix} 1 & -\sin(\Theta) & 0 \\ 0 & \cos(\Theta) & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot .HomMat2D$$ ![figure](../assets/c4eec626cc6e391d.svg)

The point (*`px`*,*`py`*) is the fixed point of the transformation,
i.e., this point remains unchanged when transformed using
*`hom_mat_2dslant`*. To obtain this behavior, first a translation is added
to the input transformation matrix that moves the fixed point onto the origin
of the global coordinate system. Then, the slant is added, and finally a
translation that moves the fixed point back to its original position. This
corresponds to the following chain of transformations for *`axis`* =
*"x"*:

$$HomMat2DSlant = \begin{bmatrix}1 & 0 & +Px \\ 0 & 1 & +Py \\ 0 & 0 & 1\end{bmatrix} \cdot \begin{bmatrix} \cos(\Theta) & 0 & 0 \\ \sin(\Theta) & 1 & 0 \\ 0 & 0 & 1\end{bmatrix} \cdot \begin{bmatrix} 1 & 0 & -Px \\ 0 & 1 & -Py \\ 0 & 0 & 1\end{bmatrix} \cdot HomMat2D$$ ![figure](../assets/64a6740150e9b052.svg)

To perform the transformation in the local coordinate system, i.e.,
the one described by *`hom_mat_2d`*, use
[`hom_mat2d_slant_local`](hom_mat2d_slant_local.md).

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

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`theta`** (input_control)  angle.rad `→` Union[float, int]

Slant angle.

Default:
0.78

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.78, 1.57, 3.14

Value range:
`0
≤
theta
≤
6.28318530718`

**`axis`** (input_control)  string `→` str

Coordinate axis that is slanted.

Default:
"x"

List of values:
"x", "y"

**`px`** (input_control)  point.x `→` Union[float, int]

Fixed point of the transformation (x coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point.y `→` Union[float, int]

Fixed point of the transformation (y coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`hom_mat_2dslant`** (output_control)  hom_mat2d `→` Sequence[float]

Output transformation matrix.

## Result

If the parameters are valid, the operator `hom_mat2d_slant` returns
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

`hom_mat2d_slant_local`

## Module

Foundation
