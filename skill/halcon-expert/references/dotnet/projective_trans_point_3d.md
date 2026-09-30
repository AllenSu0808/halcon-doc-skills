# ProjectiveTransPoint3d (Operator)

## Name

`ProjectiveTransPoint3d` — Project a 3D point using a projective transformation matrix.

## Signature

`static void HOperatorSet.ProjectiveTransPoint3d(HTuple homMat3D, HTuple px, HTuple py, HTuple pz, out HTuple qx, out HTuple qy, out HTuple qz)`

`HTuple HHomMat3D.ProjectiveTransPoint3d(HTuple px, HTuple py, HTuple pz, out HTuple qy, out HTuple qz)`

`double HHomMat3D.ProjectiveTransPoint3d(double px, double py, double pz, out double qy, out double qz)`

## Description

`ProjectiveTransPoint3d` applies the homogeneous projective
transformation matrix *`homMat3D`* to all input points
(*`px`*,*`py`*,*`pz`*) and returns an array of output
points (*`qx`*,*`qy`*,*`qz`*). The transformation is
described by the homogeneous transformation matrix given in
*`homMat3D`*. This corresponds to the following equations
(input and output points as homogeneous vectors):

$$\begin{pmatrix}T_x\\T_y\\T_z\\T_w\end{pmatrix}=\text{HoMAt3D}\cdot\begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix}$$ ![figure](../assets/25fc3f48e837c725.svg)

`ProjectiveTransPoint3d` then transforms the homogeneous
coordinates to Euclidean coordinates by dividing them by Tw:
$$\begin{pmatrix} Qx \\ Qy \\ Qz \end{pmatrix} = \begin{pmatrix} \dfrac{Tx}{Tw} \\ \dfrac{Ty}{Tw} \\ \dfrac{Tz}{Tw} \\ \dfrac{T w}{Tw} \end{pmatrix}$$ ![figure](../assets/524a9b2d5e9a2a11.svg)
If a point in the plane at infinity (Tw = 0) is created by the
transformation, an error is returned. If this is undesired,
[`ProjectiveTransHomPoint3d`](projective_trans_hom_point_3d.md) can be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`homMat3D`** (input_control)  hom_mat3d `→` [HHomMat3D](HHomMat3D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

**`px`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (x coordinate).

**`py`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (y coordinate).

**`pz`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (z coordinate).

**`qx`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (x coordinate).

**`qy`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (y coordinate).

**`qz`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (z coordinate).

## Possible Predecessors

`VectorToHomMat3d`

## Alternatives

`ProjectiveTransHomPoint3d`

## Module

Foundation
