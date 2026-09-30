# project_hom_point_hom_mat3d (Operator)

## Name

`project_hom_point_hom_mat3d` — Project a homogeneous 3D point using a 3×4 projection matrix.

## Signature

`def project_hom_point_hom_mat3d(hom_mat_3d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]], pw: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def project_hom_point_hom_mat3d_s(hom_mat_3d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]], pw: MaybeSequence[Union[float, int]]) -> Tuple[float, float, float]`

## Description

[`projective_trans_hom_point_3d`](projective_trans_hom_point_3d.md) applies the 3×4 projection
matrix *`hom_mat_3d`* to all homogeneous input points
(*`px`*,*`py`*,*`pz`*,*`pw`*) and returns an
array of homogeneous output points
(*`qx`*,*`qy`*,*`qw`*). The transformation is
described by the homogeneous transformation matrix given in
*`hom_mat_3d`*. This corresponds to the following equation (input
and output points as homogeneous vectors):
$$\begin{pmatrix}Qx\\Qy\\Qw\end{pmatrix}=\mathrm{HomMat3D}\cdot\begin{pmatrix}Px\\Py\\Pz\\Pw\end{pmatrix}$$ ![figure](../assets/0a4227b35c277e7a.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they must be divided by *`qw`*:
$$\begin{pmatrix}Ex \\ Ey\end{pmatrix} = \begin{pmatrix}\frac{Qx}{Qw} \\ \frac{Qy}{Qw}\end{pmatrix}$$ ![figure](../assets/d34e9b0ceb4d1677.svg)
This can be achieved directly by calling
[`project_point_hom_mat3d`](project_point_hom_mat3d.md). Thus,
`project_hom_point_hom_mat3d` is primarily useful for
transforming points or point sets for which the resulting points
might lie on the line at infinity, i.e., points that potentially
have *`qw`* = 0, for which the above division cannot be
performed.

Note that, consistent with the conventions used by the projection in
[`calibrate_cameras`](calibrate_cameras.md), *`qx`* corresponds to the column
coordinate of an image and *`qy`* corresponds to the row
coordinate.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

3×4 projection matrix.

**`px`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (x coordinate).

**`py`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (y coordinate).

**`pz`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (z coordinate).

**`pw`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (w coordinate).

**`qx`** (output_control)  real(-array) `→` Sequence[float]

Output point (x coordinate).

**`qy`** (output_control)  real(-array) `→` Sequence[float]

Output point (y coordinate).

**`qw`** (output_control)  real(-array) `→` Sequence[float]

Output point (w coordinate).

## Possible Predecessors

`cam_par_pose_to_hom_mat3d`

## Alternatives

`project_point_hom_mat3d`,
`project_3d_point`

## Module

Foundation
