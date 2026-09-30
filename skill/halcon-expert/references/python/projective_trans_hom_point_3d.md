# projective_trans_hom_point_3d (Operator)

## Name

`projective_trans_hom_point_3d` — Project a homogeneous 3D point using a projective transformation
matrix.

## Signature

`def projective_trans_hom_point_3d(hom_mat_3d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]], pw: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float], Sequence[float]]`

`def projective_trans_hom_point_3d_s(hom_mat_3d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]], pw: MaybeSequence[Union[float, int]]) -> Tuple[float, float, float, float]`

## Description

`projective_trans_hom_point_3d` applies the homogeneous
projective transformation matrix *`hom_mat_3d`* to all
homogeneous input points
(*`px`*,*`py`*,*`pz`*,*`pw`*) and returns an
array of homogeneous output points
(*`qx`*,*`qy`*,*`qz`*,*`qw`*). The
transformation is described by the homogeneous transformation matrix
given in *`hom_mat_3d`*. This corresponds to the following
equation (input and output points as homogeneous vectors):

$$\begin{pmatrix}Q_x\\Q_Y\\Q_z\\Q_w\end{pmatrix}=\mathrm{HomMat3D}\cdot\begin{pmatrix}P_x\\P_y\\P_z\\P_w\end{pmatrix}$$ ![figure](../assets/e56fcb87676422d6.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they must be divided by *`qw`*:
$$\begin{pmatrix} E_x \\ E_y \\ E_z \end{pmatrix} = \begin{pmatrix} \dfrac{Q_x}{Q_w} \\ \dfrac{Q_y}{Q_w} \\ \dfrac{Q_z}{Q_w} \\ }$$ ![figure](../assets/415e212ce8dc0ca9.svg)
This can be achieved directly by calling
[`projective_trans_point_3d`](projective_trans_point_3d.md). Thus,
`projective_trans_hom_point_3d` is primarily useful for
transforming points or point sets for which the resulting points
might lie in the plane at infinity, i.e., points that potentially
have *`qw`* = 0, for which the above division cannot be
performed.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Homogeneous projective transformation matrix.

**`px`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (x coordinate).

**`py`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (y coordinate).

**`pz`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (z coordinate).

**`pw`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (w coordinate).

**`qx`** (output_control)  number(-array) `→` Sequence[float]

Output point (x coordinate).

**`qy`** (output_control)  number(-array) `→` Sequence[float]

Output point (y coordinate).

**`qz`** (output_control)  number(-array) `→` Sequence[float]

Output point (z coordinate).

**`qw`** (output_control)  number(-array) `→` Sequence[float]

Output point (w coordinate).

## Possible Predecessors

`vector_to_hom_mat3d`

## Alternatives

`projective_trans_point_3d`

## Module

Foundation
