# hom_mat3d_identity (Operator)

## Name

`hom_mat3d_identity` — Generate the homogeneous transformation matrix of the identical 3D
transformation.

## Signature

`hom_mat3d_identity( : : : HomMat3DIdentity)`

## Description

`hom_mat3d_identity` generates the homogeneous transformation matrix
*`HomMat3DIdentity`* describing the identical 3D transformation:

$$\text{HomMat3DIdentity} = \left[\begin{array}{cccc}1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{array}\right]$$ ![figure](../assets/15bc9a0bea0a66ce.svg)

## Attention

Note that homogeneous matrices are stored row-by-row as a tuple; the
last row is not stored because it is identical for all homogeneous matrices
that describe an affine transformation. Thus, *`HomMat3DIdentity`* is
stored as the tuple [1,0,0,0,0,1,0,0,0,0,1,0].

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HomMat3DIdentity`** (output_control)  hom_mat3d `→`  (real)

Transformation matrix.

## Result

`hom_mat3d_identity` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`hom_mat3d_translate`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate`,
`hom_mat3d_rotate_local`

## Alternatives

`pose_to_hom_mat3d`

## Module

Foundation
