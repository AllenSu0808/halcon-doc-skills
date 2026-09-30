# align_metrology_model (Operator)

## Name

`align_metrology_model` — Alignment of a metrology model.

## Signature

`align_metrology_model( : : MetrologyHandle, Row, Column, Angle : )`

## Description

`align_metrology_model` moves and rotates the whole metrology model
*`MetrologyHandle`*
relative to the image coordinate system which has its origin in the
top left corner.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

An alignment ensures, that the position and
orientation of the metrology model is adapted to the
objects to be measured in the current image. The alignment is then
used by [`apply_metrology_model`](apply_metrology_model.md) to perform the measurement.
First the metrology model is rotated by *`Angle`*, then
the metrology model is translated by *`Row`* and *`Column`*.
The values of the alignment are overwritten by the
next call of `align_metrology_model`.

### Computation of the parameters of the alignment

The parameters of the alignment can be determined using diverse methods.
Here, three possibilities to determine the parameters are listed:

- **Using region analysis:** —

  If the metrology model can be extracted using region processing and if the
  pose of the Region changes only slightly in subsequent images, the
  parameters of the reference system of the metrology model and of the
  alignment can be derived using region analysis. In the following picture
  [`threshold`](threshold.md) and [`smallest_rectangle2`](smallest_rectangle2.md) were used to obtain
  these parameter.

  ![figure](../assets/f6b4ed1001b029a0.svg)

  The region extracted with [`threshold`](threshold.md) is shown in red.
  The rectangle computed with [`smallest_rectangle2`](smallest_rectangle2.md) is shown in green.

  1. Setting the reference system

     In the image in which the metrology model was defined, extract a region
     containing the metrology objects. The pose of this region with
     respect to the image coordinate system is determined and set
     as the reference system of the metrology model using
     [`set_metrology_model_param`](set_metrology_model_param.md).
     This step is only performed once when setting up the metrology model.

     *Example:*

     [`threshold(Image, Region, 0, 50)`](threshold.md)

     [`smallest_rectangle2(Region, RowOrig, ColumnOrig, AngleOrig,
     Length1, Length2)`](smallest_rectangle2.md)

     [`set_metrology_model_param(MetrologyHandle, 'reference_system',
     [RowOrig, ColumnOrig, AngleOrig])`](set_metrology_model_param.md)
  2. Determining the alignment

     In an image where the metrology model occurs in a different Pose, the
     current pose if the extracted region is determined. This pose is then
     used to align the metrology model.

     *Example:*

     [`threshold(CurrentImage, Region, 0, 50)`](threshold.md)

     [`smallest_rectangle2(Region, RowAlign, ColumnAlign, AngleAlign,
     Length1, Length2)`](smallest_rectangle2.md)

     `align_metrology_model(MetrologyHandle, RowAlign, ColumnAlign,
     AngleAlign)`
- **Using a shape model:** —

  If a shape model is used to align the metrology model,
  the reference system with respect to which the metrology objects are given
  has to be set so that it coincides with the coordinate system used by the
  shape model. Only then, the results
  (*'row'*, *'column'*, *'angle'*) of
  [`get_generic_shape_model_result`](get_generic_shape_model_result.md) can be used directly in
  `align_metrology_model` to align the metrology model in the current
  image. The individual steps that are needed, are shown below.

  |  |  |  |
  | --- | --- | --- |
  | ![figure](../assets/dfc740c134af69f4.svg) | ![figure](../assets/369645aa3dd71ac7.svg) | ![figure](../assets/ffd96ee19a5dc193.svg) |
  | ( 1) | ( 2) | ( 3) |

  (1) The contours of the metrology model (2) The contours of the shape model
  (3) The contours of the metrology model after setting the correct
  reference system.

  1. Setting the reference system

     In the image in which the metrology model was defined, the pose of the
     origin of the shape model is determined and set
     as the reference system of the metrology model using
     [`set_metrology_model_param`](set_metrology_model_param.md). This step is only performed once
     when setting up the metrology model.

     *Example:*

     [`train_generic_shape_model(Image, ModelID)`](train_generic_shape_model.md)

     [`area_center(Image, Area, RowOrig, ColumnOrig)`](area_center.md)

     [`set_metrology_model_param(MetrologyHandle, 'reference_system',
     [RowOrig,ColumnOrig,0])`](set_metrology_model_param.md)
  2. Determining the alignment

     In an image, in which the object to be measured occurs in a different
     pose, the current pose of the shape model is determined and set
     in the metrology model using `align_metrology_model`.

     *Example:*

     [`find_generic_shape_model(CurrentImage, ModelID, MatchResultID,
     NumMatchResult)`](find_generic_shape_model.md)

     [`get_generic_shape_model_result(MatchResultID, 'all', 'row',
     RowAlign)`](get_generic_shape_model_result.md)

     [`get_generic_shape_model_result(MatchResultID, 'all', 'column',
     ColumnAlign)`](get_generic_shape_model_result.md)

     [`get_generic_shape_model_result(MatchResultID, 'all', 'angle',
     AngleAlign)`](get_generic_shape_model_result.md)

     `align_metrology_model(MetrologyHandle, RowAlign, ColumnAlign,
     AngleAlign)`
- **Using a rigid 2D transformation:** —

  If certain model points (given as [PRowModel], [PColumnModel]) can be
  clearly identified and if they can still be clearly identified in further
  images in which the objects to be measured can occur shifted or rotated,
  a rigid transformation can be calculated between those points.
  The transformation parameters can then directly be used for aligning
  the model. In this case, the reference point of the metrology model
  does not have to be changed.

  |  |  |
  | --- | --- |
  | ![figure](../assets/f3429aac80b61361.svg) | ![figure](../assets/bdccf3345fb40fd2.svg) |
  | ( 1) | ( 2) |

  (1) The contours of the metrology object and the four corresponding
  points in the image that was used for the creation of the metrology model.
  (2) The contours of the metrology object and the four corresponding
  points in a new image.

  1. Determine the point correspondences
  2. Estimate the model pose

     The following operator sequence calculates the parameters of the model
     pose
     (*`Row`*, *`Column`*, *`Angle`*)
     from corresponding points in the model image and one other image.

     *Example:*

     [`vector_to_rigid(PRowModel, PColumnModel, PRowCurrent,
     PColumnCurrent, HomMat2D)`](vector_to_rigid.md)

     [`hom_mat2d_to_affine_par(HomMat2D, Sx, Sy, Angle, Theta,
     Row, Column)`](hom_mat2d_to_affine_par.md)

     `align_metrology_model(MetrologyHandle, Row, Column, Angle)`

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- MetrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`MetrologyHandle`** (input_control, state is modified)  metrology_model `→`  (handle)

Handle of the metrology model.

**`Row`** (input_control)  real `→`  (real / integer)

Row coordinate of the alignment.

Default:
0

**`Column`** (input_control)  real `→`  (real / integer)

Column coordinate of the alignment.

Default:
0

**`Angle`** (input_control)  angle.rad `→`  (real / integer)

Rotation angle of the alignment.

Default:
0

## Example (HDevelop)

```
read_image (Image, 'metal-parts/circle_plate_01')
create_metrology_model (MetrologyHandle)
get_image_size (Image, Width, Height)
set_metrology_model_image_size (MetrologyHandle, Width, Height)
CircleParam := [354,274,53]
CircleParam := [CircleParam,350,519,53]
add_metrology_object_generic (MetrologyHandle, 'circle', CircleParam, 20,\
                              5, 1, 30, [], [], CircleIndices)
create_generic_shape_model (ModelID)
set_generic_shape_model_param (ModelID, 'metric', 'use_polarity')
set_generic_shape_model_param (ModelID, 'min_contrast', 20)
train_generic_shape_model (Image, ModelID)
* Determine location of shape model origin
area_center (Image, Area, RowOrigin, ColOrigin)
set_metrology_model_param (MetrologyHandle, 'reference_system', \
                           [RowOrigin,ColOrigin,0])
read_image (CurrentImage, 'metal-parts/circle_plate_02')
find_generic_shape_model (CurrentImage, ModelID, MatchResultID, \
                          NumMatchResult)
get_generic_shape_model_result (MatchResultID, 'all', 'row', Row)
get_generic_shape_model_result (MatchResultID, 'all', 'column', Col)
get_generic_shape_model_result (MatchResultID, 'all', 'angle', Angle)
align_metrology_model (MetrologyHandle, Row, Col, Angle)
apply_metrology_model (CurrentImage, MetrologyHandle)
get_metrology_object_result (MetrologyHandle, CircleIndices, 'all', \
                             'result_type', 'all_param', Rectangle)
get_metrology_object_result_contour (Contour, MetrologyHandle, \
                                     CircleIndices, 'all', 1.5)
```

## Result

If the parameters are valid, the operator
`align_metrology_model` returns the value 2 (
H_MSG_TRUE)
.
If necessary, an exception is raised.

## Possible Predecessors

`set_metrology_model_param`,
`add_metrology_object_generic`

## Possible Successors

`apply_metrology_model`

## See also

`get_metrology_object_model_contour`

## Module

2D Metrology
