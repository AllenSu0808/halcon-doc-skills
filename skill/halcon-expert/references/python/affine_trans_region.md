# affine_trans_region (Operator)

## Name

`affine_trans_region` — Apply an arbitrary affine 2D transformation to regions.

## Signature

`def affine_trans_region(region: HObject, hom_mat_2d: Sequence[float], interpolate: str) -> HObject`

## Description

`affine_trans_region` applies an arbitrary affine 2D
transformation, i.e., scaling, rotation, translation, and slant (skewing), to
the regions given in *`region`* and returns the transformed
regions in *`region_affine_trans`*. The affine transformation is
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

The parameter *`interpolate`* determines whether the transformation is
to be done by using interpolation internally. The interpolation modes
*"nearest_neighbor"* and *"constant"*, which are
described in detail for [`affine_trans_image`](affine_trans_image.md), can be used. An
interpolation can lead to smoother region boundaries, especially if regions
are enlarged. However, the runtime increases drastically.

## Attention

`affine_trans_region` in general is not reversible
(clipping and discretization during rotation and scaling).

`affine_trans_region` does not use the HALCON standard
coordinate system (with the origin in the center of the upper left
pixel), but instead uses the same coordinate system as in
[`affine_trans_pixel`](affine_trans_pixel.md), i.e., the origin lies in the upper
left corner of the upper left pixel. Therefore,
applying `affine_trans_region` corresponds to
a chain of transformations (see [`affine_trans_pixel`](affine_trans_pixel.md)), which is
applied to each point of the region (input and output pixels as
homogeneous vectors).
As an effect, you might get unexpected results when creating affine
transformations based on coordinates that are derived from the
region, e.g., by operators like
[`area_center`](area_center.md). For example, if you use this operator to calculate
the center of gravity of a rotationally symmetric region and then rotate
the region around this point using [`hom_mat2d_rotate`](hom_mat2d_rotate.md), the resulting
region will not lie on the original one. In such a case, you can compensate
this effect by applying the following translations to *`hom_mat_2d`*
before using it in `affine_trans_region`:

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

**`region`** (input_object)  region(-array) `→` HObject

Region(s) to be rotated and scaled.

**`region_affine_trans`** (output_object)  region(-array) `→` HObject

Transformed output region(s).

Number of elements:
RegionAffineTrans == Region

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Input transformation matrix.

**`interpolate`** (input_control)  string `→` str

Should the transformation be done using interpolation?

Default:
"nearest_neighbor"

List of values:
"constant", "nearest_neighbor"

## Result

If the matrix *`hom_mat_2d`* represents an affine transformation
(i.e., not a projective transformation), `affine_trans_region`
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

`hom_mat2d_identity`,
`hom_mat2d_scale`,
`hom_mat2d_translate`,
`hom_mat2d_invert`,
`hom_mat2d_rotate`,
`hom_mat2d_reflect`

## Possible Successors

`select_shape`

## Alternatives

`move_region`,
`mirror_region`,
`zoom_region`

## See also

`affine_trans_image`

## Module

Foundation
