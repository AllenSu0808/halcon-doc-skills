# hom_mat3d_determinant (Operator)

## Name

`hom_mat3d_determinant` — Compute the determinant of a homogeneous 3D transformation matrix.

## Signature

`hom_mat3d_determinant( : : HomMat3D : Determinant)`

## Description

`hom_mat3d_determinant` computes the determinant of the
homogeneous 3D transformation matrix given by *`HomMat3D`* and
returns it in *`Determinant`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HomMat3D`** (input_control)  hom_mat3d `→`  (real)

Input transformation matrix.

**`Determinant`** (output_control)  real `→`  (real)

Determinant of the input matrix.

## Result

`hom_mat3d_determinant` always returns 2 (
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

## Module

Foundation
