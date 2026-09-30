# HomMat2dCompose (Operator)

## Name

`HomMat2dCompose` — Multiply two homogeneous 2D transformation matrices.

## Signature

`static void HOperatorSet.HomMat2dCompose(HTuple homMat2DLeft, HTuple homMat2DRight, out HTuple homMat2DCompose)`

`HHomMat2D HHomMat2D.HomMat2dCompose(HHomMat2D homMat2DRight)`

## Description

`HomMat2dCompose` composes a new 2D transformation matrix
by multiplying the two input matrices:

$$\texttt{HomMat2DCompose}=\texttt{HomMat2DLeft}\cdot\texttt{HomMat2DRight}$$

For example, if the two input matrices correspond to rigid transformations,
i.e., to transformations consisting of a rotation and a translation, the
resulting matrix is calculated as follows:

$$\text{HomMat2DCompose} = \begin{bmatrix} R_l & T_l \\ 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} R_r & T_r \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} R_l \cdot R_r & R_l \cdot T_r + T_l \\ 0 & 1 \end{bmatrix}$$ ![figure](../assets/f7664fb7e84633a4.svg)

## Attention

Note that homogeneous matrices are stored row-by-row as a tuple;
the last row is usually not stored because it is identical for all
homogeneous matrices that describe an affine transformation. For example,
the homogeneous matrix
$$\begin{bmatrix} ra & rb & tc \\ rd & re & tf \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/dd4c7548e15a2db4.svg)
is stored as the tuple [ra, rb, tc, rd, re, tf]. However, it is also
possible to process full 3×3 matrices, which represent
a projective 2D transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat2DLeft`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Left input transformation matrix.

**`homMat2DRight`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Right input transformation matrix.

**`homMat2DCompose`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

If the parameters are valid, the operator `HomMat2dCompose` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`HomMat2dCompose`,
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
