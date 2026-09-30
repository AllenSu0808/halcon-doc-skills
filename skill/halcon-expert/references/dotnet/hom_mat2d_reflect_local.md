# HomMat2dReflectLocal (Operator)

## Name

`HomMat2dReflectLocal` — Add a reflection to a homogeneous 2D transformation matrix.

## Signature

`static void HOperatorSet.HomMat2dReflectLocal(HTuple homMat2D, HTuple px, HTuple py, out HTuple homMat2DReflect)`

`HHomMat2D HHomMat2D.HomMat2dReflectLocal(HTuple px, HTuple py)`

`HHomMat2D HHomMat2D.HomMat2dReflectLocal(double px, double py)`

## Description

`HomMat2dReflectLocal` adds a reflection about the axis given by
the two points (0,0) and (*`px`*,*`py`*) to the homogeneous 2D
transformation matrix *`homMat2D`* and returns the resulting matrix
in *`homMat2DReflect`*. The reflection is described by a
2×2 reflection matrix M.
In contrast to [`HomMat2dReflect`](hom_mat2d_reflect.md), it is performed relative to the
local coordinate system, i.e., the coordinate system described by
*`homMat2D`*; this corresponds to the following chain of
transformation matrices:

$$HomMat2DReflect = \begin{bmatrix} M & 0 \\ 0 & 1 \end{bmatrix} \cdot HomMat2D \\quad M = I - \frac{2}{v^{T} v}\, v v^{T}$$ ![figure](../assets/f60d5ca94b91a78a.svg)
where v = (-*`py`*,*`px`*)^T is the normal vector to the axis.

The axis (0,0)-(*`px`*,*`py`*) is fixed in the transformation,
i.e., the points on the axis remain unchanged when transformed using
*`homMat2DReflect`*.

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

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`px`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Point that defines the axis (x coordinate).

Default:
16

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Point that defines the axis (y coordinate).

Default:
32

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`homMat2DReflect`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

`HomMat2dReflectLocal` returns 2 (
H_MSG_TRUE)
if the point
(*`px`*,*`py`*) is not (0,0). If necessary, an exception
is raised.

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

`HomMat2dReflect`

## Module

Foundation
