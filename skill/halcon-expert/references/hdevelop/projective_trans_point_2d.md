# projective_trans_point_2d (Operator)

## Name

`projective_trans_point_2d` — Project a homogeneous 2D point using a projective transformation
matrix.

## Signature

`projective_trans_point_2d( : : HomMat2D, Px, Py, Pw : Qx, Qy, Qw)`

## Description

`projective_trans_point_2d` applies the homogeneous projective
transformation matrix *`HomMat2D`* to all homogeneous input
points (*`Px`*,*`Py`*,*`Pw`*) and returns an array of
homogeneous output points (*`Qx`*,*`Qy`*,*`Qw`*). The
transformation is described by the homogeneous transformation matrix
given in *`HomMat2D`*. This corresponds to the following
equation (input and output points as homogeneous vectors):

$$\begin{pmatrix}Q_x \\ Q_y \\ Q_w\end{pmatrix}=\mathrm{HomMat2D}\cdot \begin{pmatrix}P_x \\ P_y \\ P_w\end{pmatrix}$$ ![figure](../assets/577384673df19c8d.svg)

To transform the homogeneous coordinates to Euclidean coordinates,
they have to be divided by *`Qw`*:
$$\begin{pmatrix}Ex \\ Ey\end{pmatrix} = \begin{pmatrix}\frac{Qx}{Qw} \\ \frac{Qy}{Qw}\end{pmatrix}$$ ![figure](../assets/d34e9b0ceb4d1677.svg)

If the points to transform are specified in standard image
coordinates, their *row* coordinates must be passed in
*`Px`* and their *column* coordinates in *`Py`*. This
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

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Homogeneous projective transformation matrix.

**`Px`** (input_control)  number(-array) `→`  (real / integer)

Input point (x coordinate).

**`Py`** (input_control)  number(-array) `→`  (real / integer)

Input point (y coordinate).

**`Pw`** (input_control)  number(-array) `→`  (real / integer)

Input point (w coordinate).

**`Qx`** (output_control)  number(-array) `→`  (real)

Output point (x coordinate).

**`Qy`** (output_control)  number(-array) `→`  (real)

Output point (y coordinate).

**`Qw`** (output_control)  number(-array) `→`  (real)

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
