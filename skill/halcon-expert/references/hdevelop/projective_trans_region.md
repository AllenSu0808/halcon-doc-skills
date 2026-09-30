# projective_trans_region (Operator)

## Name

`projective_trans_region` — Apply a projective transformation to a region.

## Signature

`projective_trans_region(Regions : TransRegions : HomMat2D, Interpolation : )`

## Description

`projective_trans_region` applies the projective
transformation specified by the homogeneous matrix *`HomMat2D`*
on the regions in *`Regions`* and returns the transformed
regions in *`TransRegions`*.

For creation and interpretation details of this matrix see also
[`projective_trans_image`](projective_trans_image.md).

If *'clip_region'* is set to its default value
*'true'* by `set_system('clip_region', 'true')` or if
the transformation is degenerated and thus produces infinite
regions, the output region is clipped by the rectangle with upper
left corner (0, 0) and lower right corner (*'width'*,
*'height'*), where *'width'* and *'height'* are
system variables (see also [`get_system`](get_system.md)). If
*'clip_region'* is *'false'*, the output region is not
clipped except by the maximum supported coordinate size.
See the `“Installation Guide”` for further information about
coordinate range limitations.
This may result in extremely memory and time intensive computations,
so use with care.

## Attention

The used coordinate system is the same as in [`affine_trans_pixel`](affine_trans_pixel.md). This
means that in fact not *`HomMat2D`* is applied but a modified
version. Therefore, applying `projective_trans_region` corresponds to
the following chain of transformations, which is applied to each point
$(Row_{i},Col_{i})$ of the region (input and output
pixels as homogeneous vectors):

$$\left(\begin{array}{c}RowTrans_{i} \\\ColTrans_{i} \\\ 1\end{array}\right) = \left[\begin{array}{ccc}1 & 0 & -0.5 \\0 & 1 & -0.5 \\0 & 0 & 1\end{array}\right] \cdot \text{HomMat2D} \cdot \left[\begin{array}{ccc}1 & 0 & +0.5 \\0 & 1 & +0.5 \\0 & 0 & 1\end{array}\right] \cdot \left(\begin{array}{c}Row_i \\Col_i \\ 1\end{array}\right)$$ ![figure](../assets/f9a1b905f5066ea4.svg)

As an effect, you might get unexpected results when creating projective
transformations based on coordinates that are derived from the
region, e.g., by operators like
[`area_center`](area_center.md). For example, if you use this operator to calculate
the center of gravity of a rotationally symmetric region and then rotate
the region around this point using [`hom_mat2d_rotate`](hom_mat2d_rotate.md), the resulting
region will not lie on the original one. In such a case, you can compensate
this effect by applying the following translations to *`HomMat2D`*
before using it in `projective_trans_region`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `projective_trans_region(Region, TransRegion, HomMat2DAdapted, 'bilinear')` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Automatically parallelized on tuple level.

## Parameters

**`Regions`** (input_object)  region(-array) `→` object

Input regions.

**`TransRegions`** (output_object)  region(-array) `→` object

Output regions.

**`HomMat2D`** (input_control)  hom_mat2d `→`  (real)

Homogeneous projective transformation matrix.

**`Interpolation`** (input_control)  string `→`  (string)

Interpolation method for the transformation.

Default:
'bilinear'

List of values:
'bilinear', 'nearest_neighbor'

## Possible Predecessors

`vector_to_proj_hom_mat2d`,
`hom_vector_to_proj_hom_mat2d`,
`proj_match_points_ransac`,
`proj_match_points_ransac_guided`,
`hom_mat3d_project`

## See also

`projective_trans_image`,
`projective_trans_image_size`,
`projective_trans_contour_xld`,
`projective_trans_point_2d`,
`projective_trans_pixel`

## Module

Foundation
