# projective_trans_contour_xld (Operator)

## Name

`projective_trans_contour_xld` — Apply a projective transformation to an XLD contour.

## Signature

`def projective_trans_contour_xld(contours: HObject, hom_mat_2d: Sequence[float]) -> HObject`

## Description

`projective_trans_contour_xld` applies the projective
transformation specified by the homogeneous matrix *`hom_mat_2d`*
on the contours in *`contours`* and returns the transformed
contours in *`contours_proj_trans`*.

For creation and interpretation details of this matrix see also
[`projective_trans_image`](projective_trans_image.md).

## Attention

The used coordinate system is the same as in [`affine_trans_pixel`](affine_trans_pixel.md). This
means that in fact not *`hom_mat_2d`* is applied but a modified
version. Therefore, applying `projective_trans_contour_xld` corresponds to
the following chain of transformations, which is applied to each point
$(Row_{i},Col_{i})$ of the contour (input and output
pixels as homogeneous vectors):

$$\left(\begin{array}{c}RowTrans_{i} \\\ColTrans_{i} \\\ 1\end{array}\right) = \left[\begin{array}{ccc}1 & 0 & -0.5 \\0 & 1 & -0.5 \\0 & 0 & 1\end{array}\right] \cdot \text{HomMat2D} \cdot \left[\begin{array}{ccc}1 & 0 & +0.5 \\0 & 1 & +0.5 \\0 & 0 & 1\end{array}\right] \cdot \left(\begin{array}{c}Row_i \\Col_i \\ 1\end{array}\right)$$ ![figure](../assets/f9a1b905f5066ea4.svg)

As an effect, you might get unexpected results when creating projective
transformations based on coordinates that are derived from the
contour, e.g., by operators like
[`area_center_xld`](area_center_xld.md). For example, if you use this operator to calculate
the center of gravity of a rotationally symmetric XLD contour and then rotate
the contour around this point using [`hom_mat2d_rotate`](hom_mat2d_rotate.md), the resulting
contour will not lie on the original one. In such a case, you can compensate
this effect by applying the following translations to *`hom_mat_2d`*
before using it in `projective_trans_contour_xld`:

|  |
| --- |
| `hom_mat2d_translate(HomMat2D, 0.5, 0.5, HomMat2DTmp)` |
| `hom_mat2d_translate_local(HomMat2DTmp, -0.5, -0.5, HomMat2DAdapted)` |
| `projective_trans_contour_xld(Contours, ContoursAffineTrans, HomMat2DAdapted)` |

For an explanation of the different 2D coordinate systems
used in HALCON, see the introduction of chapter
[Transformations / 2D Transformations](toc_transformations_2dtransformations.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`contours`** (input_object)  xld_cont(-array) `→` HObject

Input contours.

**`contours_proj_trans`** (output_object)  xld_cont(-array) `→` HObject

Output contours.

**`hom_mat_2d`** (input_control)  hom_mat2d `→` Sequence[float]

Homogeneous projective transformation matrix.

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
`projective_trans_point_2d`,
`projective_trans_pixel`

## Module

Foundation
