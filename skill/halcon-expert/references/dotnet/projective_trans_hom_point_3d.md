# ProjectiveTransHomPoint3d (Operator)

## Name

`ProjectiveTransHomPoint3d` — Project a homogeneous 3D point using a projective transformation
matrix.

## Signature

`static void HOperatorSet.ProjectiveTransHomPoint3d(HTuple homMat3D, HTuple px, HTuple py, HTuple pz, HTuple pw, out HTuple qx, out HTuple qy, out HTuple qz, out HTuple qw)`

`HTuple HHomMat3D.ProjectiveTransHomPoint3d(HTuple px, HTuple py, HTuple pz, HTuple pw, out HTuple qy, out HTuple qz, out HTuple qw)`

`double HHomMat3D.ProjectiveTransHomPoint3d(double px, double py, double pz, double pw, out double qy, out double qz, out double qw)`

## Description

`ProjectiveTransHomPoint3d` applies the homogeneous
projective transformation matrix *`homMat3D`* to all
homogeneous input points
(*`px`*,*`py`*,*`pz`*,*`pw`*) and returns an
array of homogeneous output points
(*`qx`*,*`qy`*,*`qz`*,*`qw`*). The
transformation is described by the homogeneous transformation matrix
given in *`homMat3D`*. This corresponds to the following
equation (input and output points as homogeneous vectors):

$$\begin{pmatrix}Q_x\\Q_Y\\Q_z\\Q_w\end{pmatrix}=\mathrm{HomMat3D}\cdot\begin{pmatrix}P_x\\P_y\\P_z\\P_w\end{pmatrix}$$ ![figure](../assets/e56fcb87676422d6.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they must be divided by *`qw`*:
$$\begin{pmatrix} E_x \\ E_y \\ E_z \end{pmatrix} = \begin{pmatrix} \dfrac{Q_x}{Q_w} \\ \dfrac{Q_y}{Q_w} \\ \dfrac{Q_z}{Q_w} \\ }$$ ![figure](../assets/415e212ce8dc0ca9.svg)
This can be achieved directly by calling
[`ProjectiveTransPoint3d`](projective_trans_point_3d.md). Thus,
`ProjectiveTransHomPoint3d` is primarily useful for
transforming points or point sets for which the resulting points
might lie in the plane at infinity, i.e., points that potentially
have *`qw`* = 0, for which the above division cannot be
performed.

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

**`pw`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*double* / int / long)

Input point (w coordinate).

**`qx`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (x coordinate).

**`qy`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (y coordinate).

**`qz`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (z coordinate).

**`qw`** (output_control)  number(-array) `→` [HTuple](HTuple.md) (*double*)

Output point (w coordinate).

## Possible Predecessors

`VectorToHomMat3d`

## Alternatives

`ProjectiveTransPoint3d`

## Module

Foundation
