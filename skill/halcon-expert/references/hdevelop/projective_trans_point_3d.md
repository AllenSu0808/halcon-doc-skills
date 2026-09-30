# projective_trans_point_3d (Operator)

## Name

`projective_trans_point_3d` — Project a 3D point using a projective transformation matrix.

## Signature

`projective_trans_point_3d( : : HomMat3D, Px, Py, Pz : Qx, Qy, Qz)`

## Description

`projective_trans_point_3d` applies the homogeneous projective
transformation matrix *`HomMat3D`* to all input points
(*`Px`*,*`Py`*,*`Pz`*) and returns an array of output
points (*`Qx`*,*`Qy`*,*`Qz`*). The transformation is
described by the homogeneous transformation matrix given in
*`HomMat3D`*. This corresponds to the following equations
(input and output points as homogeneous vectors):

$$\begin{pmatrix}T_x\\T_y\\T_z\\T_w\end{pmatrix}=\text{HoMAt3D}\cdot\begin{pmatrix}P_x\\P_y\\P_z\\1\end{pmatrix}$$ ![figure](../assets/25fc3f48e837c725.svg)

`projective_trans_point_3d` then transforms the homogeneous
coordinates to Euclidean coordinates by dividing them by Tw:
$$\begin{pmatrix} Qx \\ Qy \\ Qz \end{pmatrix} = \begin{pmatrix} \dfrac{Tx}{Tw} \\ \dfrac{Ty}{Tw} \\ \dfrac{Tz}{Tw} \\ \dfrac{T w}{Tw} \end{pmatrix}$$ ![figure](../assets/524a9b2d5e9a2a11.svg)
If a point in the plane at infinity (Tw = 0) is created by the
transformation, an error is returned. If this is undesired,
[`projective_trans_hom_point_3d`](projective_trans_hom_point_3d.md) can be used.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`HomMat3D`** (input_control)  hom_mat3d `→`  (real)

Homogeneous projective transformation matrix.

**`Px`** (input_control)  number(-array) `→`  (real / integer)

Input point (x coordinate).

**`Py`** (input_control)  number(-array) `→`  (real / integer)

Input point (y coordinate).

**`Pz`** (input_control)  number(-array) `→`  (real / integer)

Input point (z coordinate).

**`Qx`** (output_control)  number(-array) `→`  (real)

Output point (x coordinate).

**`Qy`** (output_control)  number(-array) `→`  (real)

Output point (y coordinate).

**`Qz`** (output_control)  number(-array) `→`  (real)

Output point (z coordinate).

## Possible Predecessors

`vector_to_hom_mat3d`

## Alternatives

`projective_trans_hom_point_3d`

## Module

Foundation
