# HomMat3dInvert (Operator)

## Name

`HomMat3dInvert` — Invert a homogeneous 3D transformation matrix.

## Signature

`static void HOperatorSet.HomMat3dInvert(HTuple homMat3D, out HTuple homMat3DInvert)`

`HHomMat3D HHomMat3D.HomMat3dInvert()`

## Description

`HomMat3dInvert` inverts the homogeneous 3D transformation
matrix given by *`homMat3D`*. The resulting matrix is returned in
*`homMat3DInvert`*.

## Attention

Note that homogeneous matrices are stored row-by-row as a tuple;
the last row is usually not stored because it is identical for all
homogeneous matrices that describe an affine transformation. For example,
the homogeneous matrix
$$\left[\begin{array}{cccc} ra & rb & rc & td \\ re & rf & rg & th \\ ri & rj & rk & tl \\ 0 & 0 & 0 & 1 \end{array}\right]$$ ![figure](../assets/6e5fe31b1dd2a4f4.svg)
is stored as the tuple [ra, rb, rc, td, re, rf, rg, th, ri, rj, rk, tl].
However, it is also possible to process full 4×4 matrices,
which represent a projective 4D transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`homMat3DInvert`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

`HomMat3dInvert` returns 2 (
H_MSG_TRUE)
if the parameters are valid and the
input matrix is invertible. Otherwise, an exception is raised.

## Possible Predecessors

`HomMat3dTranslate`,
`HomMat3dTranslateLocal`,
`HomMat3dScale`,
`HomMat3dScaleLocal`,
`HomMat3dRotate`,
`HomMat3dRotateLocal`,
`PoseToHomMat3d`

## Possible Successors

`HomMat3dTranslate`,
`HomMat3dTranslateLocal`,
`HomMat3dScale`,
`HomMat3dScaleLocal`,
`HomMat3dRotate`,
`HomMat3dRotateLocal`,
`HomMat3dToPose`

## Alternatives

`PoseInvert`,
`DualQuatConjugate`

## See also

`AffineTransPoint3d`,
`HomMat3dIdentity`,
`HomMat3dRotate`,
`HomMat3dTranslate`,
`PoseToHomMat3d`,
`HomMat3dToPose`,
`HomMat3dCompose`

## Module

Foundation
