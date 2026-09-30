# AffineTransPoint3d (Operator)

## Name

`AffineTransPoint3d` — Apply an arbitrary affine 3D transformation to points.

## Signature

`static void HOperatorSet.AffineTransPoint3d(HTuple homMat3D, HTuple px, HTuple py, HTuple pz, out HTuple qx, out HTuple qy, out HTuple qz)`

`HTuple HHomMat3D.AffineTransPoint3d(HTuple px, HTuple py, HTuple pz, out HTuple qy, out HTuple qz)`

`double HHomMat3D.AffineTransPoint3d(double px, double py, double pz, out double qy, out double qz)`

## Description

`AffineTransPoint3d` applies an arbitrary affine 3D transformation,
i.e., scaling, rotation, and translation, to the input points
(*`px`*,*`py`*,*`pz`*) and returns the resulting points in
(*`qx`*, *`qy`*,*`qz`*). The affine transformation is
described by the homogeneous transformation matrix given in
*`homMat3D`*. This corresponds to the following equation (input and
output points as homogeneous vectors):

$$\begin{pmatrix}Q_x\\Q_y\\Q_z\\1\end{pmatrix} = \mathrm{HomMat3D} \cdot \begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix}$$ ![figure](../assets/1a543a153c82d08b.svg)

The transformation matrix can be created using the operators
[`HomMat3dIdentity`](hom_mat3d_identity.md), [`HomMat3dScale`](hom_mat3d_scale.md),
[`HomMat3dRotate`](hom_mat3d_rotate.md), [`HomMat3dTranslate`](hom_mat3d_translate.md), etc., or be the result
of [`PoseToHomMat3d`](pose_to_hom_mat3d.md).

For example, if *`homMat3D`* corresponds to a rigid transformation,
i.e., if it consists of a rotation and a translation, the
points are transformed as follows:

$$\begin{pmatrix}Q_x\\Q_y\\Q_z\\1\end{pmatrix} = \begin{bmatrix}R & T\\0 & 1\end{bmatrix} \cdot \begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix} = (R\cdot \begin{pmatrix}P_x\\P_y\\P_z\end{pmatrix}+T)$$ ![figure](../assets/689e51e41e8b66c0.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`px`** (input_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point(s) (x coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point(s) (y coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`pz`** (input_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point(s) (z coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`qx`** (output_control)  point3d.x(-array) `→` [HTuple](HTuple.md) (*double*)

Output point(s) (x coordinate).

**`qy`** (output_control)  point3d.y(-array) `→` [HTuple](HTuple.md) (*double*)

Output point(s) (y coordinate).

**`qz`** (output_control)  point3d.z(-array) `→` [HTuple](HTuple.md) (*double*)

Output point(s) (z coordinate).

## Result

If the parameters are valid, the operator `AffineTransPoint3d`
returns 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`HomMat3dTranslate`,
`HomMat3dTranslateLocal`,
`HomMat3dScale`,
`HomMat3dScaleLocal`,
`HomMat3dRotate`,
`HomMat3dRotateLocal`

## Possible Successors

`HomMat3dTranslate`,
`HomMat3dTranslateLocal`,
`HomMat3dScale`,
`HomMat3dScaleLocal`,
`HomMat3dRotate`,
`HomMat3dRotateLocal`

## Module

Foundation
