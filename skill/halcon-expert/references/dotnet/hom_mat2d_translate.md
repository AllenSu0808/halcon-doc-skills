# HomMat2dTranslate (Operator)

## Name

`HomMat2dTranslate` — Add a translation to a homogeneous 2D transformation matrix.

## Signature

`static void HOperatorSet.HomMat2dTranslate(HTuple homMat2D, HTuple tx, HTuple ty, out HTuple homMat2DTranslate)`

`HHomMat2D HHomMat2D.HomMat2dTranslate(HTuple tx, HTuple ty)`

`HHomMat2D HHomMat2D.HomMat2dTranslate(double tx, double ty)`

## Description

`HomMat2dTranslate` adds a translation by the vector
t = (*`tx`*,*`ty`*) to the
homogeneous 2D transformation matrix *`homMat2D`* and returns the
resulting matrix in *`homMat2DTranslate`*. The translation is performed
relative to the global (i.e., fixed) coordinate system; this corresponds to
the following chain of transformation matrices:

$$\mathrm{HomMat2DTranslate} = \left[\begin{array}{ccc}1 & 0 & T\_x\\0 & 1 & T\_y\\0 & 0 & 1\end{array}\right] \cdot \mathrm{HomMat2D} \\ T = \left(\begin{array}{c}T\_x\\T\_y\end{array}\right)$$ ![figure](../assets/8b20dcfe94920eae.svg)

To perform the transformation in the local coordinate system, i.e.,
the one described by *`homMat2D`*, use
[`HomMat2dTranslateLocal`](hom_mat2d_translate_local.md).

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

**`tx`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Translation along the x-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`ty`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Translation along the y-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`homMat2DTranslate`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

If the parameters are valid, the operator `HomMat2dTranslate` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`HomMat2dIdentity`,
`HomMat2dTranslate`,
`HomMat2dScale`,
`HomMat2dRotate`,
`HomMat2dSlant`,
`HomMat2dReflect`

## Possible Successors

`HomMat2dTranslate`,
`HomMat2dScale`,
`HomMat2dRotate`,
`HomMat2dSlant`,
`HomMat2dReflect`

## See also

`HomMat2dTranslateLocal`

## Module

Foundation
