# hom_mat2d_to_affine_par (Operator)

## Name

`hom_mat2d_to_affine_par` — Compute the affine transformation parameters from a homogeneous 2D
transformation matrix.

## Signature

`hom_mat2d_to_affine_par( : : HomMat2D : Sx, Sy, Phi, Theta, Tx, Ty)`

## Description

`hom_mat2d_to_affine_par` computes the affine transformation parameters
corresponding to the homogeneous 2D transformation matrix *`HomMat2D`*.
The parameters *`Sx`* and *`Sy`* determine how the transformation
scales the original x- and y-axes, respectively. The two scaling factors are
always positive. The angle *`Theta`* describes whether the transformed
coordinate axes are orthogonal (*`Theta`* = 0) or slanted. If
$|\texttt{Theta}|>\pi/2$, the transformation
contains a reflection. The angle *`Phi`* determines the rotation of the
transformed x-axis with respect to the original x-axis. The parameters
*`Tx`* and *`Ty`* determine the translation of the two coordinate
systems. The matrix *`HomMat2D`* can be constructed from the six
transformation parameters by the following operator sequence:

|  |
| --- |
| [`hom_mat2d_identity(HomMat2DIdentity)`](hom_mat2d_identity.md) |
| [`hom_mat2d_scale(HomMat2DIdentity, Sx, Sy, 0, 0, HomMat2DScale)`](hom_mat2d_scale.md) |
| [`hom_mat2d_slant(HomMat2DScale, Theta, 'y', 0, 0, HomMat2DSlant)`](hom_mat2d_slant.md) |
| [`hom_mat2d_rotate(HomMat2DSlant, Phi, 0, 0, HomMat2DRotate)`](hom_mat2d_rotate.md) |
| [`hom_mat2d_translate(HomMat2DRotate, Tx, Ty, HomMat2D)`](hom_mat2d_translate.md) |

This is equivalent to the following chain of transformation matrices:

$$\mathrm{HomMat2D} = \begin{bmatrix} 1 & 0 & +Tx \\ 0 & 1 & +Ty \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} \cos(\phi) & -\sin(\phi) & 0 \\ \sin(\phi) & \cos(\phi) & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 & -\sin(\theta) & 0 \\ 0 & \cos(\theta) & 0 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{bmatrix} S_x & 0 & 0 \\ 0 & S_y & 0 \\ 0 & 0 & 1 \end{bmatrix}$$ ![figure](../assets/da1387253d504744.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Input transformation matrix.

**`Sx`** (output_control)  real `→`  (real)

Scaling factor along the x direction.

**`Sy`** (output_control)  real `→`  (real)

Scaling factor along the y direction.

**`Phi`** (output_control)  angle.rad `→`  (real)

Rotation angle.

**`Theta`** (output_control)  angle.rad `→`  (real)

Slant angle.

**`Tx`** (output_control)  point.x `→`  (real)

Translation along the x direction.

**`Ty`** (output_control)  point.y `→`  (real)

Translation along the y direction.

## Result

If the matrix *`HomMat2D`* is non-degenerate and represents an
affine transformation (i.e., not a projective transformation),
`hom_mat2d_to_affine_par` returns 2 (
H_MSG_TRUE)
. Otherwise, an
exception is raised.

## Possible Predecessors

`vector_to_hom_mat2d`,
`vector_to_rigid`,
`vector_to_similarity`,
`vector_to_aniso`,
`point_line_to_hom_mat2d`

## Possible Successors

`hom_mat2d_translate`,
`hom_mat2d_scale`,
`hom_mat2d_rotate`,
`hom_mat2d_slant`

## Module

Foundation
