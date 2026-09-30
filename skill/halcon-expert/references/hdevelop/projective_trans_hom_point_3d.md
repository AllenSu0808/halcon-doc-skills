# projective_trans_hom_point_3d (Operator)

## Name

`projective_trans_hom_point_3d` — Project a homogeneous 3D point using a projective transformation
matrix.

## Signature

`projective_trans_hom_point_3d( : : HomMat3D, Px, Py, Pz, Pw : Qx, Qy, Qz, Qw)`

## Description

`projective_trans_hom_point_3d` applies the homogeneous
projective transformation matrix *`HomMat3D`* to all
homogeneous input points
(*`Px`*,*`Py`*,*`Pz`*,*`Pw`*) and returns an
array of homogeneous output points
(*`Qx`*,*`Qy`*,*`Qz`*,*`Qw`*). The
transformation is described by the homogeneous transformation matrix
given in *`HomMat3D`*. This corresponds to the following
equation (input and output points as homogeneous vectors):

$$\begin{pmatrix}Q_x\\Q_Y\\Q_z\\Q_w\end{pmatrix}=\mathrm{HomMat3D}\cdot\begin{pmatrix}P_x\\P_y\\P_z\\P_w\end{pmatrix}$$ ![figure](../assets/e56fcb87676422d6.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they must be divided by *`Qw`*:
$$\begin{pmatrix} E_x \\ E_y \\ E_z \end{pmatrix} = \begin{pmatrix} \dfrac{Q_x}{Q_w} \\ \dfrac{Q_y}{Q_w} \\ \dfrac{Q_z}{Q_w} \\ }$$ ![figure](../assets/415e212ce8dc0ca9.svg)
This can be achieved directly by calling
[`projective_trans_point_3d`](projective_trans_point_3d.md). Thus,
`projective_trans_hom_point_3d` is primarily useful for
transforming points or point sets for which the resulting points
might lie in the plane at infinity, i.e., points that potentially
have *`Qw`* = 0, for which the above division cannot be
performed.

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

**`Pw`** (input_control)  number(-array) `→`  (real / integer)

Input point (w coordinate).

**`Qx`** (output_control)  number(-array) `→`  (real)

Output point (x coordinate).

**`Qy`** (output_control)  number(-array) `→`  (real)

Output point (y coordinate).

**`Qz`** (output_control)  number(-array) `→`  (real)

Output point (z coordinate).

**`Qw`** (output_control)  number(-array) `→`  (real)

Output point (w coordinate).

## Possible Predecessors

`vector_to_hom_mat3d`

## Alternatives

`projective_trans_point_3d`

## Module

Foundation
