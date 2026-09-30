# HomMat2dTranspose (Operator)

## Name

`HomMat2dTranspose` — Transpose a homogeneous 2D transformation matrix.

## Signature

`static void HOperatorSet.HomMat2dTranspose(HTuple homMat2D, out HTuple homMat2DTranspose)`

`HHomMat2D HHomMat2D.HomMat2dTranspose()`

## Description

`HomMat2dTranspose` transposes the homogeneous 2D
transformation matrix given by *`homMat2D`*. The result matrix
*`homMat2DTranspose`* is always a 3×3 matrix,
even if the input matrix is represented by a 2×3
matrix.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`homMat2DTranspose`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

`HomMat2dTranspose` always returns 2 (
H_MSG_TRUE)
.

## Possible Predecessors

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

## Possible Successors

`HomMat2dCompose`,
`HomMat2dInvert`

## Module

Foundation
