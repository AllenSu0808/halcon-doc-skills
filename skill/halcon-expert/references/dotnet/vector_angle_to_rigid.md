# VectorAngleToRigid (Operator)

## Name

`VectorAngleToRigid` — Compute a rigid affine transformation from points and angles.

## Signature

`static void HOperatorSet.VectorAngleToRigid(HTuple row1, HTuple column1, HTuple angle1, HTuple row2, HTuple column2, HTuple angle2, out HTuple homMat2D)`

`void HHomMat2D.VectorAngleToRigid(HTuple row1, HTuple column1, HTuple angle1, HTuple row2, HTuple column2, HTuple angle2)`

`void HHomMat2D.VectorAngleToRigid(double row1, double column1, double angle1, double row2, double column2, double angle2)`

## Description

`VectorAngleToRigid` computes a rigid affine transformation, i.e., a
transformation consisting of a rotation and a translation, from a point
correspondence and two corresponding angles and returns it as the
homogeneous transformation matrix *`homMat2D`*. The matrix consists of 2
components: a rotation matrix R and a
translation vector t (also see
[`HomMat2dRotate`](hom_mat2d_rotate.md) and [`HomMat2dTranslate`](hom_mat2d_translate.md)):

$$\text{HomMat2D} = \begin{bmatrix} R & T \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix} \cdot \begin{bmatrix} R \\ 0 \\ 0 \end{bmatrix} = H(T) \cdot H(R)$$ ![figure](../assets/0b9d6103538635fe.svg)

The coordinates of the original point are passed in
(*`row1`*,*`column1`*), while the corresponding angle is passed in
*`angle1`*. The coordinates of the transformed point are passed in
(*`row2`*,*`column2`*), while the corresponding angle is passed in
*`angle2`*. The following equation describes the transformation of the
point using homogeneous vectors:

$$\left(\begin{array}{c} \text{Row2} \\ \text{Column2} \\ 1 \end{array}\right) = \mathrm{HomMat2D} \cdot \left(\begin{array}{c} \text{Row1} \\ \text{Column1} \\ 1 \end{array}\right)$$ ![figure](../assets/350484f98e8f4fe0.svg)

In particular, the operator `VectorAngleToRigid` is useful to
construct a rigid affine transformation from the results of the matching
operators (e.g., [`FindNccModel`](find_ncc_model.md)),
which transforms a reference image to the current image or (if the parameters
are passed in reverse order) from the current image to the reference image.

*`homMat2D`* can be used directly with operators that transform data
using affine transformations, e.g., [`AffineTransImage`](affine_trans_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`row1`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the original point.

**`column1`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the original point.

**`angle1`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Angle of the original point.

**`row2`** (input_control)  point.y `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinate of the transformed point.

**`column2`** (input_control)  point.x `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinate of the transformed point.

**`angle2`** (input_control)  angle.rad `→` [HTuple](HTuple.md) (*double* / int / long)

Angle of the transformed point.

**`homMat2D`** (output_control)  hom_mat2d `→` [HHomMat2D](HHomMat2D.md), [HTuple](HTuple.md) (*double*)

Output transformation matrix.

## Example (HDevelop)

```
read_image (Image, 'face_masks/face_mask_01')
* Prepare NCC matching.
gen_rectangle2 (ROI, 616.5, 708.5, rad(-82.4054), 50, 35)
reduce_domain (Image, ROI, ImageReduced)
create_ncc_model (ImageReduced, 'auto', rad(0), rad(360), 'auto',\
                  'use_polarity', ModelID)
read_image (SearchImage, 'face_masks/face_mask_02')
find_ncc_model (SearchImage, ModelID, rad(0), rad(360), 0.7, 1, 0.5,\
                'true', 0, Row, Column, Angle, Score)
get_ncc_model_region (ModelRegion, ModelID)
gen_contour_region_xld (ModelRegion, ModelContours, 'border_holes')
* Create transformation matrix for found match.
vector_angle_to_rigid (0, 0, 0, Row, Column, Angle, HomMat2D)
affine_trans_contour_xld (ModelContours, ContoursAffineTrans, HomMat2D)
```

## Possible Predecessors

`GetNccModelRegion`

## Possible Successors

`HomMat2dInvert`,
`AffineTransImage`,
`AffineTransRegion`,
`AffineTransContourXld`,
`AffineTransPolygonXld`,
`AffineTransPoint2d`

## Alternatives

`VectorToRigid`

## See also

`VectorFieldToHomMat2d`

## Module

Foundation
