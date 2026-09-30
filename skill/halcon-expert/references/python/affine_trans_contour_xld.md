# affine_trans_contour_xld (Operator)

## Name

`affine_trans_contour_xld` — Apply an arbitrary affine 2D transformation to XLD contours.

## Signature

`def affine_trans_contour_xld(contours: HObject, hom_mat_2d: Sequence[float]) -> HObject`

## Description

`affine_trans_contour_xld` applies an arbitrary affine 2D
transformation, i.e., scaling, rotation, translation, and slant (skewing), to
the XLD contours given in *`contours`* and returns the transformed
contours in *`contours_affine_trans`*. The affine transformation is
described by the homogeneous transformation matrix given in
*`hom_mat_2d`*, which can be created using the operators
[`hom_mat2d_identity`](hom_mat2d_identity.md), [`hom_mat2d_scale`](hom_mat2d_scale.md),
[`hom_mat2d_rotate`](hom_mat2d_rotate.md), [`hom_mat2d_translate`](hom_mat2d_translate.md), etc., or be the result
of operators like [`vector_angle_to_rigid`](vector_angle_to_rigid.md).

The components of the homogeneous transformation matrix are interpreted as
follows: The *row* coordinate of the image corresponds to x and
the *column* coordinate corresponds to y of the coordinate system in
which the transformation matrix was defined. This is necessary to obtain
a right-handed coordinate system for the image. In particular, this assures
that rotations are performed in the correct direction. Note that the
(x,y) order of the matrices quite naturally corresponds to the usual
(row,column) order for coordinates in the image.

## Attention

`affine_trans_contour_xld` does not use the HALCON standard
coordinate system (with the origin in the center of the upper left
pixel), but instead uses the same coordinate system as in
[`affine_trans_pixel`](affine_trans_pixel.md), i.e., the origin lies in the upper
left corner of the upper left pixel. Therefore,
applying `affine_trans_contour_xld` corresponds to
a chain of transformations (see [`affine_trans_pixel`](affine_trans_pixel.md)), which is applied
to each point of the contour (input and output pixels as homogeneous
vectors). As an effect, you might get unexpected results when creating affine
transformations based on coordinates that are derived from the
contour, e.g., by operators like
[`area_center_xld`](area_center_xld.md). For example, if you use this operator to calculate
the center of gravity of a rotationally symmetric XLD contour and then rotate
the contour around this point using [`hom_mat2d_rotate`](hom_mat2d_rotate.md), the resulting
contour will not lie on the original one. In such a case, you can compensate
this effect by applying the following translations to *`hom_mat_2d`*
before using it in `affine_trans_contour_xld`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `affine_trans_contour_xld(Contours, ContoursAffineTrans, HomMat2DAdapted)` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Input XLD contours.

**`contours_affine_trans`** (output_object)  xld_cont(-array) `→` HObject

Transformed XLD contours.

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

## Result

If the matrix *`hom_mat_2d`* represents an affine transformation
(i.e., not a projective transformation),
`affine_trans_contour_xld` returns 2 (
H_MSG_TRUE)
. If the input is
empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`hom_mat2d_identity`,
`hom_mat2d_translate`,
`hom_mat2d_rotate`,
`hom_mat2d_scale`,
`hom_mat2d_reflect`

## See also

`affine_trans_image`,
`affine_trans_region`

## Module

Foundation
