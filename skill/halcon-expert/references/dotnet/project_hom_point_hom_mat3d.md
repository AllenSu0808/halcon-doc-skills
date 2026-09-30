# ProjectHomPointHomMat3d (Operator)

## Name

`ProjectHomPointHomMat3d` — Project a homogeneous 3D point using a 3×4 projection matrix.

## Signature

`static void HOperatorSet.ProjectHomPointHomMat3d(HTuple homMat3D, HTuple px, HTuple py, HTuple pz, HTuple pw, out HTuple qx, out HTuple qy, out HTuple qw)`

`HTuple HHomMat3D.ProjectHomPointHomMat3d(HTuple px, HTuple py, HTuple pz, HTuple pw, out HTuple qy, out HTuple qw)`

`double HHomMat3D.ProjectHomPointHomMat3d(double px, double py, double pz, double pw, out double qy, out double qw)`

## Description

[`ProjectiveTransHomPoint3d`](projective_trans_hom_point_3d.md) applies the 3×4 projection
matrix *`homMat3D`* to all homogeneous input points
(*`px`*,*`py`*,*`pz`*,*`pw`*) and returns an
array of homogeneous output points
(*`qx`*,*`qy`*,*`qw`*). The transformation is
described by the homogeneous transformation matrix given in
*`homMat3D`*. This corresponds to the following equation (input
and output points as homogeneous vectors):
$$\begin{pmatrix}Qx\\Qy\\Qw\end{pmatrix}=\mathrm{HomMat3D}\cdot\begin{pmatrix}Px\\Py\\Pz\\Pw\end{pmatrix}$$ ![figure](../assets/0a4227b35c277e7a.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they must be divided by *`qw`*:
$$\begin{pmatrix}Ex \\ Ey\end{pmatrix} = \begin{pmatrix}\frac{Qx}{Qw} \\ \frac{Qy}{Qw}\end{pmatrix}$$ ![figure](../assets/d34e9b0ceb4d1677.svg)
This can be achieved directly by calling
[`ProjectPointHomMat3d`](project_point_hom_mat3d.md). Thus,
`ProjectHomPointHomMat3d` is primarily useful for
transforming points or point sets for which the resulting points
might lie on the line at infinity, i.e., points that potentially
have *`qw`* = 0, for which the above division cannot be
performed.

Note that, consistent with the conventions used by the projection in
[`CalibrateCameras`](calibrate_cameras.md), *`qx`* corresponds to the column
coordinate of an image and *`qy`* corresponds to the row
coordinate.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

3×4 projection matrix.

**`px`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (x coordinate).

**`py`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (y coordinate).

**`pz`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (z coordinate).

**`pw`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (w coordinate).

**`qx`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (x coordinate).

**`qy`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (y coordinate).

**`qw`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (w coordinate).

## Possible Predecessors

`CamParPoseToHomMat3d`

## Alternatives

`ProjectPointHomMat3d`,
`Project3dPoint`

## Module

Foundation
