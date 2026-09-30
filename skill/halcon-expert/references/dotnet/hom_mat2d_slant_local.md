# HomMat2dSlantLocal (Operator)

## Name

`HomMat2dSlantLocal` — Add a slant to a homogeneous 2D transformation matrix.

## Signature

`static void HOperatorSet.HomMat2dSlantLocal(HTuple homMat2D, HTuple theta, HTuple axis, out HTuple homMat2DSlant)`

`HHomMat2D HHomMat2D.HomMat2dSlantLocal(HTuple theta, string axis)`

`HHomMat2D HHomMat2D.HomMat2dSlantLocal(double theta, string axis)`

## Description

`HomMat2dSlantLocal` adds a slant by the angle *`theta`* to the
homogeneous 2D transformation matrix *`homMat2D`* and returns the
resulting matrix in *`homMat2DSlant`*. A slant is an affine
transformation in which one coordinate axis remains fixed, while the other
coordinate axis is rotated counterclockwise by an angle *`theta`*. The
parameter *`axis`* determines which coordinate axis is slanted. For
*`axis`* = *"x"*, the x-axis is slanted and the y-axis remains
fixed, while for *`axis`* = *"y"* the y-axis is slanted and the
x-axis remains fixed. In contrast to
[`HomMat2dSlant`](hom_mat2d_slant.md), the slanting is performed
relative to the local coordinate system, i.e., the coordinate system
described by *`homMat2D`*; this corresponds to the following chains of
transformation matrices:

$$Axis = \,'x\':\, \mathrm{HomMat2DSlant=HomMat2D}\cdot\begin{bmatrix}\cos(\Theta)&0&0\\[6pt]\sin(\Theta)&1&0\\[6pt]0&0&1\end{bmatrix} Axis = \'y\':\, \mathrm{HomMat2DSlant=HomMat2D}\cdot\begin{bmatrix}1&-\sin(\Theta)&0\\[6pt]0&\cos(\Theta)&0\\[6pt]0&0&1\end{bmatrix}$$ ![figure](../assets/b80db120851b9732.svg)

The fixed point of the transformation is the origin of the local
coordinate system, i.e., this point remains unchanged when
transformed using *`homMat2DSlant`*.

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

**`theta`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

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

**`axis`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Coordinate axis that is slanted.

Default:
"x"

List of values:
"x", "y"

**`homMat2DSlant`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

If the parameters are valid, the operator
`HomMat2dSlantLocal` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`HomMat2dIdentity`,
`HomMat2dTranslateLocal`,
`HomMat2dScaleLocal`,
`HomMat2dRotateLocal`,
`HomMat2dSlantLocal`,
`HomMat2dReflect`

## Possible Successors

`HomMat2dTranslateLocal`,
`HomMat2dScaleLocal`,
`HomMat2dRotateLocal`,
`HomMat2dSlantLocal`,
`HomMat2dReflectLocal`

## See also

`HomMat2dSlant`

## Module

Foundation
