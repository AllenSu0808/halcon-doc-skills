# hom_mat3d_invert (Operator)

## Name

`hom_mat3d_invert` — Invert a homogeneous 3D transformation matrix.

## Signature

`hom_mat3d_invert( : : HomMat3D : HomMat3DInvert)`

## Description

`hom_mat3d_invert` inverts the homogeneous 3D transformation
matrix given by *`HomMat3D`*. The resulting matrix is returned in
*`HomMat3DInvert`*.

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

**`HomMat3D`** (input_control)  hom_mat3d `→`  (real)

Input transformation matrix.

**`HomMat3DInvert`** (output_control)  hom_mat3d `→`  (real)

Output transformation matrix.

## Result

`hom_mat3d_invert` returns 2 (
H_MSG_TRUE)
if the parameters are valid and the
input matrix is invertible. Otherwise, an exception is raised.

## Possible Predecessors

`hom_mat3d_translate`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate`,
`hom_mat3d_rotate_local`,
`pose_to_hom_mat3d`

## Possible Successors

`hom_mat3d_translate`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate`,
`hom_mat3d_rotate_local`,
`hom_mat3d_to_pose`

## Alternatives

`pose_invert`,
`dual_quat_conjugate`

## See also

`affine_trans_point_3d`,
`hom_mat3d_identity`,
`hom_mat3d_rotate`,
`hom_mat3d_translate`,
`pose_to_hom_mat3d`,
`hom_mat3d_to_pose`,
`hom_mat3d_compose`

## Module

Foundation
