# HomMat3dDeterminant (Operator)

## Name

`HomMat3dDeterminant` — Compute the determinant of a homogeneous 3D transformation matrix.

## Signature

`static void HOperatorSet.HomMat3dDeterminant(HTuple homMat3D, out HTuple determinant)`

`double HHomMat3D.HomMat3dDeterminant()`

## Description

`HomMat3dDeterminant` computes the determinant of the
homogeneous 3D transformation matrix given by *`homMat3D`* and
returns it in *`determinant`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`determinant`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Determinant of the input matrix.

## Result

`HomMat3dDeterminant` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

`HomMat3dTranslate`,
`HomMat3dTranslateLocal`,
`HomMat3dScale`,
`HomMat3dScaleLocal`,
`HomMat3dRotate`,
`HomMat3dRotateLocal`,
`VectorToHomMat3d`

## Module

Foundation
