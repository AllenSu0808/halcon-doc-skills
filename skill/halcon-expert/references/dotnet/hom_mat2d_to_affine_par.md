# HomMat2dToAffinePar (Operator)

## Name

`HomMat2dToAffinePar` — Compute the affine transformation parameters from a homogeneous 2D
transformation matrix.

## Signature

`static void HOperatorSet.HomMat2dToAffinePar(HTuple homMat2D, out HTuple sx, out HTuple sy, out HTuple phi, out HTuple theta, out HTuple tx, out HTuple ty)`

`double HHomMat2D.HomMat2dToAffinePar(out double sy, out double phi, out double theta, out double tx, out double ty)`

## Description

`HomMat2dToAffinePar` computes the affine transformation parameters
corresponding to the homogeneous 2D transformation matrix *`homMat2D`*.
The parameters *`sx`* and *`sy`* determine how the transformation
scales the original x- and y-axes, respectively. The two scaling factors are
always positive. The angle *`theta`* describes whether the transformed
coordinate axes are orthogonal (*`theta`* = 0) or slanted. If
$|\texttt{Theta}|>\pi/2$, the transformation
contains a reflection. The angle *`phi`* determines the rotation of the
transformed x-axis with respect to the original x-axis. The parameters
*`tx`* and *`ty`* determine the translation of the two coordinate
systems. The matrix *`homMat2D`* can be constructed from the six
transformation parameters by the following operator sequence:

|  |
| --- |
| [`HomMat2dIdentity(HomMat2DIdentity)`](hom_mat2d_identity.md) |
| [`HomMat2dScale(HomMat2DIdentity, Sx, Sy, 0, 0, HomMat2DScale)`](hom_mat2d_scale.md) |
| [`HomMat2dSlant(HomMat2DScale, Theta, "y", 0, 0, HomMat2DSlant)`](hom_mat2d_slant.md) |
| [`HomMat2dRotate(HomMat2DSlant, Phi, 0, 0, HomMat2DRotate)`](hom_mat2d_rotate.md) |
| [`HomMat2dTranslate(HomMat2DRotate, Tx, Ty, HomMat2D)`](hom_mat2d_translate.md) |

This is equivalent to the following chain of transformation matrices:

$$\mathrm{HomMat2D} = \begin{bmatrix} 1 & 0 & +Tx \\ 0 & 1 & +Ty \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} \cos(\phi) & -\sin(\phi) & 0 \\ \sin(\phi) & \cos(\phi) & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 & -\sin(\theta) & 0 \\ 0 & \cos(\theta) & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} S_x & 0 & 0 \\ 0 & S_y & 0 \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/da1387253d504744.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`sx`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Scaling factor along the x direction.

**`sy`** (output_control)  real `→` [HTuple](HTuple.md) (*double*)

Scaling factor along the y direction.

**`phi`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Rotation angle.

**`theta`** (output_control)  angle.rad `→` [HTuple](HTuple.md) (*double*)

Slant angle.

**`tx`** (output_control)  point.x `→` [HTuple](HTuple.md) (*double*)

Translation along the x direction.

**`ty`** (output_control)  point.y `→` [HTuple](HTuple.md) (*double*)

Translation along the y direction.

## Result

If the matrix *`homMat2D`* is non-degenerate and represents an
affine transformation (i.e., not a projective transformation),
`HomMat2dToAffinePar` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised.

## Possible Predecessors

`VectorToHomMat2d`,
`VectorToRigid`,
`VectorToSimilarity`,
`VectorToAniso`,
`PointLineToHomMat2d`

## Possible Successors

`HomMat2dTranslate`,
`HomMat2dScale`,
`HomMat2dRotate`,
`HomMat2dSlant`

## Module

Foundation
