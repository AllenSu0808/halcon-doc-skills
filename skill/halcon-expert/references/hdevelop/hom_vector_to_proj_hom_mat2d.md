# hom_vector_to_proj_hom_mat2d (Operator)

## Name

`hom_vector_to_proj_hom_mat2d` — Compute a homogeneous transformation matrix using given point
correspondences.

## Signature

`hom_vector_to_proj_hom_mat2d( : : Px, Py, Pw, Qx, Qy, Qw, Method : HomMat2D)`

## Description

`hom_vector_to_proj_hom_mat2d` determines the homogeneous
projective transformation matrix *`HomMat2D`* that optimally
fulfills the following equations given by at least 4 point
correspondences
$$\mathrm{HomMat2D} \cdot \begin{pmatrix} P_x \\ P_y \\ P_w \end{pmatrix} = \begin{pmatrix} Q_x \\ Q_y \\ Q_w \end{pmatrix}$$ ![figure](../assets/c952baa8c4158336.svg)
If fewer than 4 pairs of points
(*`Px`*,*`Py`*,*`Pw`*),
(*`Qx`*,*`Qy`*,*`Qw`*) are given, there exists no
unique solution, if exactly 4 pairs are supplied the matrix
*`HomMat2D`* transforms them in exactly the desired way, and if
there are more than 4 point pairs given,
`hom_vector_to_proj_hom_mat2d` seeks to minimize the
transformation error. To achieve such a minimization, two different
algorithms are available. The algorithm to use can be chosen using
the parameter *`Method`*. For conventional geometric problems
*`Method`*=*'normalized_dlt'* usually yields better
results. However, if one of the coordinates *`Qw`* or
*`Pw`* equals *0*, *`Method`*=*'dlt'* must
be chosen.

In contrast to [`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md),
`hom_vector_to_proj_hom_mat2d` uses homogeneous coordinates
for the points, and hence points at infinity (*`Pw`* =
*0* or *`Qw`* = *0*) can be used to determine
the transformation. If finite points are used, typically
*`Pw`* and *`Qw`* are set to *1*. In this case,
[`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md) can also be used.
[`vector_to_proj_hom_mat2d`](vector_to_proj_hom_mat2d.md) has the advantage that one
additional optimization method can be used and that the covariances
of the points can be taken into account. If the correspondence
between the points has not been determined,
[`proj_match_points_ransac`](proj_match_points_ransac.md) should be used to determine the
correspondence as well as the transformation.

If the points to transform are specified in standard image
coordinates, their *row* coordinates must be passed in
*`Px`* and their *column* coordinates in *`Py`*. This
is necessary to obtain a right-handed coordinate system for the
image. In particular, this assures that rotations are performed in
the correct direction. Note that the (x,y) order of the
matrices quite naturally corresponds to the usual (row,column) order
for coordinates in the image.

## Attention

It should be noted that homogeneous transformation matrices refer to
a general right-handed mathematical coordinate system. If a
homogeneous transformation matrix is used to transform images,
regions, XLD contours, or any other data that has been extracted
from images, the row coordinates of the transformation must be
passed in the x coordinates, while the column coordinates must be
passed in the y coordinates. Consequently, the order of passing row
and column coordinates follows the usual order
(`Row`,`Column`). This convention is essential to
obtain a right-handed coordinate system for the transformation of
iconic data, and consequently to ensure in particular that rotations
are performed in the correct mathematical direction.

Furthermore, it should be noted that if a homogeneous transformation
matrix is used to transform images, regions, XLD contours, or any
other data that has been extracted from images, it is assumed that
the origin of the coordinate system of the homogeneous
transformation matrix lies in the upper left corner of a pixel. The
image processing operators that return point coordinates, however,
assume a coordinate system in which the origin lies in the center of
a pixel. Therefore, to obtain a consistent homogeneous
transformation matrix, 0.5 must be added to the point coordinates
before computing the transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Px`** (input_control)  number-array `→`  (real / integer)

Input points 1 (x coordinate).

**`Py`** (input_control)  number-array `→`  (real / integer)

Input points 1 (y coordinate).

**`Pw`** (input_control)  number-array `→`  (real / integer)

Input points 1 (w coordinate).

**`Qx`** (input_control)  number-array `→`  (real)

Input points 2 (x coordinate).

**`Qy`** (input_control)  number-array `→`  (real)

Input points 2 (y coordinate).

**`Qw`** (input_control)  number-array `→`  (real)

Input points 2 (w coordinate).

**`Method`** (input_control)  string `→`  (string)

Estimation algorithm.

Default:
'normalized_dlt'

List of values:
'dlt', 'normalized_dlt'

**`HomMat2D`** (output_control)  hom_mat2d `→`  (real)

Homogeneous projective transformation matrix.

## Possible Predecessors

`proj_match_points_ransac`,
`proj_match_points_ransac_guided`,
`points_foerstner`,
`points_harris`

## Possible Successors

`projective_trans_image`,
`projective_trans_image_size`,
`projective_trans_region`,
`projective_trans_contour_xld`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## Alternatives

`vector_to_proj_hom_mat2d`,
`proj_match_points_ransac`,
`proj_match_points_ransac_guided`

## References

Richard Hartley, Andrew Zisserman: “Multiple View Geometry in
Computer Vision”; Cambridge University Press, Cambridge; 2000.
  
Olivier Faugeras, Quang-Tuan Luong: “The Geometry of Multiple
Images: The Laws That Govern the Formation of Multiple Images of a
Scene and Some of Their Applications”; MIT Press, Cambridge, MA;
2001.

## Module

Calibration
