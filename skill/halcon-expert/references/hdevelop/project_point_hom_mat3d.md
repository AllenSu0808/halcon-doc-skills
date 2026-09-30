# project_point_hom_mat3d (Operator)

## Name

`project_point_hom_mat3d` — Project a 3D point using a 3×4 projection matrix.

## Signature

`project_point_hom_mat3d( : : HomMat3D, Px, Py, Pz : Qx, Qy)`

## Description

`project_point_hom_mat3d` applies the 3×4 projection matrix
*`HomMat3D`* to all input points
(*`Px`*,*`Py`*,*`Pz`*) and returns an array of output
points (*`Qx`*,*`Qy`*). The transformation is described by
the 3×4 projection matrix given in *`HomMat3D`*. This
corresponds to the following equations (input and output points as
homogeneous vectors):
$$\begin{pmatrix}T_x\\T_y\\T_w\end{pmatrix}=\mathrm{HomMat3D}\cdot\begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix}$$ ![figure](../assets/542613f12ba435d5.svg)

`project_point_hom_mat3d` then transforms the homogeneous
coordinates to Euclidean coordinates by dividing them by Tw:
$$\left(\begin{array}{c} Q_x \\ Q_y \end{array}\right) = \left(\begin{array}{c} \frac{T_x}{T_w} \\ \frac{T_y}{T_w} \end{array}\right)$$ ![figure](../assets/391e23b82653b558.svg)
If a point on the line at infinity (Tw = 0) is created by the
transformation, an error is returned. If this is undesired,
[`project_hom_point_hom_mat3d`](project_hom_point_hom_mat3d.md) can be used.

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

**`Qx`** (output_control)  real(-array) `→`  (real)

Output point (x coordinate).

**`Qy`** (output_control)  real(-array) `→`  (real)

Output point (y coordinate).

## Possible Predecessors

`cam_par_pose_to_hom_mat3d`

## Alternatives

`project_hom_point_hom_mat3d`,
`project_3d_point`

## Module

Foundation
