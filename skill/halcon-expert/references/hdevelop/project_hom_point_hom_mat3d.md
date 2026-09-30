# project_hom_point_hom_mat3d (Operator)

## Name

`project_hom_point_hom_mat3d` — Project a homogeneous 3D point using a 3×4 projection matrix.

## Signature

`project_hom_point_hom_mat3d( : : HomMat3D, Px, Py, Pz, Pw : Qx, Qy, Qw)`

## Description

[`projective_trans_hom_point_3d`](projective_trans_hom_point_3d.md) applies the 3×4 projection
matrix *`HomMat3D`* to all homogeneous input points
(*`Px`*,*`Py`*,*`Pz`*,*`Pw`*) and returns an
array of homogeneous output points
(*`Qx`*,*`Qy`*,*`Qw`*). The transformation is
described by the homogeneous transformation matrix given in
*`HomMat3D`*. This corresponds to the following equation (input
and output points as homogeneous vectors):
$$\begin{pmatrix}Qx\\Qy\\Qw\end{pmatrix}=\mathrm{HomMat3D}\cdot\begin{pmatrix}Px\\Py\\Pz\\Pw\end{pmatrix}$$ ![figure](../assets/0a4227b35c277e7a.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they must be divided by *`Qw`*:
$$\begin{pmatrix}Ex \\ Ey\end{pmatrix} = \begin{pmatrix}\frac{Qx}{Qw} \\ \frac{Qy}{Qw}\end{pmatrix}$$ ![figure](../assets/d34e9b0ceb4d1677.svg)
This can be achieved directly by calling
[`project_point_hom_mat3d`](project_point_hom_mat3d.md). Thus,
`project_hom_point_hom_mat3d` is primarily useful for
transforming points or point sets for which the resulting points
might lie on the line at infinity, i.e., points that potentially
have *`Qw`* = 0, for which the above division cannot be
performed.

Note that, consistent with the conventions used by the projection in
[`calibrate_cameras`](calibrate_cameras.md), *`Qx`* corresponds to the column
coordinate of an image and *`Qy`* corresponds to the row
coordinate.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`HomMat3D`** (input_control)  hom_mat3d `→`  (real)

3×4 projection matrix.

**`Px`** (input_control)  number(-array) `→`  (real / integer)

Input point (x coordinate).

**`Py`** (input_control)  number(-array) `→`  (real / integer)

Input point (y coordinate).

**`Pz`** (input_control)  number(-array) `→`  (real / integer)

Input point (z coordinate).

**`Pw`** (input_control)  number(-array) `→`  (real / integer)

Input point (w coordinate).

**`Qx`** (output_control)  real(-array) `→`  (real)

Output point (x coordinate).

**`Qy`** (output_control)  real(-array) `→`  (real)

Output point (y coordinate).

**`Qw`** (output_control)  real(-array) `→`  (real)

Output point (w coordinate).

## Possible Predecessors

`cam_par_pose_to_hom_mat3d`

## Alternatives

`project_point_hom_mat3d`,
`project_3d_point`

## Module

Foundation
