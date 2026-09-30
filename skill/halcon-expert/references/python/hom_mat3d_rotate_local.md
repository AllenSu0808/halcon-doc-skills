# hom_mat3d_rotate_local (Operator)

## Name

`hom_mat3d_rotate_local` — Add a rotation to a homogeneous 3D transformation matrix.

## Signature

`def hom_mat3d_rotate_local(hom_mat_3d: Sequence[float], phi: Union[float, int], axis: MaybeSequence[Union[str, float, int]]) -> Sequence[float]`

## Description

`hom_mat3d_rotate_local` adds a rotation by the angle *`phi`*
around the axis passed in the parameter *`axis`* to the homogeneous 3D
transformation matrix *`hom_mat_3d`* and returns the resulting matrix in
*`hom_mat_3drotate`*. The axis can be specified by passing the strings
'x', 'y', or 'z', or by passing a vector [x,y,z] as a tuple.

The rotation is described by a 3×3 rotation matrix
R. In contrast to [`hom_mat3d_rotate`](hom_mat3d_rotate.md), it
is performed relative to the local coordinate system, i.e., the coordinate
system described by *`hom_mat_3d`*; this corresponds to the following
chain of transformation matrices:

*`axis`* = *"x"*:
$$HomMat3DRotate = HomMat3D \cdot \\begin{bmatrix} R_x \ 0 \\ 0 \\ 0 \\ 0 \\ 1 \end{bmatrix}$$ ![figure](../assets/7469b1d3d5b0d601.svg)

*`axis`* = *"y"*:
$$HomMat3DRotate = HomMat3D . R_y = [ [cos(Phi) 0 sin(Phi)]; [0 1 0]; [-sin(Phi) 0 cos(Phi)] ]$$ ![figure](../assets/b4bff2170ecf99a3.svg)

*`axis`* = *"z"*:
$$HomMat3DRotate = HomMat3D \cdot R_z = R_z = \begin{bmatrix} \cos(\Phi) & -\sin(\Phi) & 0 \\ sin(\Phi) & \cos(\Phi) & 0 \\ 0 & 0 & 1 \end{bmatrix} @ Axis = [x,y,z]:$$ ![figure](../assets/3a0796af1b77555a.svg)$$HomMat3Rotate = HomMat3D \cdot \begin{bmatrix} R_a \\ 0 \\ 0 \\ 0 \\ 1 \end{bmatrix} R_a = u \cdot u^T + cos(\Phi_i) \cdot (I - u \cdot u^T) + sin(\Phi_i) \cdot S$$ ![figure](../assets/f2fdb97342f5dd95.svg)
$$\mathbf{u} = \frac{\text{Axis}}{\|\text{Axis}\|} = \begin{pmatrix} x' \\ y' \\ z' \end{pmatrix} \quad I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \quad S = \begin{bmatrix} 0 & -z' & y' \\ z' & 0 & -x' \\ -y' & x' & 0 \end{bmatrix}$$ ![figure](../assets/4a6ec7d589909b65.svg)

The fixed point of the transformation is the origin of the local
coordinate system, i.e., this point remains unchanged when
transformed using *`hom_mat_3drotate`*.

## Attention

Note that homogeneous matrices are stored row-by-row as a tuple;
the last row is usually not stored because it is identical for all
homogeneous matrices that describe an affine transformation. For example,
the homogeneous matrix
$$\left[\begin{array}{cccc} ra & rb & rc & td \\ re & rf & rg & th \\ ri & rj & rk & tl \\ 0 & 0 & 0 & 1 \end{array}\right]$$ ![figure](../assets/6e5fe31b1dd2a4f4.svg)
is stored as the tuple [ra, rb, rc, td, re, rf, rg, th, ri, rj, rk, tl].
However, it is also possible to process full 4×4 matrices,
which represent a projective 4D transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Input transformation matrix.

**`phi`** (input_control)  angle.rad `→` Union[float, int]

Rotation angle.

Default:
0.78

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.78, 1.57, 3.14

Value range:
`0
≤
phi
≤
6.28318530718`

**`axis`** (input_control)  string(-array) `→` MaybeSequence[Union[str, float, int]]

Axis, to be rotated around.

Default:
"x"

Suggested values:
"x", "y", "z"

**`hom_mat_3drotate`** (output_control)  hom_mat3d `→` Sequence[float]

Output transformation matrix.

## Result

If the parameters are valid, the operator
`hom_mat3d_rotate_local` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`hom_mat3d_identity`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate_local`

## Possible Successors

`hom_mat3d_translate_local`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate_local`

## See also

`hom_mat3d_invert`,
`hom_mat3d_identity`,
`hom_mat3d_rotate`,
`pose_to_hom_mat3d`,
`hom_mat3d_to_pose`,
`hom_mat3d_compose`

## Module

Foundation
