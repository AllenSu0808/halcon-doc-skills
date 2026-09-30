# hom_mat2d_invert (Operator)

## Name

`hom_mat2d_invert` — Invert a homogeneous 2D transformation matrix.

## Signature

`def hom_mat2d_invert(hom_mat_2d: Sequence[float]) -> Sequence[float]`

## Description

`hom_mat2d_invert` inverts the homogeneous 2D transformation
matrix given by *`hom_mat_2d`*. The resulting matrix is returned in
*`hom_mat_2dinvert`*.

## Attention

Note that homogeneous matrices are stored row-by-row as a tuple;
the last row is usually not stored because it is identical for all
homogeneous matrices that describe an affine transformation. For example,
the homogeneous matrix
$$\begin{bmatrix} ra & rb & tc \\ rd & re & tf \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/dd4c7548e15a2db4.svg)
is stored as the tuple [ra, rb, tc, rd, re, tf]. However, it is also
possible to process full 3×3 matrices, which represent
a projective 2D transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`hom_mat_2dinvert`** (output_control)  hom_mat2d `→` Sequence[float]

Output transformation matrix.

## Result

`hom_mat2d_invert` returns 2 (
H_MSG_TRUE)
if the parameters are valid and the
input matrix is invertible. Otherwise, an exception is raised.

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
