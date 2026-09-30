# hom_mat2d_determinant (Operator)

## Name

`hom_mat2d_determinant` — Compute the determinant of a homogeneous 2D transformation matrix.

## Signature

`hom_mat2d_determinant( : : HomMat2D : Determinant)`

## Description

`hom_mat2d_determinant` computes the determinant of the
homogeneous 2D transformation matrix given by *`HomMat2D`* and
returns it in *`Determinant`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Input transformation matrix.

**`Determinant`** (output_control)  real `→`  (real)

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
