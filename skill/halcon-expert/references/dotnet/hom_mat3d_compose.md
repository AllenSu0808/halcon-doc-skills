# HomMat3dCompose (Operator)

## Name

`HomMat3dCompose` — Multiply two homogeneous 3D transformation matrices.

## Signature

`static void HOperatorSet.HomMat3dCompose(HTuple homMat3DLeft, HTuple homMat3DRight, out HTuple homMat3DCompose)`

`HHomMat3D HHomMat3D.HomMat3dCompose(HHomMat3D homMat3DRight)`

## Description

`HomMat3dCompose` composes a new 3D transformation matrix
by multiplying the two input matrices:

$$\texttt{HomMat3DCompose}=\texttt{HomMat3DLeft}\cdot\texttt{HomMat3DRight}$$

For example, if the two input matrices correspond to rigid transformations,
i.e., to transformations consisting of a rotation and a translation, the
resulting matrix is calculated as follows:

$$\mathrm{HomMat3DCcompose} = \left[ \begin{array}{ccc} R_l & T_l \\ 0 & 1 \\ \end{array} \right] \cdot \left[ \begin{array}{ccc} R_r & T_r \\ 0 & 1 \\ \end{array} \right] = \left[ \begin{array}{ccc} R_l \cdot R_r & R_l \cdot T_r + T_l \\ 0 & 1 \\ \end{array} \right]$$ ![figure](../assets/688aa08f7b15c7c4.svg)

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

**`homMat3DLeft`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Left input transformation matrix.

**`homMat3DRight`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Right input transformation matrix.

**`homMat3DCompose`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

If the parameters are valid, the operator `HomMat3dCompose` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`HomMat3dCompose`,
`HomMat3dTranslate`,
`HomMat3dTranslateLocal`,
`HomMat3dScale`,
`HomMat3dScaleLocal`,
`HomMat3dRotate`,
`HomMat3dRotateLocal`,
`PoseToHomMat3d`

## Possible Successors

`HomMat3dCompose`,
`HomMat3dTranslate`,
`HomMat3dTranslateLocal`,
`HomMat3dScale`,
`HomMat3dScaleLocal`,
`HomMat3dRotate`,
`HomMat3dRotateLocal`

## Alternatives

`PoseCompose`,
`DualQuatCompose`

## See also

`AffineTransPoint3d`,
`HomMat3dIdentity`,
`HomMat3dRotate`,
`HomMat3dTranslate`,
`PoseToHomMat3d`,
`HomMat3dToPose`

## Module

Foundation
