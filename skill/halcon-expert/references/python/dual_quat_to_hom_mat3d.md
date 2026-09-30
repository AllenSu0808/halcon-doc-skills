# dual_quat_to_hom_mat3d (Operator)

## Name

`dual_quat_to_hom_mat3d` — Convert a unit dual quaternion into a homogeneous transformation matrix.

## Signature

`def dual_quat_to_hom_mat3d(dual_quaternion: Sequence[float]) -> Sequence[float]`

## Description

The operator `dual_quat_to_hom_mat3d` converts a unit dual quaternion
*`dual_quaternion`*, which represents a 3D rigid transformation,
into its corresponding homogeneous transformation matrix *`hom_mat_3d`*.

For a brief introduction to dual quaternions, the used notation, and the
relationship between dual quaternions and screws, see
`“Solution Guide III-C - 3D Vision”`.

The rotation part of *`hom_mat_3d`* is computed from the
real part of the dual quaternion, as described in [`quat_to_hom_mat3d`](quat_to_hom_mat3d.md).
The translation part $\mathbf{T}$ of *`hom_mat_3d`* is computed
from the real and dual part of
$\hat{q} = q_r + \varepsilon q_d$ ![figure](../assets/58fb67719e5d2ee1.svg):
$$p = q_d q_r T = \frac{2.0 v_p}{,}$$ ![figure](../assets/ba64ef0d981a111f.svg)
where $\mathbf{v}_{p}$ is the vector part of the quaternion
$p$.

## Attention

*`hom_mat_3d`* will only be a valid rigid transformation matrix if
*`dual_quaternion`* is a unit dual quaternion.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dual_quaternion`** (input_control)  dual_quaternion `→` Sequence[float]

Unit dual quaternion.

**`hom_mat_3d`** (output_control)  hom_mat3d `→` Sequence[float]

Transformation matrix.

## Possible Predecessors

`screw_to_dual_quat`,
`dual_quat_interpolate`,
`dual_quat_compose`,
`dual_quat_normalize`

## Possible Successors

`affine_trans_point_3d`

## Alternatives

`dual_quat_to_pose`,
`dual_quat_to_screw`

## See also

`dual_quat_compose`,
`pose_to_dual_quat`,
`dual_quat_conjugate`,
`serialize_dual_quat`,
`deserialize_dual_quat`,
`dual_quat_trans_line_3d`,
`dual_quat_trans_point_3d`,
`quat_to_hom_mat3d`

## Module

Foundation
