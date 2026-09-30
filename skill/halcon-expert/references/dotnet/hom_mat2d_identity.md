# HomMat2dIdentity (Operator)

## Name

`HomMat2dIdentity` — Generate the homogeneous transformation matrix of the identical 2D
transformation.

## Signature

`static void HOperatorSet.HomMat2dIdentity(out HTuple homMat2DIdentity)`

`public HHomMat2D()`

`void HHomMat2D.HomMat2dIdentity()`

## Description

`HomMat2dIdentity` generates the homogeneous transformation matrix
*`homMat2DIdentity`* describing the identical 2D transformation:

$$\text{HomMat2DIdentity} = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/d2a174d7f0c057e6.svg)

## Attention

Note that homogeneous matrices are stored row-by-row as a tuple; the
last row is not stored because it is identical for all homogeneous matrices
that describe an affine transformation. Thus, *`homMat2DIdentity`* is
stored as the tuple [1,0,0,0,1,0].

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat2DIdentity`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix.

## Result

`HomMat2dIdentity` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`HomMat2dTranslate`,
`HomMat2dTranslateLocal`,
`HomMat2dScale`,
`HomMat2dScaleLocal`,
`HomMat2dRotate`,
`HomMat2dRotateLocal`,
`HomMat2dSlant`,
`HomMat2dSlantLocal`,
`HomMat2dReflect`,
`HomMat2dReflectLocal`

## Module

Foundation
