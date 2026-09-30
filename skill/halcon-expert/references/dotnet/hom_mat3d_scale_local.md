# HomMat3dScaleLocal (Operator)

## Name

`HomMat3dScaleLocal` — Add a scaling to a homogeneous 3D transformation matrix.

## Signature

`static void HOperatorSet.HomMat3dScaleLocal(HTuple homMat3D, HTuple sx, HTuple sy, HTuple sz, out HTuple homMat3DScale)`

`HHomMat3D HHomMat3D.HomMat3dScaleLocal(HTuple sx, HTuple sy, HTuple sz)`

`HHomMat3D HHomMat3D.HomMat3dScaleLocal(double sx, double sy, double sz)`

## Description

`HomMat3dScaleLocal` adds a scaling by the scale factors
*`sx`*, *`sy`*, and *`sz`* to the homogeneous 3D
transformation matrix *`homMat3D`* and returns the resulting matrix in
*`homMat3DScale`*. The scaling is described by a 3×3
scaling matrix S. In contrast to
[`HomMat3dScale`](hom_mat3d_scale.md), it is performed relative to the local coordinate
system, i.e., the coordinate system described by *`homMat3D`*; this
corresponds to the following chain of transformation matrices:

$$HomMat3DScale = HomMat3D.\n\mathbf{S} = \begin{bmatrix} S_x & 0 & 0 \\ 0 & S_y & 0 \\ 0 & 0 & S_z \end{bmatrix}$$ ![figure](../assets/9ef5dcb85c753801.svg)

The fixed point of the transformation is the origin of the local
coordinate system, i.e., this point remains unchanged when
transformed using *`homMat3DScale`*.

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

**`sx`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Scale factor along the x-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sx != 0`

**`sy`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Scale factor along the y-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sy != 0`

**`sz`** (input_control)  number `→` [HTuple](HTuple.md) (*double* / int / long)

Scale factor along the z-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sz != 0`

**`homMat3DScale`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

`HomMat3dScaleLocal` returns 2 (
H_MSG_TRUE)
if all three scale
factors are not 0. If necessary, an exception is raised.

## Possible Predecessors

`HomMat3dIdentity`,
`HomMat3dTranslateLocal`,
`HomMat3dScaleLocal`,
`HomMat3dRotateLocal`

## Possible Successors

`HomMat3dTranslateLocal`,
`HomMat3dScaleLocal`,
`HomMat3dRotateLocal`

## See also

`HomMat3dInvert`,
`HomMat3dIdentity`,
`HomMat3dScale`,
`PoseToHomMat3d`,
`HomMat3dToPose`,
`HomMat3dCompose`

## Module

Foundation
