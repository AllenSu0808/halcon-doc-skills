# vector_angle_to_rigid (Operator)

## Name

`vector_angle_to_rigid` — Compute a rigid affine transformation from points and angles.

## Signature

`vector_angle_to_rigid( : : Row1, Column1, Angle1, Row2, Column2, Angle2 : HomMat2D)`

## Description

`vector_angle_to_rigid` computes a rigid affine transformation, i.e., a
transformation consisting of a rotation and a translation, from a point
correspondence and two corresponding angles and returns it as the
homogeneous transformation matrix *`HomMat2D`*. The matrix consists of 2
components: a rotation matrix R and a
translation vector t (also see
[`hom_mat2d_rotate`](hom_mat2d_rotate.md) and [`hom_mat2d_translate`](hom_mat2d_translate.md)):

$$\text{HomMat2D} = \begin{bmatrix} R & T \\ 0 & 1 \end{bmatrix} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \\ 0 & 0 \end{bmatrix} \cdot \begin{bmatrix} R \\ 0 \\ 0 \end{bmatrix} = H(T) \cdot H(R)$$ ![figure](../assets/0b9d6103538635fe.svg)

The coordinates of the original point are passed in
(*`Row1`*,*`Column1`*), while the corresponding angle is passed in
*`Angle1`*. The coordinates of the transformed point are passed in
(*`Row2`*,*`Column2`*), while the corresponding angle is passed in
*`Angle2`*. The following equation describes the transformation of the
point using homogeneous vectors:

$$\left(\begin{array}{c} \text{Row2} \\ \text{Column2} \\ 1 \end{array}\right) = \mathrm{HomMat2D} \cdot \left(\begin{array}{c} \text{Row1} \\ \text{Column1} \\ 1 \end{array}\right)$$ ![figure](../assets/350484f98e8f4fe0.svg)

In particular, the operator `vector_angle_to_rigid` is useful to
construct a rigid affine transformation from the results of the matching
operators (e.g., [`find_ncc_model`](find_ncc_model.md)),
which transforms a reference image to the current image or (if the parameters
are passed in reverse order) from the current image to the reference image.

*`HomMat2D`* can be used directly with operators that transform data
using affine transformations, e.g., [`affine_trans_image`](affine_trans_image.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Row1`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the original point.

**`Column1`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the original point.

**`Angle1`** (input_control)  angle.rad `→`  (real / integer)

Angle of the original point.

**`Row2`** (input_control)  point.y `→`  (real / integer)

Row coordinate of the transformed point.

**`Column2`** (input_control)  point.x `→`  (real / integer)

Column coordinate of the transformed point.

**`Angle2`** (input_control)  angle.rad `→`  (real / integer)

Angle of the transformed point.

**`HomMat2D`** (output_control)  hom_mat2d `→`  (real)

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

`get_ncc_model_region`

## Possible Successors

`hom_mat2d_invert`,
`affine_trans_image`,
`affine_trans_region`,
`affine_trans_contour_xld`,
`affine_trans_polygon_xld`,
`affine_trans_point_2d`

## Alternatives

`vector_to_rigid`

## See also

`vector_field_to_hom_mat2d`

## Module

Foundation
