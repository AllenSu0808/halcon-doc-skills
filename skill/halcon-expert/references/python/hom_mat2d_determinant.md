# hom_mat2d_determinant (Operator)

## Name

`hom_mat2d_determinant` — Compute the determinant of a homogeneous 2D transformation matrix.

## Signature

`def hom_mat2d_determinant(hom_mat_2d: Sequence[float]) -> float`

## Description

`hom_mat2d_determinant` computes the determinant of the
homogeneous 2D transformation matrix given by *`hom_mat_2d`* and
returns it in *`determinant`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`determinant`** (output_control)  real `→` float

Determinant of the input matrix.

## Result

`hom_mat2d_determinant` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`hom_mat2d_translate`,
`hom_mat2d_translate_local`,
`hom_mat2d_scale`,
`hom_mat2d_scale_local`,
`hom_mat2d_rotate`,
`hom_mat2d_rotate_local`,
`hom_mat2d_slant`,
`hom_mat2d_slant_local`,
`hom_mat2d_reflect`,
`hom_mat2d_reflect_local`

## Module

Foundation
