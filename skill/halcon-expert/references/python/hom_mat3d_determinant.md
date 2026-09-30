# hom_mat3d_determinant (Operator)

## Name

`hom_mat3d_determinant` — Compute the determinant of a homogeneous 3D transformation matrix.

## Signature

`def hom_mat3d_determinant(hom_mat_3d: Sequence[float]) -> float`

## Description

`hom_mat3d_determinant` computes the determinant of the
homogeneous 3D transformation matrix given by *`hom_mat_3d`* and
returns it in *`determinant`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Input transformation matrix.

**`determinant`** (output_control)  real `→` float

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
