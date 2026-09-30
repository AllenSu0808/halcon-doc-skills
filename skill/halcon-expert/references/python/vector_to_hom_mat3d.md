# vector_to_hom_mat3d (Operator)

## Name

`vector_to_hom_mat3d` — Approximate a 3D transformation from point correspondences.

## Signature

`def vector_to_hom_mat3d(transformation_type: str, px: Sequence[float], py: Sequence[float], pz: Sequence[float], qx: Sequence[float], qy: Sequence[float], qz: Sequence[float]) -> Sequence[float]`

## Description

`vector_to_hom_mat3d` approximates an affine or projective 3D
transformation from point correspondences and returns it as the
homogeneous transformation matrix *`hom_mat_3d`*.

The type of the 3D transformation to compute is specified with
*`transformation_type`*. For *`transformation_type`* =
*"rigid"*, a rigid 3D transformation (a rotation and a
translation), for *`transformation_type`* =
*"similarity"*, a 3D similarity transformation (a uniform
scaling, a rotation, and a translation), for
*`transformation_type`* = *"affine"* a general affine
3D transformation, and for *`transformation_type`* =
*"projective"* a projective 3D transformation is computed.

The minimum required number of point correspondences is 3 for
*`transformation_type`* = *"rigid"*, 3 for
*`transformation_type`* = *"similarity"*, 4 for
*`transformation_type`* = *"affine"*, and 5 for
*`transformation_type`* = *"projective"*.

The point correspondences are passed in the tuples
(*`px`*,*`py`*,*`pz`*) and
(*`qx`*,*`qy`*,*`qz`*), where corresponding points
must be at the same index positions in the tuples. If more than the
minimum number of point correspondences are passed, the
transformation is overdetermined. In this case, the returned
transformation is the transformation that minimizes the distances
between the transformed input points
(*`px`*,*`py`*,*`pz`*) and the points
(*`qx`*,*`qy`*,*`qz`*), as described in the following
equation (points as homogeneous vectors):

$$\sum_i \left| \begin{pmatrix} Q_x[i] \\ Q_y[i] \\ Q_z[i] \\ 1 \end{pmatrix} \right| - \mathrm{HomMat3D} \cdot \begin{pmatrix} P_x[i] \\ P_y[i] \\ P_z[i] \\ 1 \end{pmatrix}|^2 = \minimize$$ ![figure](../assets/a5aa51a9bccf4de1.svg)

*`hom_mat_3d`* can be used directly with operators that transform
3D data using affine transformations, e.g.,
[`affine_trans_point_3d`](affine_trans_point_3d.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`transformation_type`** (input_control)  string `→` str

Type of the transformation to compute.

Default:
"rigid"

List of values:
"affine", "projective", "rigid", "similarity"

**`px`** (input_control)  point3d.x-array `→` Sequence[float]

X coordinates of the original points.

**`py`** (input_control)  point3d.y-array `→` Sequence[float]

Y coordinates of the original points.

**`pz`** (input_control)  point3d.z-array `→` Sequence[float]

Z coordinates of the original points.

**`qx`** (input_control)  point3d.x-array `→` Sequence[float]

X coordinates of the transformed points.

**`qy`** (input_control)  point3d.x-array `→` Sequence[float]

Y coordinates of the transformed points.

**`qz`** (input_control)  point3d.z-array `→` Sequence[float]

Z coordinates of the transformed points.

**`hom_mat_3d`** (output_control)  hom_mat3d `→` Sequence[float]

Output transformation matrix.

## Possible Successors

`hom_mat3d_to_pose`,
`affine_trans_point_3d`

## See also

`point_pluecker_line_to_hom_mat3d`

## Module

Foundation
