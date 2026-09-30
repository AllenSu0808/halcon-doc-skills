# VectorToHomMat3d (Operator)

## Name

`VectorToHomMat3d` — Approximate a 3D transformation from point correspondences.

## Signature

`static void HOperatorSet.VectorToHomMat3d(HTuple transformationType, HTuple px, HTuple py, HTuple pz, HTuple qx, HTuple qy, HTuple qz, out HTuple homMat3D)`

`void HHomMat3D.VectorToHomMat3d(string transformationType, HTuple px, HTuple py, HTuple pz, HTuple qx, HTuple qy, HTuple qz)`

## Description

`VectorToHomMat3d` approximates an affine or projective 3D
transformation from point correspondences and returns it as the
homogeneous transformation matrix *`homMat3D`*.

The type of the 3D transformation to compute is specified with
*`transformationType`*. For *`transformationType`* =
*"rigid"*, a rigid 3D transformation (a rotation and a
translation), for *`transformationType`* =
*"similarity"*, a 3D similarity transformation (a uniform
scaling, a rotation, and a translation), for
*`transformationType`* = *"affine"* a general affine
3D transformation, and for *`transformationType`* =
*"projective"* a projective 3D transformation is computed.

The minimum required number of point correspondences is 3 for
*`transformationType`* = *"rigid"*, 3 for
*`transformationType`* = *"similarity"*, 4 for
*`transformationType`* = *"affine"*, and 5 for
*`transformationType`* = *"projective"*.

The point correspondences are passed in the tuples
(*`px`*,*`py`*,*`pz`*) and
(*`qx`*,*`qy`*,*`qz`*), where corresponding points
must be at the same index positions in the tuples. If more than the
minimum number of point correspondences are passed, the
transformation is overdetermined. In this case, the returned
transformation is the transformation that minimizes the distances
between the transformed input points
(*`px`*,*`py`*,*`pz`*) and the points
(*`qx`*,*`qy`*,*`qz`*), as described in the following
equation (points as homogeneous vectors):

$$\sum_i \left| \begin{pmatrix} Q_x[i] \\ Q_y[i] \\ Q_z[i] \\ 1 \end{pmatrix} \right| - \mathrm{HomMat3D} \cdot \begin{pmatrix} P_x[i] \\ P_y[i] \\ P_z[i] \\ 1 \end{pmatrix}|^2 = \minimize$$ ![figure](../assets/a5aa51a9bccf4de1.svg)

*`homMat3D`* can be used directly with operators that transform
3D data using affine transformations, e.g.,
[`AffineTransPoint3d`](affine_trans_point_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`transformationType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the transformation to compute.

Default:
"rigid"

List of values:
"affine", "projective", "rigid", "similarity"

**`px`** (input_control)  point3d.x-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the original points.

**`py`** (input_control)  point3d.y-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the original points.

**`pz`** (input_control)  point3d.z-array `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the original points.

**`qx`** (input_control)  point3d.x-array `→` [HTuple](HTuple.md) (*double*)

X coordinates of the transformed points.

**`qy`** (input_control)  point3d.x-array `→` [HTuple](HTuple.md) (*double*)

Y coordinates of the transformed points.

**`qz`** (input_control)  point3d.z-array `→` [HTuple](HTuple.md) (*double*)

Z coordinates of the transformed points.

**`homMat3D`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Possible Successors

`HomMat3dToPose`,
`AffineTransPoint3d`

## See also

`PointPlueckerLineToHomMat3d`

## Module

Foundation
