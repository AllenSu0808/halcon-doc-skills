# hom_mat2d_identity (Operator)

## Name

`hom_mat2d_identity` — Generate the homogeneous transformation matrix of the identical 2D
transformation.

## Signature

`hom_mat2d_identity( : : : HomMat2DIdentity)`

## Description

`hom_mat2d_identity` generates the homogeneous transformation matrix
*`HomMat2DIdentity`* describing the identical 2D transformation:

$$\text{HomMat2DIdentity} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/d2a174d7f0c057e6.svg)

## Attention

Note that homogeneous matrices are stored row-by-row as a tuple; the
last row is not stored because it is identical for all homogeneous matrices
that describe an affine transformation. Thus, *`HomMat2DIdentity`* is
stored as the tuple [1,0,0,0,1,0].

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HomMat2DIdentity`** (output_control)  hom_mat2d `→`  (real)

Transformation matrix.

## Result

`hom_mat2d_identity` always returns 2 (
H_MSG_TRUE)
.

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
