# hom_mat3d_translate (Operator)

## Name

`hom_mat3d_translate` — Add a translation to a homogeneous 3D transformation matrix.

## Signature

`hom_mat3d_translate( : : HomMat3D, Tx, Ty, Tz : HomMat3DTranslate)`

## Description

`hom_mat3d_translate` adds a translation by the vector
t = (*`Tx`*,*`Ty`*,*`Tz`*) to
the homogeneous 3D transformation matrix *`HomMat3D`* and returns the
resulting matrix in *`HomMat3DTranslate`*. The translation is performed
relative to the global (i.e., fixed) coordinate system; this corresponds to
the following chain of transformation matrices:

$$HomMat3DTranslate = \begin{bmatrix}1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 1\end{bmatrix} \cdot HomMat3D \\ T = \begin{pmatrix} T_x \\ T_y \\ T_z \end{pmatrix}$$ ![figure](../assets/65f6888ba5dd2792.svg)

To perform the transformation in the local coordinate system, i.e.,
the one described by *`HomMat3D`*, use
[`hom_mat3d_translate_local`](hom_mat3d_translate_local.md).

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

**`HomMat3D`** (input_control)  hom_mat3d `→`  (real)

Input transformation matrix.

**`Tx`** (input_control)  point3d.x `→`  (real / integer)

Translation along the x-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Ty`** (input_control)  point3d.y `→`  (real / integer)

Translation along the y-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Tz`** (input_control)  point3d.z `→`  (real / integer)

Translation along the z-axis.

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`HomMat3DTranslate`** (output_control)  hom_mat3d `→`  (real)

Output transformation matrix.

## Result

If the parameters are valid, the operator `hom_mat3d_translate` returns
2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`hom_mat3d_identity`,
`hom_mat3d_translate`,
`hom_mat3d_scale`,
`hom_mat3d_rotate`

## Possible Successors

`hom_mat3d_translate`,
`hom_mat3d_scale`,
`hom_mat3d_rotate`

## See also

`hom_mat3d_invert`,
`hom_mat3d_identity`,
`hom_mat3d_translate_local`,
`pose_to_hom_mat3d`,
`hom_mat3d_to_pose`,
`hom_mat3d_compose`

## Module

Foundation
