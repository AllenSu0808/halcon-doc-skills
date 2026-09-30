# hom_mat2d_translate_local (Operator)

## Name

`hom_mat2d_translate_local` — Add a translation to a homogeneous 2D transformation matrix.

## Signature

`hom_mat2d_translate_local( : : HomMat2D, Tx, Ty : HomMat2DTranslate)`

## Description

`hom_mat2d_translate_local` adds a translation by the vector
t = (*`Tx`*,*`Ty`*) to the
homogeneous 2D transformation matrix *`HomMat2D`* and returns the
resulting matrix in *`HomMat2DTranslate`*. In contrast to
[`hom_mat2d_translate`](hom_mat2d_translate.md), the translation is performed relative to the
local coordinate system, i.e., the coordinate system described by
*`HomMat2D`*; this corresponds to the following chain of transformation
matrices:

$$HomMat2DTranslate = HomMat2D · \begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1\end{bmatrix}^{T} T = \begin{pmatrix}T_x \\ T_y\end{pmatrix}$$ ![figure](../assets/99004a9d233882f9.svg)

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

**`Tx`** (input_control)  point.x `→`  (real / integer)

Translation along the x-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Ty`** (input_control)  point.y `→`  (real / integer)

Translation along the y-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`HomMat2DTranslate`** (output_control)  hom_mat2d `→`  (real)

Output transformation matrix.

## Result

If the parameters are valid, the operator
`hom_mat2d_translate_local` returns 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

## Possible Predecessors

`hom_mat2d_identity`,
`hom_mat2d_translate_local`,
`hom_mat2d_scale_local`,
`hom_mat2d_rotate_local`,
`hom_mat2d_slant_local`,
`hom_mat2d_reflect_local`

## Possible Successors

`hom_mat2d_translate_local`,
`hom_mat2d_scale_local`,
`hom_mat2d_rotate_local`,
`hom_mat2d_slant_local`,
`hom_mat2d_reflect_local`

## See also

`hom_mat2d_translate`

## Module

Foundation
