# hom_mat2d_scale_local (Operator)

## Name

`hom_mat2d_scale_local` — Add a scaling to a homogeneous 2D transformation matrix.

## Signature

`def hom_mat2d_scale_local(hom_mat_2d: Sequence[float], sx: Union[float, int], sy: Union[float, int]) -> Sequence[float]`

## Description

`hom_mat2d_scale_local` adds a scaling by the scale factors *`sx`*
and *`sy`* to the homogeneous 2D transformation matrix *`hom_mat_2d`*
and returns the resulting matrix in *`hom_mat_2dscale`*. The scaling is
described by a 2×2 scaling matrix
S. In contrast to [`hom_mat2d_scale`](hom_mat2d_scale.md), it is
performed relative to the local coordinate system, i.e., the coordinate
system described by *`hom_mat_2d`*; this corresponds to the following
chain of transformation matrices:

$$HomMat2DScale = HomMat2D \cdot \begin{bmatrix} S & 0 \\ 0 & 1 \end{bmatrix} \\ S = \begin{bmatrix} Sx & 0 \\ 0 & Sy \end{bmatrix}$$ ![figure](../assets/a4243a538c97d7ed.svg)

The fixed point of the transformation is the origin of the local
coordinate system, i.e., this point remains unchanged when
transformed using *`hom_mat_2dscale`*.

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
$$\begin{bmatrix} ra & rb & tc \\ rd & re & tf \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/dd4c7548e15a2db4.svg)
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

**`sx`** (input_control)  number `→` Union[float, int]

Scale factor along the x-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 16

Restriction:
`Sx != 0`

**`sy`** (input_control)  number `→` Union[float, int]

Scale factor along the y-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 16

Restriction:
`Sy != 0`

**`hom_mat_2dscale`** (output_control)  hom_mat2d `→` Sequence[float]

Output transformation matrix.

## Result

`hom_mat2d_scale_local` returns 2 (
H_MSG_TRUE)
if both scale factors are not
0. If necessary, an exception is raised.

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

`hom_mat2d_scale`

## Module

Foundation
