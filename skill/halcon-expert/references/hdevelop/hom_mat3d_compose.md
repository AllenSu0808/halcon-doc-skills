# hom_mat3d_compose (Operator)

## Name

`hom_mat3d_compose` — Multiply two homogeneous 3D transformation matrices.

## Signature

`hom_mat3d_compose( : : HomMat3DLeft, HomMat3DRight : HomMat3DCompose)`

## Description

`hom_mat3d_compose` composes a new 3D transformation matrix
by multiplying the two input matrices:

$$\texttt{HomMat3DCompose}=\texttt{HomMat3DLeft}\cdot\texttt{HomMat3DRight}$$

For example, if the two input matrices correspond to rigid transformations,
i.e., to transformations consisting of a rotation and a translation, the
resulting matrix is calculated as follows:

$$\mathrm{HomMat3DCcompose} = \left[ \begin{array}{ccc} R_l & T_l \\ 0 & 1 \\ \end{array} \right] \cdot \left[ \begin{array}{ccc} R_r & T_r \\ 0 & 1 \\ \end{array} \right] = \left[ \begin{array}{ccc} R_l \cdot R_r & R_l \cdot T_r + T_l \\ 0 & 1 \\ \end{array} \right]$$ ![figure](../assets/688aa08f7b15c7c4.svg)

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

**`HomMat3DLeft`** (input_control)  hom_mat3d `→`  (real)

Left input transformation matrix.

**`HomMat3DRight`** (input_control)  hom_mat3d `→`  (real)

Right input transformation matrix.

**`HomMat3DCompose`** (output_control)  hom_mat3d `→`  (real)

Output transformation matrix.

## Result

If the parameters are valid, the operator `hom_mat3d_compose` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`hom_mat3d_compose`,
`hom_mat3d_translate`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate`,
`hom_mat3d_rotate_local`,
`pose_to_hom_mat3d`

## Possible Successors

`hom_mat3d_compose`,
`hom_mat3d_translate`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate`,
`hom_mat3d_rotate_local`

## Alternatives

`pose_compose`,
`dual_quat_compose`

## See also

`affine_trans_point_3d`,
`hom_mat3d_identity`,
`hom_mat3d_rotate`,
`hom_mat3d_translate`,
`pose_to_hom_mat3d`,
`hom_mat3d_to_pose`

## Module

Foundation
