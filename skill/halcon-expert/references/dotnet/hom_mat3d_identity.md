# HomMat3dIdentity (Operator)

## Name

`HomMat3dIdentity` — Generate the homogeneous transformation matrix of the identical 3D
transformation.

## Signature

`static void HOperatorSet.HomMat3dIdentity(out HTuple homMat3DIdentity)`

`public HHomMat3D()`

`void HHomMat3D.HomMat3dIdentity()`

## Description

`HomMat3dIdentity` generates the homogeneous transformation matrix
*`homMat3DIdentity`* describing the identical 3D transformation:

$$\text{HomMat3DIdentity} = \left[\begin{array}{cccc}1 & 0 & 0 & 0\\0 & 1 & 0 & 0\\0 & 0 & 1 & 0\\0 & 0 & 0 & 1\end{array}\right]$$ ![figure](../assets/15bc9a0bea0a66ce.svg)

## Attention

Note that homogeneous matrices are stored row-by-row as a tuple; the
last row is not stored because it is identical for all homogeneous matrices
that describe an affine transformation. Thus, *`homMat3DIdentity`* is
stored as the tuple [1,0,0,0,0,1,0,0,0,0,1,0].

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat3DIdentity`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Transformation matrix.

## Result

`HomMat3dIdentity` always returns 2 (
H_MSG_TRUE)
.

## Possible Successors

`HomMat3dTranslate`,
`HomMat3dTranslateLocal`,
`HomMat3dScale`,
`HomMat3dScaleLocal`,
`HomMat3dRotate`,
`HomMat3dRotateLocal`

## Alternatives

`PoseToHomMat3d`

## Module

Foundation
