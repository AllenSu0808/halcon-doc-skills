# vector_to_hom_mat3d (Operator)

## Name

`vector_to_hom_mat3d` — Approximate a 3D transformation from point correspondences.

## Signature

`vector_to_hom_mat3d( : : TransformationType, Px, Py, Pz, Qx, Qy, Qz : HomMat3D)`

## Description

`vector_to_hom_mat3d` approximates an affine or projective 3D
transformation from point correspondences and returns it as the
homogeneous transformation matrix *`HomMat3D`*.

The type of the 3D transformation to compute is specified with
*`TransformationType`*. For *`TransformationType`* =
*'rigid'*, a rigid 3D transformation (a rotation and a
translation), for *`TransformationType`* =
*'similarity'*, a 3D similarity transformation (a uniform
scaling, a rotation, and a translation), for
*`TransformationType`* = *'affine'* a general affine
3D transformation, and for *`TransformationType`* =
*'projective'* a projective 3D transformation is computed.

The minimum required number of point correspondences is 3 for
*`TransformationType`* = *'rigid'*, 3 for
*`TransformationType`* = *'similarity'*, 4 for
*`TransformationType`* = *'affine'*, and 5 for
*`TransformationType`* = *'projective'*.

The point correspondences are passed in the tuples
(*`Px`*,*`Py`*,*`Pz`*) and
(*`Qx`*,*`Qy`*,*`Qz`*), where corresponding points
must be at the same index positions in the tuples. If more than the
minimum number of point correspondences are passed, the
transformation is overdetermined. In this case, the returned
transformation is the transformation that minimizes the distances
between the transformed input points
(*`Px`*,*`Py`*,*`Pz`*) and the points
(*`Qx`*,*`Qy`*,*`Qz`*), as described in the following
equation (points as homogeneous vectors):

$$\sum_i \left| \begin{pmatrix} Q_x[i] \\ Q_y[i] \\ Q_z[i] \\ 1 \end{pmatrix} \right| - \mathrm{HomMat3D} \cdot \begin{pmatrix} P_x[i] \\ P_y[i] \\ P_z[i] \\ 1 \end{pmatrix}|^2 = \minimize$$ ![figure](../assets/a5aa51a9bccf4de1.svg)

*`HomMat3D`* can be used directly with operators that transform
3D data using affine transformations, e.g.,
[`affine_trans_point_3d`](affine_trans_point_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`TransformationType`** (input_control)  string `→`  (string)

Type of the transformation to compute.

Default:
'rigid'

List of values:
'affine', 'projective', 'rigid', 'similarity'

**`Px`** (input_control)  point3d.x-array `→`  (real)

X coordinates of the original points.

**`Py`** (input_control)  point3d.y-array `→`  (real)

Y coordinates of the original points.

**`Pz`** (input_control)  point3d.z-array `→`  (real)

Z coordinates of the original points.

**`Qx`** (input_control)  point3d.x-array `→`  (real)

X coordinates of the transformed points.

**`Qy`** (input_control)  point3d.x-array `→`  (real)

Y coordinates of the transformed points.

**`Qz`** (input_control)  point3d.z-array `→`  (real)

Z coordinates of the transformed points.

**`HomMat3D`** (output_control)  hom_mat3d `→`  (real)

Output transformation matrix.

## Possible Successors

`hom_mat3d_to_pose`,
`affine_trans_point_3d`

## See also

`point_pluecker_line_to_hom_mat3d`

## Module

Foundation
