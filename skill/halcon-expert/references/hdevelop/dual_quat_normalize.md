# dual_quat_normalize (Operator)

## Name

`dual_quat_normalize` — Normalize a dual quaternion.

## Signature

`dual_quat_normalize( : : DualQuaternion : DualQuaternionNormalized)`

## Description

The operator `dual_quat_normalize` normalizes the input dual
quaternion *`DualQuaternion`* and returns the normalized dual
quaternion, which is also called a unit dual quaternion,
in *`DualQuaternionNormalized`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

The norm of a unit dual quaternion
$\hat{q} = q_r + \varepsilon q_d$ ![figure](../assets/58fb67719e5d2ee1.svg)
is 1, i.e., $\hat{q}\hat{q}=1$ ![figure](../assets/d8667844b46f184e.svg). This is
equivalent to the following two conditions:
$$\|q_r\|\, = \\bar{q}_r \\bar{q}_r = 1 \\\nq_r \bar{q}_d + \bar{q}_r q_d = 0$$ ![figure](../assets/a011c9e8e1545972.svg)
where $\overline{q}$ ![figure](../assets/c62a28b14aa80af0.svg) represents the conjugate quaternion of
$q$ (see [`quat_conjugate`](quat_conjugate.md)).

A 3D rigid transformation can be represented by a unit dual quaternion.

## Attention

If the norm of the real part of *`DualQuaternion`* is 0,
`dual_quat_normalize` returns the error code 9310 (H_ERR_DQ_ZERO_NORM)
because in this case no normalization is possible.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DualQuaternion`** (input_control)  dual_quaternion(-array) `→`  (real)

Unit dual quaternion.

**`DualQuaternionNormalized`** (output_control)  dual_quaternion(-array) `→`  (real)

Normalized dual quaternion.

## Possible Predecessors

`dual_quat_compose`

## Possible Successors

`dual_quat_to_hom_mat3d`

## See also

`dual_quat_interpolate`,
`pose_to_dual_quat`,
`screw_to_dual_quat`,
`dual_quat_to_screw`,
`dual_quat_to_pose`,
`dual_quat_conjugate`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`quat_normalize`

## Module

Foundation
