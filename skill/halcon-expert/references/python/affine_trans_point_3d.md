# affine_trans_point_3d (Operator)

## Name

`affine_trans_point_3d` — Apply an arbitrary affine 3D transformation to points.

## Signature

`def affine_trans_point_3d(hom_mat_3d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def affine_trans_point_3d_s(hom_mat_3d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]]) -> Tuple[float, float, float]`

## Description

`affine_trans_point_3d` applies an arbitrary affine 3D transformation,
i.e., scaling, rotation, and translation, to the input points
(*`px`*,*`py`*,*`pz`*) and returns the resulting points in
(*`qx`*, *`qy`*,*`qz`*). The affine transformation is
described by the homogeneous transformation matrix given in
*`hom_mat_3d`*. This corresponds to the following equation (input and
output points as homogeneous vectors):

$$\begin{pmatrix}Q_x\\Q_y\\Q_z\\1\end{pmatrix} = \mathrm{HomMat3D} \cdot \begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix}$$ ![figure](../assets/1a543a153c82d08b.svg)

The transformation matrix can be created using the operators
[`hom_mat3d_identity`](hom_mat3d_identity.md), [`hom_mat3d_scale`](hom_mat3d_scale.md),
[`hom_mat3d_rotate`](hom_mat3d_rotate.md), [`hom_mat3d_translate`](hom_mat3d_translate.md), etc., or be the result
of [`pose_to_hom_mat3d`](pose_to_hom_mat3d.md).

For example, if *`hom_mat_3d`* corresponds to a rigid transformation,
i.e., if it consists of a rotation and a translation, the
points are transformed as follows:

$$\begin{pmatrix}Q_x\\Q_y\\Q_z\\1\end{pmatrix} = \begin{bmatrix}R & T\\0 & 1\end{bmatrix} \cdot \begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix} = (R\cdot \begin{pmatrix}P_x\\P_y\\P_z\end{pmatrix}+T)$$ ![figure](../assets/689e51e41e8b66c0.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Input transformation matrix.

**`px`** (input_control)  point3d.x(-array) `→` MaybeSequence[Union[float, int]]

Input point(s) (x coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point3d.y(-array) `→` MaybeSequence[Union[float, int]]

Input point(s) (y coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`pz`** (input_control)  point3d.z(-array) `→` MaybeSequence[Union[float, int]]

Input point(s) (z coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`qx`** (output_control)  point3d.x(-array) `→` Sequence[float]

Output point(s) (x coordinate).

**`qy`** (output_control)  point3d.y(-array) `→` Sequence[float]

Output point(s) (y coordinate).

**`qz`** (output_control)  point3d.z(-array) `→` Sequence[float]

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
