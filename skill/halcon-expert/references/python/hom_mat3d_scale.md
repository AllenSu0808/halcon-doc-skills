# hom_mat3d_scale (Operator)

## Name

`hom_mat3d_scale` — Add a scaling to a homogeneous 3D transformation matrix.

## Signature

`def hom_mat3d_scale(hom_mat_3d: Sequence[float], sx: Union[float, int], sy: Union[float, int], sz: Union[float, int], px: Union[float, int], py: Union[float, int], pz: Union[float, int]) -> Sequence[float]`

## Description

`hom_mat3d_scale` adds a scaling by the scale factors *`sx`*,
*`sy`*, and *`sz`* to the homogeneous 3D transformation matrix
*`hom_mat_3d`* and returns the resulting matrix in *`hom_mat_3dscale`*.
The scaling is described by a 3×3 scaling matrix
S. It is performed relative to the global (i.e.,
fixed) coordinate system; this corresponds to the following chain of
transformation matrices:

$$\mathrm{HomMat3DScale} = \begin{bmatrix} S & 0 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{bmatrix} \cdot \mathrm{HomMat3D} \mathbf{S} = \begin{bmatrix} S_x & 0 & 0 \\ 0 & S_y & 0 \\ 0 & 0 & S_z \end{bmatrix}$$ ![figure](../assets/dc69c600d4fa255a.svg)

The point (*`px`*,*`py`*,*`pz`*) is the fixed point of the
transformation, i.e., this point remains unchanged when transformed using
*`hom_mat_3dscale`*. To obtain this behavior, first a translation is added
to the input transformation matrix that moves the fixed point onto the origin
of the global coordinate system. Then, the scaling is added, and finally a
translation that moves the fixed point back to its original position. This
corresponds to the following chain of transformations:

$$HomMat3DScale = \begin{bmatrix}1&0&0&+Px\\0&1&0&+Py\\0&0&1&+Pz\\0&0&0&1\e nd{bmatrix} \cdot S \cdot \begin{bmatrix}1&0&0&-Px\\0&1&0&-Py\\0&0&1&-Pz\\0&0&0&1\e nd{bmatrix}$$ ![figure](../assets/9924827903379c3a.svg)

To perform the transformation in the local coordinate system, i.e.,
the one described by *`hom_mat_3d`*, use
[`hom_mat3d_scale_local`](hom_mat3d_scale_local.md).

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

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Input transformation matrix.

**`sx`** (input_control)  number `→` Union[float, int]

Scale factor along the x-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sx != 0`

**`sy`** (input_control)  number `→` Union[float, int]

Scale factor along the y-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sy != 0`

**`sz`** (input_control)  number `→` Union[float, int]

Scale factor along the z-axis.

Default:
2

Suggested values:
0.125, 0.25, 0.5, 1, 2, 4, 8, 112

Restriction:
`Sz != 0`

**`px`** (input_control)  point3d.x `→` Union[float, int]

Fixed point of the transformation (x coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point3d.y `→` Union[float, int]

Fixed point of the transformation (y coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`pz`** (input_control)  point3d.z `→` Union[float, int]

Fixed point of the transformation (z coordinate).

Default:
0

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`hom_mat_3dscale`** (output_control)  hom_mat3d `→` Sequence[float]

Output transformation matrix.

## Result

`hom_mat3d_scale` returns 2 (
H_MSG_TRUE)
if all three scale factors are not
0. If necessary, an exception is raised.

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
`hom_mat3d_scale_local`,
`pose_to_hom_mat3d`,
`hom_mat3d_to_pose`,
`hom_mat3d_compose`

## Module

Foundation
