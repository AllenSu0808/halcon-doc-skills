# hom_mat2d_reflect (Operator)

## Name

`hom_mat2d_reflect` — Add a reflection to a homogeneous 2D transformation matrix.

## Signature

`def hom_mat2d_reflect(hom_mat_2d: Sequence[float], px: Union[float, int], py: Union[float, int], qx: Union[float, int], qy: Union[float, int]) -> Sequence[float]`

## Description

`hom_mat2d_reflect` adds a reflection about the axis given by the
two points (*`px`*,*`py`*) and (*`qx`*,*`qy`*) to the
homogeneous 2D transformation matrix *`hom_mat_2d`* and returns the
resulting matrix in *`hom_mat_2dreflect`*. The reflection is described
by a 2×2 reflection matrix M.
It is performed relative to the global (i.e., fixed) coordinate system;
this corresponds to the following chain of transformation matrices:

$$HomMat2DReflect = \begin{bmatrix} M & 0 \\ 0 & 1 \end{bmatrix} \cdot HomMat2D \\quad M = I - \frac{2}{v^{T} v}\, v v^{T}$$ ![figure](../assets/f60d5ca94b91a78a.svg)
where v = (*`py`*-*`qy`*,*`qx`*-*`px`*)^T is the
normal vector to the axis.

The axis (*`px`*,*`py`*)-(*`qx`*,*`qy`*) is fixed in
the transformation, i.e., the points on the axis remain unchanged when
transformed using *`hom_mat_2dreflect`*. To obtain this behavior, first
a translation is added to the input transformation matrix that moves the
axis onto the origin of the global coordinate system. Then, the reflection
is added, and finally a translation that moves the axis back to its original
position. This corresponds to the following chain of transformations:

$$\mathrm{HomMat2DReflect = \begin{bmatrix} 1 & 0 & +P_x \\ 0 & 1 & +P_y \\ 0 & 0 & 1 \ \end{bmatrix} \cdot \begin{bmatrix} M \\ 0 \\ 0 \end{bmatrix} \cdot \begin{bmatrix} 1 & 0 & -P_x \\ 0 & 1 & -P_y \\ 0 & 0 & 1 \ \end{bmatrix} \,\mathrm{HomMat2D}$$ ![figure](../assets/069041be6e804b00.svg)

To perform the transformation in the local coordinate system, i.e.,
the one described by *`hom_mat_2d`*, use
[`hom_mat2d_reflect_local`](hom_mat2d_reflect_local.md).

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
possible to process full $\text{3}\times\text{3}$ matrices, which represent
a projective 2D transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`px`** (input_control)  point.x `→` Union[float, int]

First point of the axis (x coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point.y `→` Union[float, int]

First point of the axis (y coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`qx`** (input_control)  point.x `→` Union[float, int]

Second point of the axis (x coordinate).

Default:
16

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`qy`** (input_control)  point.y `→` Union[float, int]

Second point of the axis (y coordinate).

Default:
32

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`hom_mat_2dreflect`** (output_control)  hom_mat2d `→` Sequence[float]

Output transformation matrix.

## Result

`hom_mat2d_reflect` returns 2 (
H_MSG_TRUE)
if both points on the axis are not
identical. If necessary, an exception is raised.

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

`hom_mat2d_reflect_local`

## Module

Foundation
