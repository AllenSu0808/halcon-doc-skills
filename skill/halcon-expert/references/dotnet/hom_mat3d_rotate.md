# HomMat3dRotate (Operator)

## Name

`HomMat3dRotate` — Add a rotation to a homogeneous 3D transformation matrix.

## Signature

`static void HOperatorSet.HomMat3dRotate(HTuple homMat3D, HTuple phi, HTuple axis, HTuple px, HTuple py, HTuple pz, out HTuple homMat3DRotate)`

`HHomMat3D HHomMat3D.HomMat3dRotate(HTuple phi, HTuple axis, HTuple px, HTuple py, HTuple pz)`

`HHomMat3D HHomMat3D.HomMat3dRotate(double phi, string axis, double px, double py, double pz)`

## Description

`HomMat3dRotate` adds a rotation by the angle *`phi`* around the
axis passed in the parameter *`axis`* to the homogeneous 3D
transformation matrix *`homMat3D`* and returns the resulting matrix in
*`homMat3DRotate`*. The axis can be specified by passing the strings
'x', 'y', or 'z', or by passing a vector [x,y,z] as a tuple.

The rotation is described by a 3×3 rotation matrix
R. It is performed relative to the global
(i.e., fixed) coordinate system; this corresponds to the following chain of
transformation matrices:

*`axis`* = *"x"*:
$$HomMat3DRotate = \begin{bmatrix} 1 & 0 & 0 & 0 \\ 0 & R_x & 0 & 0 \\ 0 & 0 & R_x & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \cdot HomMat3D \\\nR_x = \begin{bmatrix} 1 & 0 & 0 \\ 0 & cos(\phi_i) & -sin(\phi_i) \\ 0 & sin(\phi_i) & cos(\phi_i) \end{bmatrix}$$ ![figure](../assets/799ecd4d14cddb35.svg)

*`axis`* = *"y"*:
$$\text{HomMat3DRotate} = \begin{bmatrix} R_y \end{bmatrix} \cdot \text{HomMat3D} \\ R_y = \begin{bmatrix} \cos(\phi) & 0 & \sin(\phi) \\ 0 & 1 & 0 \\ -\sin(\phi) & 0 & \cos(\phi) \end{bmatrix}$$ ![figure](../assets/d3e081b0a9f8148b.svg)

*`axis`* = *"z"*:
$$HomMat3DRotate = \begin{bmatrix}0&0&0&0\\R_z&0&0&1\\0&0&0&0\\0&0&0&1\end{bmatrix} \cdot HomMat3D\\R_z = \begin{bmatrix}\cos(\phi) & -\sin(\phi) & 0\\ \sin(\phi) & \cos(\phi) & 0\\ 0 & 0 & 1\end{bmatrix$$ ![figure](../assets/e6f17a25a55b910e.svg)

*`axis`* = *[x,y,z]*:
$$HomMat3Rotate = \begin{bmatrix} R_a & 0 & 0 & 0 \\ 0 & R_a & 0 & 0 \\ 0 & 0 & R_a & 0 \\ 0 & 0 & 0 & 1 \end{bmatrix} \cdot \ HomMat3D\quad R_a = u \cdot u^T + \cos(\Phi_i) \cdot (I - u \cdot u^T) + \sin(\Phi_i) \cdot S$$ ![figure](../assets/39ee1ddcb7676655.svg)
$$\mathbf{u} = \frac{\text{Axis}}{\|\text{Axis}\|} = \begin{pmatrix} x' \\ y' \\ z' \end{pmatrix} \quad I = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \end{bmatrix} \quad S = \begin{bmatrix} 0 & -z' & y' \\ z' & 0 & -x' \\ -y' & x' & 0 \end{bmatrix}$$ ![figure](../assets/4a6ec7d589909b65.svg)

The point (*`px`*,*`py`*,*`pz`*) is the fixed point of the
transformation, i.e., this point remains unchanged when transformed using
*`homMat3DRotate`*. To obtain this behavior, first a translation is
added to the input transformation matrix that moves the fixed point onto the
origin of the global coordinate system. Then, the rotation is added, and
finally a translation that moves the fixed point back to its original
position. This corresponds to the following chain of transformations:

$$HomMat3DRotate = \begin{bmatrix}1&0&0&+Px\\0&1&0&+Py\\0&0&1&+Pz\\0&0&0&1\end{bmatrix} \cdot \begin{bmatrix}0\\0\\0\\0\end{bmatrix} \cdot R \cdot \begin{bmatrix}1&0&0&-Px\\0&1&0&-Py\\0&0&1&-Pz\\0&0&0&1\end{bmatrix} \cdot HomMat3DRotate$$ ![figure](../assets/d1a46bba288f2005.svg)

To perform the transformation in the local coordinate system, i.e.,
the one described by *`homMat3D`*, use
[`HomMat3dRotateLocal`](hom_mat3d_rotate_local.md).

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

**`phi`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Rotation angle.

Default:
0.78

Suggested values:
0.1, 0.2, 0.3, 0.4, 0.78, 1.57, 3.14

Value range:
`0
≤
phi
≤
6.28318530718`

**`axis`** (input_control)  string(-array) `→` [HTuple](HTuple.md) (*string* / double / int / long)

Axis, to be rotated around.

Default:
"x"

Suggested values:
"x", "y", "z"

**`px`** (input_control)  point3d.x `→` [HTuple](HTuple.md) (*double* / int / long)

Fixed point of the transformation (x coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point3d.y `→` [HTuple](HTuple.md) (*double* / int / long)

Fixed point of the transformation (y coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`pz`** (input_control)  point3d.z `→` [HTuple](HTuple.md) (*double* / int / long)

Fixed point of the transformation (z coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`homMat3DRotate`** (output_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Result

If the parameters are valid, the operator `HomMat3dRotate` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`HomMat3dIdentity`,
`HomMat3dTranslate`,
`HomMat3dScale`,
`HomMat3dRotate`

## Possible Successors

`HomMat3dTranslate`,
`HomMat3dScale`,
`HomMat3dRotate`

## See also

`HomMat3dInvert`,
`HomMat3dIdentity`,
`HomMat3dRotateLocal`,
`PoseToHomMat3d`,
`HomMat3dToPose`,
`HomMat3dCompose`

## Module

Foundation
