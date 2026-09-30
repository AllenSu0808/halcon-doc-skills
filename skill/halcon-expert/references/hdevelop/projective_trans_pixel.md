# projective_trans_pixel (Operator)

## Name

`projective_trans_pixel` — Project pixel coordinates using a homogeneous projective
transformation matrix.

## Signature

`projective_trans_pixel( : : HomMat2D, Row, Col : RowTrans, ColTrans)`

## Description

`projective_trans_pixel` applies the homogeneous projective
transformation matrix *`HomMat2D`* to all input pixels
(*`Row`*,*`Col`*) and returns an array of output pixels
(*`RowTrans`*,*`ColTrans`*). The transformation is
described by the homogeneous transformation matrix given in
*`HomMat2D`*.

The difference between `projective_trans_pixel` and
[`projective_trans_point_2d`](projective_trans_point_2d.md) lies in the used coordinate
system: `projective_trans_pixel` uses a coordinate system with
origin in the upper left corner of the image, while
[`projective_trans_point_2d`](projective_trans_point_2d.md) uses the standard image coordinate
system, whose origin lies in the middle of the upper left pixel and
which is also used by operators like [`area_center`](area_center.md).

`projective_trans_pixel` corresponds to the following steps
(input and output points as homogeneous vectors):
$$\begin{pmatrix} \mathrm{RTrans} \\ \mathrm{CTrans} \\ \mathrm{WTrans} \end{pmatrix} = \mathrm{HomMat2D} \cdot \begin{pmatrix} \mathrm{Row} \\ \mathrm{Col} \\ 1 \end{pmatrix} \\ \begin{pmatrix} \mathrm{RTrans} \\ \mathrm{WTrans} \\ \mathrm{CTrans} \\ \mathrm{WTrans} \end{pmatrix} = \begin{pmatrix} \frac{\mathrm{RTrans}}{\mathrm{WTrans}} \\ \mathrm{CTrans} \\ \mathrm{WTrans} \\ \mathrm{WTrans} \end{pmatrix}$$ ![figure](../assets/8aca13c0098d86cd.svg)

If a point at infinity (`WTrans` = 0) is created by the
transformation, an error is returned.

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Homogeneous projective transformation matrix.

**`Row`** (input_control)  point.x(-array) `→`  (real / integer)

Input pixel(s) (row coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`Col`** (input_control)  point.y(-array) `→`  (real / integer)

Input pixel(s) (column coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`RowTrans`** (output_control)  point.x(-array) `→`  (real)

Output pixel(s) (row coordinate).

**`ColTrans`** (output_control)  point.y(-array) `→`  (real)

Output pixel(s) (column coordinate).

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
`projective_trans_point_2d`

## Module

Foundation
