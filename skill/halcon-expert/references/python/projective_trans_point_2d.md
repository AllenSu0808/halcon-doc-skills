# projective_trans_point_2d (Operator)

## Name

`projective_trans_point_2d` — Project a homogeneous 2D point using a projective transformation
matrix.

## Signature

`def projective_trans_point_2d(hom_mat_2d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pw: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float], Sequence[float]]`

`def projective_trans_point_2d_s(hom_mat_2d: Sequence[float], px: MaybeSequence[Union[float, int]], py: MaybeSequence[Union[float, int]], pw: MaybeSequence[Union[float, int]]) -> Tuple[float, float, float]`

## Description

`projective_trans_point_2d` applies the homogeneous projective
transformation matrix *`hom_mat_2d`* to all homogeneous input
points (*`px`*,*`py`*,*`pw`*) and returns an array of
homogeneous output points (*`qx`*,*`qy`*,*`qw`*). The
transformation is described by the homogeneous transformation matrix
given in *`hom_mat_2d`*. This corresponds to the following
equation (input and output points as homogeneous vectors):

$$\begin{pmatrix}Q_x \\ Q_y \\ Q_w\end{pmatrix}=\mathrm{HomMat2D}\cdot \begin{pmatrix}P_x \\ P_y \\ P_w\end{pmatrix}$$ ![figure](../assets/577384673df19c8d.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they have to be divided by *`qw`*:
$$\begin{pmatrix}Ex \\ Ey\end{pmatrix} = \begin{pmatrix}\frac{Qx}{Qw} \\ \frac{Qy}{Qw}\end{pmatrix}$$ ![figure](../assets/d34e9b0ceb4d1677.svg)

If the points to transform are specified in standard image
coordinates, their *row* coordinates must be passed in
*`px`* and their *column* coordinates in *`py`*. This
is necessary to obtain a right-handed coordinate system for the
image. In particular, this assures that rotations are performed in
the correct direction. Note that the (x,y) order of the
matrices quite naturally corresponds to the usual (row,column) order
for coordinates in the image.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Homogeneous projective transformation matrix.

**`px`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (x coordinate).

**`py`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (y coordinate).

**`pw`** (input_control)  number(-array) `→` MaybeSequence[Union[float, int]]

Input point (w coordinate).

**`qx`** (output_control)  number(-array) `→` Sequence[float]

Output point (x coordinate).

**`qy`** (output_control)  number(-array) `→` Sequence[float]

Output point (y coordinate).

**`qw`** (output_control)  number(-array) `→` Sequence[float]

Output point (w coordinate).

## Possible Predecessors

`vector_to_proj_hom_mat2d`,
`hom_vector_to_proj_hom_mat2d`,
`proj_match_points_ransac`,
`proj_match_points_ransac_guided`,
`hom_mat3d_project`

## See also

`projective_trans_image`,
`projective_trans_image_size`,
`projective_trans_region`,
`projective_trans_contour_xld`,
`projective_trans_pixel`

## Module

Foundation
