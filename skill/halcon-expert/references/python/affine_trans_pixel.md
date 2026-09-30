# affine_trans_pixel (Operator)

## Name

`affine_trans_pixel` — Apply an arbitrary affine 2D transformation to pixel coordinates.

## Signature

`def affine_trans_pixel(hom_mat_2d: Sequence[float], row: MaybeSequence[Union[float, int]], col: MaybeSequence[Union[float, int]]) -> Tuple[Sequence[float], Sequence[float]]`

`def affine_trans_pixel_s(hom_mat_2d: Sequence[float], row: MaybeSequence[Union[float, int]], col: MaybeSequence[Union[float, int]]) -> Tuple[float, float]`

## Description

`affine_trans_pixel` applies an arbitrary affine 2D transformation,
i.e., scaling, rotation, translation, and slant (skewing), to the input
pixels (*`row`*,*`col`*) and returns the resulting pixels in
(*`row_trans`*,*`col_trans`*); the input and output pixels are
subpixel precise coordinates. The affine transformation is described by the
homogeneous transformation matrix given in *`hom_mat_2d`*.

In contrast to [`affine_trans_point_2d`](affine_trans_point_2d.md), `affine_trans_pixel`
first converts the input coordinates from HALCON's standard coordinate
system (with the origin in the center of the upper left pixel) to a coordinate
system with the origin in the upper left corner of the upper left pixel. After
the transformation with *`hom_mat_2d`* the result is converted back to
the standard coordinate system.
This way, `affine_trans_pixel` is compatible with
[`affine_trans_image`](affine_trans_image.md), [`affine_trans_image_size`](affine_trans_image_size.md),
[`affine_trans_region`](affine_trans_region.md), [`affine_trans_contour_xld`](affine_trans_contour_xld.md), and
[`affine_trans_polygon_xld`](affine_trans_polygon_xld.md).

Applying `affine_trans_pixel` corresponds to the following chain of
transformations (input and output pixels as homogeneous vectors):

$$\begin{pmatrix} RowTrans \\ ColTrans \\ 1 \end{pmatrix} = \begin{bmatrix} 1 & 0 & -0.5 \\ 0 & 1 & -0.5 \\ 0 & 0 & 1 \end{bmatrix} \cdot HoMMat2D \cdot \begin{bmatrix} 1 & 0 & +0.5 \\ 0 & 1 & +0.5 \\ 0 & 0 & 1 \end{bmatrix} \cdot \begin{pmatrix} Row \\ Col \\ 1 \end{pmatrix}$$ ![figure](../assets/872f437a811bcdf8.svg)

Hence, `affine_trans_pixel(HomMat2D, Row, Col, RowTrans, ColTrans)`
corresponds to the following operator sequence:

|  |
| --- |
| [`affine_trans_point_2d(HomMat2D, Row+0.5, Col+0.5, RowTmp, ColTmp)`](affine_trans_point_2d.md) |
| `RowTrans := RowTmp-0.5` |
| `ColTrans := ColTmp-0.5` |

### Further Information

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on internal data level.

## Parameters

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`row`** (input_control)  point.x(-array) `→` MaybeSequence[Union[float, int]]

Input pixel(s) (row coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`col`** (input_control)  point.y(-array) `→` MaybeSequence[Union[float, int]]

Input pixel(s) (column coordinate).

Default:
64

Suggested values:
0, 16, 32, 64, 128, 256, 512, 1024

**`row_trans`** (output_control)  point.x(-array) `→` Sequence[float]

Output pixel(s) (row coordinate).

**`col_trans`** (output_control)  point.y(-array) `→` Sequence[float]

Output pixel(s) (column coordinate).

## Result

If the matrix *`hom_mat_2d`* represents an affine transformation
(i.e., not a projective transformation),
`affine_trans_pixel` returns 2 (
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

## Alternatives

`affine_trans_point_2d`

## Module

Foundation
