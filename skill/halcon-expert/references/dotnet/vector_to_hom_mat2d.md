# VectorToHomMat2d (Operator)

## Name

`VectorToHomMat2d` — Approximate an affine transformation from point correspondences.

## Signature

`static void HOperatorSet.VectorToHomMat2d(HTuple px, HTuple py, HTuple qx, HTuple qy, out HTuple homMat2D)`

`void HHomMat2D.VectorToHomMat2d(HTuple px, HTuple py, HTuple qx, HTuple qy)`

## Description

`VectorToHomMat2d` approximates an affine transformation from at
least three point correspondences and returns it as the homogeneous
transformation matrix *`homMat2D`* (see
[`HomMat2dToAffinePar`](hom_mat2d_to_affine_par.md) for the content of the homogeneous
transformation matrix).

The point correspondences are passed in the tuples
(*`px`*,*`py`*) and (*`qx`*,*`qy`*),
where corresponding points must be at the same index positions in the tuples.
If more than three point correspondences are passed, the transformation is
overdetermined. In this case, the returned transformation is the
transformation that minimizes the distances between the input points
(*`px`*,*`py`*) and the transformed points
(*`qx`*,*`qy`*), as described in the following equation
(points as homogeneous vectors):

$$\sum_{i} \bigg\|\begin{pmatrix} Q_x[i] \\ Q_y[i] \\ 1 \end{pmatrix} - \mathrm{HomMat2D} \cdot \begin{pmatrix} P_x[i] \\ P_y[i] \\ 1 \end{pmatrix}\bigg\|^2 = \text{minimum}$$ ![figure](../assets/f1be0337180510f4.svg)

*`homMat2D`* can be used directly with operators that transform data
using affine transformations, e.g., [`AffineTransImage`](affine_trans_image.md).

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

`AffineTransImage`,
`AffineTransImageSize`,
`AffineTransRegion`,
`AffineTransContourXld`,
`AffineTransPolygonXld`,
`AffineTransPoint2d`

## Alternatives

`VectorToAniso`,
`VectorToSimilarity`,
`VectorToRigid`

## See also

`VectorFieldToHomMat2d`,
`PointLineToHomMat2d`

## Module

Foundation
