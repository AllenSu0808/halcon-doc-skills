# AffineTransPolygonXld (Operator)

## Name

`AffineTransPolygonXld` — Apply an arbitrary affine transformation to XLD polygons.

## Signature

`static void HOperatorSet.AffineTransPolygonXld(HObject polygons, out HObject polygonsAffineTrans, HTuple homMat2D)`

`HXLDPoly HXLDPoly.AffineTransPolygonXld(HHomMat2D homMat2D)`

`HXLDPoly HHomMat2D.AffineTransPolygonXld(HXLDPoly polygons)`

## Description

`AffineTransPolygonXld` applies an arbitrary affine transformation,
i.e., scaling, rotation, translation, and slant (skewing), to the XLD
polygons given in *`polygons`* and returns the transformed polygons in
*`polygonsAffineTrans`*. The affine transformation is described by the
homogeneous transformation matrix given in *`homMat2D`*. This matrix can
be created using the operators [`HomMat2dIdentity`](hom_mat2d_identity.md),
[`HomMat2dScale`](hom_mat2d_scale.md), [`HomMat2dRotate`](hom_mat2d_rotate.md),
[`HomMat2dTranslate`](hom_mat2d_translate.md), etc., or be the result of operators like
[`VectorAngleToRigid`](vector_angle_to_rigid.md).

The components of the homogeneous transformation matrix are interpreted as
follows: The *row* coordinate of the image corresponds to x and
the *column* coordinate corresponds to y of the coordinate system in
which the transformation matrix was defined. This is necessary to obtain
a right-handed coordinate system for the image. In particular, this assures
that rotations are performed in the correct direction. Note that the
(x,y) order of the matrices quite naturally corresponds to the usual
(row,column) order for coordinates in the image.

## Attention

The XLD contours that are possibly referenced by *`polygons`*
are neither transformed nor stored with the output polygons, since
this is generally impossible without creating inconsistencies for
the attributes of the XLD contours. Hence, operators that access
the contours associated with a polygon, e.g.,
[`SplitContoursXld`](split_contours_xld.md) will not work correctly.

`AffineTransPolygonXld` does not use the HALCON standard
coordinate system (with the origin in the center of the upper left
pixel), but instead uses the same coordinate system as in
[`AffineTransPixel`](affine_trans_pixel.md), i.e., the origin lies in the upper
left corner of the upper left pixel. Therefore,
applying `AffineTransPolygonXld` corresponds to
a chain of transformations (see [`AffineTransPixel`](affine_trans_pixel.md)), which is
applied to each point of the polygon (input and output pixels as homogeneous
vectors).
As an effect, you might get unexpected results when creating affine
transformations based on coordinates that are derived from the
polygon, e.g., by operators like
[`AreaCenterXld`](area_center_xld.md). For example, if you use this operator to calculate
the center of gravity of a rotationally symmetric XLD polygon and then
rotate the polygon around this point using [`HomMat2dRotate`](hom_mat2d_rotate.md), the
resulting polygon will not lie on the original one. In such a case, you can
compensate this effect by applying the following translations to
*`homMat2D`* before using it in `AffineTransPolygonXld`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `affine_trans_polygon_xld(Polygons, PolygonsAffineTrans, HomMat2DAdapted)` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`polygons`** (input_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Input XLD polygons.

**`polygonsAffineTrans`** (output_object)  xld_poly(-array) `→` [HXLDPoly](HXLDPoly.md)

Transformed XLD polygons.

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

## Result

If the matrix *`homMat2D`* represents an affine transformation
(i.e., not a projective transformation),
`AffineTransPolygonXld` returns 2 (
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
`AffineTransRegion`,
`AffineTransContourXld`

## Module

Foundation
