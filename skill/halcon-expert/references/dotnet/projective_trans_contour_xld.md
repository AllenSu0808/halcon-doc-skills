# ProjectiveTransContourXld (Operator)

## Name

`ProjectiveTransContourXld` — Apply a projective transformation to an XLD contour.

## Signature

`static void HOperatorSet.ProjectiveTransContourXld(HObject contours, out HObject contoursProjTrans, HTuple homMat2D)`

`HXLDCont HXLDCont.ProjectiveTransContourXld(HHomMat2D homMat2D)`

`HXLDCont HHomMat2D.ProjectiveTransContourXld(HXLDCont contours)`

## Description

`ProjectiveTransContourXld` applies the projective
transformation specified by the homogeneous matrix *`homMat2D`*
on the contours in *`contours`* and returns the transformed
contours in *`contoursProjTrans`*.

For creation and interpretation details of this matrix see also
[`ProjectiveTransImage`](projective_trans_image.md).

## Attention

The used coordinate system is the same as in [`AffineTransPixel`](affine_trans_pixel.md). This
means that in fact not *`homMat2D`* is applied but a modified
version. Therefore, applying `ProjectiveTransContourXld` corresponds to
the following chain of transformations, which is applied to each point
$(Row_{i},Col_{i})$ of the contour (input and output
pixels as homogeneous vectors):

$$\left(\begin{array}{c}RowTrans_{i} \\\ColTrans_{i} \\\ 1\end{array}\right) = \left[\begin{array}{ccc}1 & 0 & -0.5 \\0 & 1 & -0.5 \\0 & 0 & 1\end{array}\right] \cdot \text{HomMat2D} \cdot \left[\begin{array}{ccc}1 & 0 & +0.5 \\0 & 1 & +0.5 \\0 & 0 & 1\end{array}\right] \cdot \left(\begin{array}{c}Row_i \\Col_i \\ 1\end{array}\right)$$ ![figure](../assets/f9a1b905f5066ea4.svg)

As an effect, you might get unexpected results when creating projective
transformations based on coordinates that are derived from the
contour, e.g., by operators like
[`AreaCenterXld`](area_center_xld.md). For example, if you use this operator to calculate
the center of gravity of a rotationally symmetric XLD contour and then rotate
the contour around this point using [`HomMat2dRotate`](hom_mat2d_rotate.md), the resulting
contour will not lie on the original one. In such a case, you can compensate
this effect by applying the following translations to *`homMat2D`*
before using it in `ProjectiveTransContourXld`:

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

**`contours`** (input_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Input contours.

**`contoursProjTrans`** (output_object)  xld_cont(-array) `→` [HXLDCont](HXLDCont.md)

Output contours.

**`homMat2D`** (input_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Homogeneous projective transformation matrix.

## Possible Predecessors

`VectorToProjHomMat2d`,
`HomVectorToProjHomMat2d`,
`ProjMatchPointsRansac`,
`ProjMatchPointsRansacGuided`,
`HomMat3dProject`

## See also

`ProjectiveTransImage`,
`ProjectiveTransImageSize`,
`ProjectiveTransRegion`,
`ProjectiveTransPoint2d`,
`ProjectiveTransPixel`

## Module

Foundation
