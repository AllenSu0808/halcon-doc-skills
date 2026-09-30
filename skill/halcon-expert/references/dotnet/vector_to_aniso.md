# VectorToAniso (Operator)

## Name

`VectorToAniso` — Approximate an anisotropic similarity transformation from point
correspondences.

## Signature

`static void HOperatorSet.VectorToAniso(HTuple px, HTuple py, HTuple qx, HTuple qy, out HTuple homMat2D)`

`void HHomMat2D.VectorToAniso(HTuple px, HTuple py, HTuple qx, HTuple qy)`

## Description

`VectorToAniso` approximates an anisotropic similarity
transformation, i.e., a transformation consisting of a rotation, a
non-uniform scaling, and a translation, from at least three point
correspondences and returns it as the homogeneous transformation
matrix *`homMat2D`*. The matrix consists of 3 components: a
scaling matrix S with non-identical
scaling in the x and y directions, a rotation matrix
R, and a translation vector
t (also see [`HomMat2dScale`](hom_mat2d_scale.md),
[`HomMat2dRotate`](hom_mat2d_rotate.md), and [`HomMat2dTranslate`](hom_mat2d_translate.md)):

$$\text{HomMat2D} = \begin{bmatrix} \mathbf{R} \cdot \mathbf{S} & \mathbf{T} \\ 0 & 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \\ 0 & 0 \end{bmatrix} \cdot \begin{bmatrix} \mathbf{R} & \mathbf{0} \\ \mathbf{0} & 1 \end{bmatrix} \cdot \begin{bmatrix} s_x & 0 & 0 \\ 0 & s_y & 0 \\ 0 & 0 & 1 \end{bmatrix} = \mathrm{H}(\mathbf{T}) \cdot \mathrm{H}(\mathbf{R}) \cdot \mathrm{H}(\mathbf{S})$$ ![figure](../assets/b7b263511bdf3472.svg)

The point correspondences are passed in the tuples
(*`px`*,*`py`*) and (*`qx`*,*`qy`*), where
corresponding points must be at the same index positions in the tuples.
The transformation is always overdetermined. Therefore, the returned
transformation is the transformation that minimizes the distances between
the original points (*`px`*,*`py`*) and the transformed points
(*`qx`*,*`qy`*), as described in the following equation (points
as homogeneous vectors):

$$\sum_{i} \bigg\|\begin{pmatrix} Q_x[i] \\ Q_y[i] \\ 1 \end{pmatrix} - \mathrm{HomMat2D} \cdot \begin{pmatrix} P_x[i] \\ P_y[i] \\ 1 \end{pmatrix}\bigg\|^2 = \text{minimum}$$ ![figure](../assets/f1be0337180510f4.svg)

*`homMat2D`* can be used directly with operators that transform data
using affine transformations, e.g., [`AffineTransImage`](affine_trans_image.md).

In an anisotropic similarity transformation, as defined above, the points
are first scaled and then rotated. Sometimes, a transformation in which
the points are first rotated and then scaled is useful. This kind of
transformation can be computed with `VectorToAniso` by passing
the point correspondences in the opposite order, i.e., the points
(*`px`*,*`py`*) are passed in the parameters
(*`qx`*,*`qy`*) and vice versa. The resulting transformation
must then be inverted with [`HomMat2dInvert`](hom_mat2d_invert.md).

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

Furthermore, it should be noted that if a homogeneous transformation
matrix is used to transform images, regions, XLD contours, or any
other data that has been extracted from images, it is assumed that
the origin of the coordinate system of the homogeneous
transformation matrix lies in the upper left corner of a pixel. The
image processing operators that return point coordinates, however,
assume a coordinate system in which the origin lies in the center of
a pixel. Therefore, to obtain a consistent homogeneous
transformation matrix, 0.5 must be added to the point coordinates
before computing the transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`px`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the original points.

**`py`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the original points.

**`qx`** (input_control)  point.x-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the transformed points.

**`qy`** (input_control)  point.y-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the transformed points.

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Possible Successors

`HomMat2dInvert`,
`AffineTransImage`,
`AffineTransImageSize`,
`AffineTransRegion`,
`AffineTransContourXld`,
`AffineTransPolygonXld`,
`AffineTransPoint2d`

## Alternatives

`VectorToHomMat2d`,
`VectorToSimilarity`,
`VectorToRigid`

## See also

`VectorFieldToHomMat2d`,
`PointLineToHomMat2d`

## Module

Foundation
