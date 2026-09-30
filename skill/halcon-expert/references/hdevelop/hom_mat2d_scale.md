# hom_mat2d_scale (Operator)

## Name

`hom_mat2d_scale` — Add a scaling to a homogeneous 2D transformation matrix.

## Signature

`hom_mat2d_scale( : : HomMat2D, Sx, Sy, Px, Py : HomMat2DScale)`

## Description

`hom_mat2d_scale` adds a scaling by the scale factors *`Sx`* and
*`Sy`* to the homogeneous 2D transformation matrix *`HomMat2D`* and
returns the resulting matrix in *`HomMat2DScale`*. The scaling is
described by a 2×2 scaling matrix
S. It is performed relative to the global
(i.e., fixed) coordinate system; this corresponds to the following chain of
transformation matrices:

$$HomMat2DScale = \begin{bmatrix} S & 0 \\ 0 & 1 \end{bmatrix} \cdot HomMat2D \, S = \begin{bmatrix} Sx & 0 \\ 0 & Sy \end{bmatrix}$$ ![figure](../assets/14ceb41434a2a1ce.svg)

The point (*`Px`*,*`Py`*) is the fixed point of the transformation,
i.e., this point remains unchanged when transformed using
*`HomMat2DScale`*. To obtain this behavior, first a translation is added
to the input transformation matrix that moves the fixed point onto the origin
of the global coordinate system. Then, the scaling is added, and finally a
translation that moves the fixed point back to its original position. This
corresponds to the following chain of transformations:

$$\text{HomMat2DScale} = \begin{bmatrix}1 & 0 & +Px \\ 0 & 1 & +Py \\ 0 & 0 & 1\end{bmatrix} \cdot \mathbf{S} \cdot \begin{bmatrix}1 & 0 & -Px \\ 0 & 1 & -Py \\ 0 & 0 & 1\end{bmatrix} \cdot \text{HomMat2D$$ ![figure](../assets/74f0cd3d4a694edc.svg)

To perform the transformation in the local coordinate system, i.e.,
the one described by *`HomMat2D`*, use
[`hom_mat2d_scale_local`](hom_mat2d_scale_local.md).

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

**`Sx`** (input_control)  number `→`  (real / integer)

Scale factor along the x-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 16

Restriction:
`Sx != 0`

**`Sy`** (input_control)  number `→`  (real / integer)

Scale factor along the y-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 16

Restriction:
`Sy != 0`

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

**`HomMat2DScale`** (output_control)  hom_mat2d `→`  (real)

Output transformation matrix.

## Result

`hom_mat2d_scale` returns 2 (
H_MSG_TRUE)
if both scale factors are not
0. If necessary, an exception is raised.

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

`hom_mat2d_scale_local`

## Module

Foundation
