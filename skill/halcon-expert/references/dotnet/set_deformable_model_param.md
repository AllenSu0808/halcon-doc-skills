# SetDeformableModelParam (Operator)

## Name

`SetDeformableModelParam` — Set selected parameters of the deformable model.

## Signature

`static void HOperatorSet.SetDeformableModelParam(HTuple modelID, HTuple genParamName, HTuple genParamValue)`

`void HDeformableModel.SetDeformableModelParam(HTuple genParamName, HTuple genParamValue)`

## Description

The operator `SetDeformableModelParam` sets the selected parameters
*`genParamName`* in the deformable model *`modelID`*. The
following parameters can be modified:

*"min_contrast"*

Sets the minimum contrast of the object in the search images for the
deformable model *`modelID`*.
Thereby, the value of *"min_contrast"* that was originally set, e.g.,
with [`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md), is overwritten
for the deformable model *`modelID`*. Note that if the
deformable model *`modelID`* was read from
file and if this file should be changed as well, the deformable model
*`modelID`* must again be written to file after the execution of the
operator `SetDeformableModelParam`.

*"get_deformable_model_contours_coord_system"*

Sets the coordinate system in which the contours are returned when
calling the operator [`GetDeformableModelContours`](get_deformable_model_contours.md).
If *"world"* is passed, the contours
are returned in the world coordinate system in metric units. Note that
this is only possible for the calibrated case. If *"image"*
is passed, the contours are returned in the image coordinate system
in pixel units. In the calibrated case this system corresponds to the
rectified image coordinate system. The
rectified image coordinate system is the coordinate system of an image
one would obtain by [`ChangeRadialDistortionImage`](change_radial_distortion_image.md) when
using the rectified camera parameters. The rectified camera parameters
can be queried by [`GetDeformableModelParams`](get_deformable_model_params.md). If the model
was created by [`CreatePlanarCalibDeformableModelXld`](create_planar_calib_deformable_model_xld.md)
the value of *"get_deformable_model_contours_coord_system"*
is *"world"* by default. In all other cases it is
*"image"* by default.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`genParamName`** (input_control)  attribute.name-array `→` [HTuple](HTuple.md) (*string*)

Parameter names.

List of values:
"get_deformable_model_contours_coord_system", "min_contrast"

**`genParamValue`** (input_control)  attribute.value-array `→` [HTuple](HTuple.md) (*double* / int / long / string)

Parameter values.

Suggested values:
5, 6, 7, 8, 9, 10, "image", "world"

## Result

If the parameters are valid, the operator `SetDeformableModelParam`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Predecessors

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`,
`CreateLocalDeformableModel`,
`ReadDeformableModel`

## Possible Successors

`FindPlanarUncalibDeformableModel`,
`FindPlanarCalibDeformableModel`

## See also

`GetDeformableModelContours`,
`GetDeformableModelParams`

## Module

Matching
