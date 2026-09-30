# hom_mat3d_transpose (Operator)

## Name

`hom_mat3d_transpose` — Transpose a homogeneous 3D transformation matrix.

## Signature

`hom_mat3d_transpose( : : HomMat3D : HomMat3DTranspose)`

## Description

`hom_mat3d_transpose` transposes the homogeneous 3D
transformation matrix given by *`HomMat3D`*. The result matrix
*`HomMat3DTranspose`* is always a 4×4 matrix,
even if the input matrix is represented by a 3×4
matrix.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HomMat3D`** (input_control)  hom_mat3d `→`  (real)

Input transformation matrix.

**`HomMat3DTranspose`** (output_control)  hom_mat3d `→`  (real)

Output transformation matrix.

## Result

`hom_mat3d_transpose` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`hom_mat3d_translate`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate`,
`hom_mat3d_rotate_local`,
`vector_to_hom_mat3d`

## Possible Successors

`hom_mat3d_compose`,
`hom_mat3d_invert`

## Module

Foundation
