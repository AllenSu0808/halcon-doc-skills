# dual_quat_conjugate (Operator)

## Name

`dual_quat_conjugate` — Conjugate a dual quaternion.

## Signature

`def dual_quat_conjugate(dual_quaternion: Sequence[float]) -> Sequence[float]`

## Description

The operator `dual_quat_conjugate` computes the conjugation
*`dual_quaternion_conjugate`* of the input dual quaternion
*`dual_quaternion`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

The conjugation of a dual quaternion
$\hat{q} = q_r + \varepsilon q_d$ ![figure](../assets/58fb67719e5d2ee1.svg) is given by $\hat{q} = \hat{q}_r + \varepsilon \hat{q}_d$ ![figure](../assets/949ad0fe69b08a79.svg), where
$\overline{q_r}$ ![figure](../assets/29e5391379772ce9.svg) and $\overline{q}_{d}$ ![figure](../assets/f62a8d44de961627.svg)
are the conjugations of the quaternions $q_{r}$ and
$q_{d}$.

For the conjugation of quaternions see [`quat_conjugate`](quat_conjugate.md).

If *`dual_quaternion`* is a unit dual quaternion and, hence, represents
a 3D rigid transformation, its inverse is its conjugate, i.e.,
$\hat{q}^{-1} = \hat{q}$ ![figure](../assets/af4670436ac2570b.svg). Consequently,
*`dual_quaternion_conjugate`* represents the inverse 3D rigid
transformation of *`dual_quaternion`*. Therefore,
`dual_quat_conjugate` can be used to invert a 3D rigid transformation
analogously to [`pose_invert`](pose_invert.md) or [`hom_mat3d_invert`](hom_mat3d_invert.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dual_quaternion`** (input_control)  dual_quaternion(-array) `→` Sequence[float]

Dual quaternion.

**`dual_quaternion_conjugate`** (output_control)  dual_quaternion(-array) `→` Sequence[float]

Conjugate of the dual quaternion.

## Possible Predecessors

`dual_quat_compose`,
`pose_to_dual_quat`,
`screw_to_dual_quat`

## Possible Successors

`dual_quat_compose`,
`dual_quat_to_hom_mat3d`,
`dual_quat_to_screw`,
`dual_quat_interpolate`,
`dual_quat_to_pose`

## Alternatives

`pose_invert`,
`hom_mat3d_invert`

## See also

`dual_quat_normalize`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`quat_conjugate`

## Module

Foundation
