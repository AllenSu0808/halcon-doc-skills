# HomMat2dDeterminant (Operator)

## Name

`HomMat2dDeterminant` — Compute the determinant of a homogeneous 2D transformation matrix.

## Signature

`static void HOperatorSet.HomMat2dDeterminant(HTuple homMat2D, out HTuple determinant)`

`double HHomMat2D.HomMat2dDeterminant()`

## Description

`HomMat2dDeterminant` computes the determinant of the
homogeneous 2D transformation matrix given by *`homMat2D`* and
returns it in *`determinant`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`determinant`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Determinant of the input matrix.

## Result

`HomMat2dDeterminant` always returns 2 (
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

## Module

Foundation
