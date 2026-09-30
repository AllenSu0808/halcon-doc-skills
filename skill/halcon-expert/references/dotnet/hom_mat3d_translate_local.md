# HomMat3dTranslateLocal (Operator)

## Name

`HomMat3dTranslateLocal` — Add a translation to a homogeneous 3D transformation matrix.

## Signature

`static void HOperatorSet.HomMat3dTranslateLocal(HTuple homMat3D, HTuple tx, HTuple ty, HTuple tz, out HTuple homMat3DTranslate)`

`HHomMat3D HHomMat3D.HomMat3dTranslateLocal(HTuple tx, HTuple ty, HTuple tz)`

`HHomMat3D HHomMat3D.HomMat3dTranslateLocal(double tx, double ty, double tz)`

## Description

`HomMat3dTranslateLocal` adds a translation by the vector
t = (*`tx`*,*`ty`*,*`tz`*) to
the homogeneous 3D transformation matrix *`homMat3D`* and returns the
resulting matrix in *`homMat3DTranslate`*. In contrast to
[`HomMat3dTranslate`](hom_mat3d_translate.md), the translation is performed relative to the
local coordinate system, i.e., the coordinate system described by
*`homMat3D`*; this corresponds to the following chain of transformation
matrices:

$$HomMat3DTranslate = HomMat3D \cdot \\begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \\ 1 & & \\end{bmatrix} \\ T = (T_x \; T_y \; T_z)^T$$ ![figure](../assets/26e69b0f385b0062.svg)

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

**`tx`** (input_control)  point3d.x `→` [HTuple](HTuple.md) (*double* / int / long)

Translation along the x-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`ty`** (input_control)  point3d.y `→` [HTuple](HTuple.md) (*double* / int / long)

Translation along the y-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`tz`** (input_control)  point3d.z `→` [HTuple](HTuple.md) (*double* / int / long)

Translation along the z-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`homMat3DTranslate`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

If the parameters are valid, the operator
`HomMat3dTranslateLocal` returns 2 (
H_MSG_TRUE)
. If necessary, an
exception is raised.

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
`HomMat3dTranslate`,
`PoseToHomMat3d`,
`HomMat3dToPose`,
`HomMat3dCompose`

## Module

Foundation
