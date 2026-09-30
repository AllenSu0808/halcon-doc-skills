# ProjectPointHomMat3d (Operator)

## Name

`ProjectPointHomMat3d` — Project a 3D point using a 3×4 projection matrix.

## Signature

`static void HOperatorSet.ProjectPointHomMat3d(HTuple homMat3D, HTuple px, HTuple py, HTuple pz, out HTuple qx, out HTuple qy)`

`HTuple HHomMat3D.ProjectPointHomMat3d(HTuple px, HTuple py, HTuple pz, out HTuple qy)`

`double HHomMat3D.ProjectPointHomMat3d(double px, double py, double pz, out double qy)`

## Description

`ProjectPointHomMat3d` applies the 3×4 projection matrix
*`homMat3D`* to all input points
(*`px`*,*`py`*,*`pz`*) and returns an array of output
points (*`qx`*,*`qy`*). The transformation is described by
the 3×4 projection matrix given in *`homMat3D`*. This
corresponds to the following equations (input and output points as
homogeneous vectors):
$$\begin{pmatrix}T_x\\T_y\\T_w\end{pmatrix}=\mathrm{HomMat3D}\cdot\begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix}$$ ![figure](../assets/542613f12ba435d5.svg)

`ProjectPointHomMat3d` then transforms the homogeneous
coordinates to Euclidean coordinates by dividing them by Tw:
$$\left(\begin{array}{c} Q_x \\ Q_y \end{array}\right) = \left(\begin{array}{c} \frac{T_x}{T_w} \\ \frac{T_y}{T_w} \end{array}\right)$$ ![figure](../assets/391e23b82653b558.svg)
If a point on the line at infinity (Tw = 0) is created by the
transformation, an error is returned. If this is undesired,
[`ProjectHomPointHomMat3d`](project_hom_point_hom_mat3d.md) can be used.

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

**`qx`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (x coordinate).

**`qy`** (output_control)  real(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (y coordinate).

## Possible Predecessors

`CamParPoseToHomMat3d`

## Alternatives

`ProjectHomPointHomMat3d`,
`Project3dPoint`

## Module

Foundation
