# affine_trans_point_2d (Operator)

## Name

`affine_trans_point_2d` — Apply an arbitrary affine 2D transformation to points.

## Signature

`def affine_trans_point_2d(hom_mat_2d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def affine_trans_point_2d_s(hom_mat_2d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

`affine_trans_point_2d` applies an arbitrary affine 2D transformation,
i.e., scaling, rotation, translation, and slant (skewing), to the input
points (*`px`*,*`py`*) and returns the resulting points in
(*`qx`*,*`qy`*). The affine transformation is described by the
homogeneous transformation matrix given in *`hom_mat_2d`*. This
corresponds to the following equation (input and output points as
homogeneous vectors):

$$\begin{pmatrix} Q_x \\ Q_y \\ 1 \end{pmatrix} = \mathrm{HomMat2D} \cdot \begin{pmatrix} P_x \\ P_y \\ 1 \end{pmatrix}$$ ![figure](../assets/142dc725bf475f23.svg)

If the points to transform are specified in standard image coordinates, their
*row* coordinates must be passed in *`px`* and their *column*
coordinates in *`py`*. This is necessary to obtain a right-handed
coordinate system for the image. In particular, this assures that rotations
are performed in the correct direction. Note that the (x,y) order of the
matrices quite naturally corresponds to the usual (row,column) order for
coordinates in the image.

The transformation matrix can be created using the operators
[`hom_mat2d_identity`](hom_mat2d_identity.md), [`hom_mat2d_rotate`](hom_mat2d_rotate.md),
[`hom_mat2d_translate`](hom_mat2d_translate.md), etc., or can be the result of operators like
[`vector_angle_to_rigid`](vector_angle_to_rigid.md).

For example, if *`hom_mat_2d`* corresponds to a rigid transformation,
i.e., if it consists of a rotation and a translation, the
points are transformed as follows:

$$\begin{pmatrix}Q_x\\Q_y\\1\end{pmatrix} = \begin{bmatrix}R & T\\0 & 1\end{bmatrix} \cdot \begin{pmatrix}P_x\\P_y\\1\end{pmatrix} = (R \cdot (\begin{pmatrix}P_x\\P_y\\1\end{pmatrix})) + T$$ ![figure](../assets/8751f45210ea5f75.svg)

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`px`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Input point(s) (x or row coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`py`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Input point(s) (y or column coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`qx`** (output_control)  point.x(-array) `→` Sequence[float]

Output point(s) (x or row coordinate).

**`qy`** (output_control)  point.y(-array) `→` Sequence[float]

Output point(s) (y or column coordinate).

## Result

If the matrix *`hom_mat_2d`* represents an affine transformation
(i.e., not a projective transformation),
`affine_trans_point_2d` returns 2 (
H_MSG_TRUE)
. Otherwise, an exception
is raised.

## Possible Predecessors

`hom_mat2d_translate`,
`hom_mat2d_translate_local`,
`hom_mat2d_scale`,
`hom_mat2d_scale_local`,
`hom_mat2d_rotate`,
`hom_mat2d_rotate_local`,
`hom_mat2d_slant`,
`hom_mat2d_slant_local`,
`hom_mat2d_reflect`,
`hom_mat2d_reflect_local`

## Possible Successors

`hom_mat2d_translate`,
`hom_mat2d_translate_local`,
`hom_mat2d_scale`,
`hom_mat2d_scale_local`,
`hom_mat2d_rotate`,
`hom_mat2d_rotate_local`,
`hom_mat2d_slant`,
`hom_mat2d_slant_local`,
`hom_mat2d_reflect`,
`hom_mat2d_reflect_local`

## Module

Foundation
