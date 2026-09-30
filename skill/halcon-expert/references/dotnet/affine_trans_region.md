# AffineTransRegion (Operator)

## Name

`AffineTransRegion` — Apply an arbitrary affine 2D transformation to regions.

## Signature

`static void HOperatorSet.AffineTransRegion(HObject region, out HObject regionAffineTrans, HTuple homMat2D, HTuple interpolate)`

`HRegion HRegion.AffineTransRegion(HHomMat2D homMat2D, string interpolate)`

`HRegion HHomMat2D.AffineTransRegion(HRegion region, string interpolate)`

## Description

`AffineTransRegion` applies an arbitrary affine 2D
transformation, i.e., scaling, rotation, translation, and slant (skewing), to
the regions given in *`region`* and returns the transformed
regions in *`regionAffineTrans`*. The affine transformation is
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

The parameter *`interpolate`* determines whether the transformation is
to be done by using interpolation internally. The interpolation modes
*"nearest_neighbor"* and *"constant"*, which are
described in detail for [`AffineTransImage`](affine_trans_image.md), can be used. An
interpolation can lead to smoother region boundaries, especially if regions
are enlarged. However, the runtime increases drastically.

## Attention

`AffineTransRegion` in general is not reversible
(clipping and discretization during rotation and scaling).

`AffineTransRegion` does not use the HALCON standard
coordinate system (with the origin in the center of the upper left
pixel), but instead uses the same coordinate system as in
[`AffineTransPixel`](affine_trans_pixel.md), i.e., the origin lies in the upper
left corner of the upper left pixel. Therefore,
applying `AffineTransRegion` corresponds to
a chain of transformations (see [`AffineTransPixel`](affine_trans_pixel.md)), which is
applied to each point of the region (input and output pixels as
homogeneous vectors).
As an effect, you might get unexpected results when creating affine
transformations based on coordinates that are derived from the
region, e.g., by operators like
[`AreaCenter`](area_center.md). For example, if you use this operator to calculate
the center of gravity of a rotationally symmetric region and then rotate
the region around this point using [`HomMat2dRotate`](hom_mat2d_rotate.md), the resulting
region will not lie on the original one. In such a case, you can compensate
this effect by applying the following translations to *`homMat2D`*
before using it in `AffineTransRegion`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `affine_trans_region(Region, RegionAffineTrans, HomMat2DAdapted, 'nearest_neighbor')` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.
- Automatically parallelized on internal data level.

## Parameters

**`region`** (input_object)  region(-array) `→` [HRegion](HRegion.md)

Region(s) to be rotated and scaled.

**`regionAffineTrans`** (output_object)  region(-array) `→` [HRegion](HRegion.md)

Transformed output region(s).

Number of elements:
RegionAffineTrans == Region

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Input transformation matrix.

**`interpolate`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Should the transformation be done using interpolation?

Default:
"nearest_neighbor"

List of values:
"constant", "nearest_neighbor"

## Result

If the matrix *`homMat2D`* represents an affine transformation
(i.e., not a projective transformation), `AffineTransRegion`
returns 2 (
H_MSG_TRUE)
. The behavior in case of empty input (no regions
given) can be set via
`set_system('no_object_result',<Result>)`, the behavior in
case of an empty input region via
`set_system('empty_region_result',<Result>)`, and the behavior
in case of an empty result region via
`set_system('store_empty_region',<'true'/'false'>)`. If
necessary, an exception is raised.

## Possible Predecessors

`HomMat2dIdentity`,
`HomMat2dScale`,
`HomMat2dTranslate`,
`HomMat2dInvert`,
`HomMat2dRotate`,
`HomMat2dReflect`

## Possible Successors

`SelectShape`

## Alternatives

`MoveRegion`,
`MirrorRegion`,
`ZoomRegion`

## See also

`AffineTransImage`

## Module

Foundation
