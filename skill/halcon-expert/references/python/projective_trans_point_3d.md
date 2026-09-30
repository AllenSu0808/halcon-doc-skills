# projective_trans_point_3d (Operator)

## Name

`projective_trans_point_3d` — Project a 3D point using a projective transformation matrix.

## Signature

`def projective_trans_point_3d(hom_mat_3d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def projective_trans_point_3d_s(hom_mat_3d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pz: MaybeSequence[Union[float, int]]) -> Tuple[float, float, float]`

## Description

`projective_trans_point_3d` applies the homogeneous projective
transformation matrix *`hom_mat_3d`* to all input points
(*`px`*,*`py`*,*`pz`*) and returns an array of output
points (*`qx`*,*`qy`*,*`qz`*). The transformation is
described by the homogeneous transformation matrix given in
*`hom_mat_3d`*. This corresponds to the following equations
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

**`hom_mat_3d`** (input_control)  hom_mat3d `→` Sequence[float]

Homogeneous projective transformation matrix.

**`px`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (x coordinate).

**`py`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (y coordinate).

**`pz`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (z coordinate).

**`qx`** (output_control)  number(-array) `→` Sequence[float]

Output point (x coordinate).

**`qy`** (output_control)  number(-array) `→` Sequence[float]

Output point (y coordinate).

**`qz`** (output_control)  number(-array) `→` Sequence[float]

Output point (z coordinate).

## Possible Predecessors

`vector_to_hom_mat3d`

## Alternatives

`projective_trans_hom_point_3d`

## Module

Foundation
