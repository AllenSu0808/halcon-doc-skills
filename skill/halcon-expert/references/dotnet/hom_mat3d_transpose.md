# HomMat3dTranspose (Operator)

## Name

`HomMat3dTranspose` — Transpose a homogeneous 3D transformation matrix.

## Signature

`static void HOperatorSet.HomMat3dTranspose(HTuple homMat3D, out HTuple homMat3DTranspose)`

`HHomMat3D HHomMat3D.HomMat3dTranspose()`

## Description

`HomMat3dTranspose` transposes the homogeneous 3D
transformation matrix given by *`homMat3D`*. The result matrix
*`homMat3DTranspose`* is always a 4×4 matrix,
even if the input matrix is represented by a 3×4
matrix.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`homMat3DTranspose`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

`HomMat3dTranspose` always returns 2 (
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

## Possible Successors

`HomMat3dCompose`,
`HomMat3dInvert`

## Module

Foundation
