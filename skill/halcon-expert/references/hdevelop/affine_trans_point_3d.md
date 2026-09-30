# affine_trans_point_3d (Operator)

## Name

`affine_trans_point_3d` — Apply an arbitrary affine 3D transformation to points.

## Signature

`affine_trans_point_3d( : : HomMat3D, Px, Py, Pz : Qx, Qy, Qz)`

## Description

`affine_trans_point_3d` applies an arbitrary affine 3D transformation,
i.e., scaling, rotation, and translation, to the input points
(*`Px`*,*`Py`*,*`Pz`*) and returns the resulting points in
(*`Qx`*, *`Qy`*,*`Qz`*). The affine transformation is
described by the homogeneous transformation matrix given in
*`HomMat3D`*. This corresponds to the following equation (input and
output points as homogeneous vectors):

$$\begin{pmatrix}Q_x\\Q_y\\Q_z\\1\end{pmatrix} = \mathrm{HomMat3D} \cdot \begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix}$$ ![figure](../assets/1a543a153c82d08b.svg)

The transformation matrix can be created using the operators
[`hom_mat3d_identity`](hom_mat3d_identity.md), [`hom_mat3d_scale`](hom_mat3d_scale.md),
[`hom_mat3d_rotate`](hom_mat3d_rotate.md), [`hom_mat3d_translate`](hom_mat3d_translate.md), etc., or be the result
of [`pose_to_hom_mat3d`](pose_to_hom_mat3d.md).

For example, if *`HomMat3D`* corresponds to a rigid transformation,
i.e., if it consists of a rotation and a translation, the
points are transformed as follows:

$$\begin{pmatrix}Q_x\\Q_y\\Q_z\\1\end{pmatrix} = \begin{bmatrix}R & T\\0 & 1\end{bmatrix} \cdot \begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix} = (R\cdot \begin{pmatrix}P_x\\P_y\\P_z\end{pmatrix}+T)$$ ![figure](../assets/689e51e41e8b66c0.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`HomMat3D`** (input_control)  hom_mat3d `→`  (real)

Input transformation matrix.

**`Px`** (input_control)  point3d.x(-array) `→`  (real / integer)

Input point(s) (x coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Py`** (input_control)  point3d.y(-array) `→`  (real / integer)

Input point(s) (y coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Pz`** (input_control)  point3d.z(-array) `→`  (real / integer)

Input point(s) (z coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Qx`** (output_control)  point3d.x(-array) `→`  (real)

Output point(s) (x coordinate).

**`Qy`** (output_control)  point3d.y(-array) `→`  (real)

Output point(s) (y coordinate).

**`Qz`** (output_control)  point3d.z(-array) `→`  (real)

Output point(s) (z coordinate).

## Result

If the parameters are valid, the operator `affine_trans_point_3d`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`hom_mat3d_translate`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate`,
`hom_mat3d_rotate_local`

## Possible Successors

`hom_mat3d_translate`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate`,
`hom_mat3d_rotate_local`

## Module

Foundation
