## Dual Quaternions

List of Operators ↓

This chapter contains operators for handling dual quaternions.

### Introduction to Dual Quaternions

A dual quaternion $\hat{q} = q_r + \varepsilon q_d$ ![figure](../assets/58fb67719e5d2ee1.svg) consists of the two quaternions
$q_{r}$ and $q_{d}$, where
$q_{r}$ is the real part, $q_{d}$ is the
dual part, and $\varepsilon$ is the dual unit number
($\varepsilon^{2}=0$). Each quaternion
$q=w+ix+jy+kz$ consists of the scalar part $w$ and
the vector part $\mathbf{v}=(x,y,z)$, where
$(1,i,j,k)$ are the basis elements of the quaternion vector
space.

For information how dual quaternions can be used for the description of
rigid 3D transformations and their relation to Plücker coordinates, see
`“Solution Guide III-C - 3D Vision”`.

### Representing Dual Quaternions in HALCON

In HALCON, a dual quaternion is represented by a tuple with eight
values $[w_{r},x_{r},y_{r},z_{r},w_{d},x_{d},y_{d},z_{d}]$, where
$w_{r}$ and $\mathbf{v}_{r}=(x_{r},y_{r},z_{r})$ are the scalar and the vector part of the real part
and $w_{d}$ and $\mathbf{v}_{d}=(x_{d},y_{d},z_{d})$ are the scalar and the vector part of the dual part.

---

#### List of Operators

- [`DeserializeDualQuat`](deserialize_dual_quat.md) — Deserialize a serialized dual quaternion.

- [`DualQuatCompose`](dual_quat_compose.md) — Multiply two dual quaternions.

- [`DualQuatConjugate`](dual_quat_conjugate.md) — Conjugate a dual quaternion.

- [`DualQuatInterpolate`](dual_quat_interpolate.md) — Interpolate two dual quaternions.

- [`DualQuatNormalize`](dual_quat_normalize.md) — Normalize a dual quaternion.

- [`DualQuatToHomMat3d`](dual_quat_to_hom_mat3d.md) — Convert a unit dual quaternion into a homogeneous transformation matrix.

- [`DualQuatToScrew`](dual_quat_to_screw.md) — Convert a unit dual quaternion into a screw.

- [`DualQuatTransLine3d`](dual_quat_trans_line_3d.md) — Transform a 3D line with a unit dual quaternion.

- [`DualQuatTransPoint3d`](dual_quat_trans_point_3d.md) — Transform a 3D point with a unit dual quaternion.

- [`ScrewToDualQuat`](screw_to_dual_quat.md) — Convert a screw into a dual quaternion.

- [`SerializeDualQuat`](serialize_dual_quat.md) — Serialize a dual quaternion.
