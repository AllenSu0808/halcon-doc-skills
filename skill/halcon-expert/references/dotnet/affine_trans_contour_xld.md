# AffineTransContourXld (Operator)

## Name

`AffineTransContourXld` — Apply an arbitrary affine 2D transformation to XLD contours.

## Signature

`static void HOperatorSet.AffineTransContourXld(HObject contours, out HObject contoursAffineTrans, HTuple homMat2D)`

`HXLDCont HXLDCont.AffineTransContourXld(HHomMat2D homMat2D)`

`HXLDCont HHomMat2D.AffineTransContourXld(HXLDCont contours)`

## Description

`AffineTransContourXld` applies an arbitrary affine 2D
transformation, i.e., scaling, rotation, translation, and slant (skewing), to
the XLD contours given in *`contours`* and returns the transformed
contours in *`contoursAffineTrans`*. The affine transformation is
described by the homogeneous transformation matrix given in
*`homMat2D`*, which can be created using the operators
[`HomMat2dIdentity`](hom_mat2d_identity.md), [`HomMat2dScale`](hom_mat2d_scale.md),
[`HomMat2dRotate`](hom_mat2d_rotate.md), [`HomMat2dTranslate`](hom_mat2d_translate.md), etc., or be the result
of operators like [`VectorAngleToRigid`](vector_angle_to_rigid.md).

The components of the homogeneous transformation matrix are interpreted as
follows: The *row* coordinate of the image corresponds to x and
the *column* coordinate corresponds to y of the coordinate system in
which the transformation matrix was defined. This is necessary to obtain
a right-handed coordinate system for the image. In particular, this assures
that rotations are performed in the correct direction. Note that the
(x,y) order of the matrices quite naturally corresponds to the usual
(row,column) order for coordinates in the image.

## Attention

`AffineTransContourXld` does not use the HALCON standard
coordinate system (with the origin in the center of the upper left
pixel), but instead uses the same coordinate system as in
[`AffineTransPixel`](affine_trans_pixel.md), i.e., the origin lies in the upper
left corner of the upper left pixel. Therefore,
applying `AffineTransContourXld` corresponds to
a chain of transformations (see [`AffineTransPixel`](affine_trans_pixel.md)), which is applied
to each point of the contour (input and output pixels as homogeneous
vectors). As an effect, you might get unexpected results when creating affine
transformations based on coordinates that are derived from the
contour, e.g., by operators like
[`AreaCenterXld`](area_center_xld.md). For example, if you use this operator to calculate
the center of gravity of a rotationally symmetric XLD contour and then rotate
the contour around this point using [`HomMat2dRotate`](hom_mat2d_rotate.md), the resulting
contour will not lie on the original one. In such a case, you can compensate
this effect by applying the following translations to *`homMat2D`*
before using it in `AffineTransContourXld`:

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

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input XLD contours.

**`contoursAffineTrans`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Transformed XLD contours.

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

## Result

If the matrix *`homMat2D`* represents an affine transformation
(i.e., not a projective transformation),
`AffineTransContourXld` returns 2 (
H_MSG_TRUE)
. If the input is
empty the behavior can be set via
`set_system(::'no_object_result',<Result>:)`. If necessary,
an exception is raised.

## Possible Predecessors

`HomMat2dIdentity`,
`HomMat2dTranslate`,
`HomMat2dRotate`,
`HomMat2dScale`,
`HomMat2dReflect`

## See also

`AffineTransImage`,
`AffineTransRegion`

## Module

Foundation
