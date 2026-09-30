# hom_mat3d_scale_local (Operator)

## Name

`hom_mat3d_scale_local` — Add a scaling to a homogeneous 3D transformation matrix.

## Signature

`hom_mat3d_scale_local( : : HomMat3D, Sx, Sy, Sz : HomMat3DScale)`

## Description

`hom_mat3d_scale_local` adds a scaling by the scale factors
*`Sx`*, *`Sy`*, and *`Sz`* to the homogeneous 3D
transformation matrix *`HomMat3D`* and returns the resulting matrix in
*`HomMat3DScale`*. The scaling is described by a 3×3
scaling matrix S. In contrast to
[`hom_mat3d_scale`](hom_mat3d_scale.md), it is performed relative to the local coordinate
system, i.e., the coordinate system described by *`HomMat3D`*; this
corresponds to the following chain of transformation matrices:

$$HomMat3DScale = HomMat3D.\n\mathbf{S} = \begin{bmatrix} S_x & 0 & 0 \\ 0 & S_y & 0 \\ 0 & 0 & S_z \end{bmatrix}$$ ![figure](../assets/9ef5dcb85c753801.svg)

The fixed point of the transformation is the origin of the local
coordinate system, i.e., this point remains unchanged when
transformed using *`HomMat3DScale`*.

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

**`Sx`** (input_control)  number `→`  (real / integer)

Scale factor along the x-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sx != 0`

**`Sy`** (input_control)  number `→`  (real / integer)

Scale factor along the y-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sy != 0`

**`Sz`** (input_control)  number `→`  (real / integer)

Scale factor along the z-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sz != 0`

**`HomMat3DScale`** (output_control)  hom_mat3d `→`  (real)

Output transformation matrix.

## Result

`hom_mat3d_scale_local` returns 2 (
H_MSG_TRUE)
if all three scale
factors are not 0. If necessary, an exception is raised.

## Possible Predecessors

`hom_mat3d_identity`,
`hom_mat3d_translate_local`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate_local`

## Possible Successors

`hom_mat3d_translate_local`,
`hom_mat3d_scale_local`,
`hom_mat3d_rotate_local`

## See also

`hom_mat3d_invert`,
`hom_mat3d_identity`,
`hom_mat3d_scale`,
`pose_to_hom_mat3d`,
`hom_mat3d_to_pose`,
`hom_mat3d_compose`

## Module

Foundation
