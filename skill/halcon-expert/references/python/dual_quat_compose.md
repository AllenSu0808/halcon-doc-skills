# dual_quat_compose (Operator)

## Name

`dual_quat_compose` — Multiply two dual quaternions.

## Signature

`def dual_quat_compose(dual_quaternion_left: Sequence[float], dual_quaternion_right: Sequence[float]) -> Sequence[float]`

## Description

The operator `dual_quat_compose` multiplies the two dual quaternions
*`dual_quaternion_left`* and *`dual_quaternion_right`* and returns the
product in *`dual_quaternion_composed`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

The multiplication of the dual quaternions $\hat{p}$ ![figure](../assets/c802e896b3d639bf.svg) and
$\hat{q}$ ![figure](../assets/2e9ecba020103681.svg) is $\hat{p}\hat{q} = p_r q_r + \epsilon(p_r q_d + p_d q_r)$ ![figure](../assets/05b34277bfdd45a7.svg).

For the multiplication of quaternions see [`quat_compose`](quat_compose.md).

Note that the multiplication of two dual quaternions is not commutative,
i.e., $\hat{p}\hat{q} \neq \hat{q}\hat{p}$ ![figure](../assets/1cb2b8f39d3a0a80.svg).

If *`dual_quaternion_left`* and *`dual_quaternion_right`* are unit
dual quaternions and, hence, represent 3D rigid transformations, their
multiplication corresponds to the multiplication of their corresponding
homogeneous transformation matrices. Consequently, `dual_quat_compose`
can be used to concatenate two 3D rigid transformations analogously to
[`pose_compose`](pose_compose.md) or [`hom_mat3d_compose`](hom_mat3d_compose.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dual_quaternion_left`** (input_control)  dual_quaternion(-array) `→` Sequence[float]

Left dual quaternion.

**`dual_quaternion_right`** (input_control)  dual_quaternion(-array) `→` Sequence[float]

Right dual quaternion.

**`dual_quaternion_composed`** (output_control)  dual_quaternion(-array) `→` Sequence[float]

Product of the dual quaternions.

## Possible Predecessors

`screw_to_dual_quat`

## Possible Successors

`dual_quat_to_hom_mat3d`,
`dual_quat_to_pose`,
`dual_quat_to_screw`

## Alternatives

`pose_compose`,
`hom_mat3d_compose`

## See also

`dual_quat_interpolate`,
`pose_to_dual_quat`,
`dual_quat_normalize`,
`dual_quat_conjugate`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`quat_compose`

## Module

Foundation
