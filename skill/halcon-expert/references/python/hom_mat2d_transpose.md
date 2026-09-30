# hom_mat2d_transpose (Operator)

## Name

`hom_mat2d_transpose` — Transpose a homogeneous 2D transformation matrix.

## Signature

`def hom_mat2d_transpose(hom_mat_2d: Sequence[float]) -> Sequence[float]`

## Description

`hom_mat2d_transpose` transposes the homogeneous 2D
transformation matrix given by *`hom_mat_2d`*. The result matrix
*`hom_mat_2dtranspose`* is always a 3×3 matrix,
even if the input matrix is represented by a 2×3
matrix.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`hom_mat_2dtranspose`** (output_control)  hom_mat2d `→` Sequence[float]

Output transformation matrix.

## Result

`hom_mat2d_transpose` always returns 2 (
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

## Possible Successors

`hom_mat2d_compose`,
`hom_mat2d_invert`

## Module

Foundation
