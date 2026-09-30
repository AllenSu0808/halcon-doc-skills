# hom_mat2d_compose (Operator)

## Name

`hom_mat2d_compose` — Multiply two homogeneous 2D transformation matrices.

## Signature

`def hom_mat2d_compose(hom_mat_2dleft: Sequence[float], hom_mat_2dright: Sequence[float]) -> Sequence[float]`

## Description

`hom_mat2d_compose` composes a new 2D transformation matrix
by multiplying the two input matrices:

$$\texttt{HomMat2DCompose}=\texttt{HomMat2DLeft}\cdot\texttt{HomMat2DRight}$$

For example, if the two input matrices correspond to rigid transformations,
i.e., to transformations consisting of a rotation and a translation, the
resulting matrix is calculated as follows:

$$\text{HomMat2DCompose} = \begin{bmatrix} R_l & T_l \\ 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} R_r & T_r \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} R_l \cdot R_r & R_l \cdot T_r + T_l \\ 0 & 1 \end{bmatrix}$$ ![figure](../assets/f7664fb7e84633a4.svg)

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

**`hom_mat_2dleft`** (input_control)  hom_mat2d `→` Sequence[float]

Left input transformation matrix.

**`hom_mat_2dright`** (input_control)  hom_mat2d `→` Sequence[float]

Right input transformation matrix.

**`hom_mat_2dcompose`** (output_control)  hom_mat2d `→` Sequence[float]

Output transformation matrix.

## Result

If the parameters are valid, the operator `hom_mat2d_compose` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`hom_mat2d_compose`,
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
