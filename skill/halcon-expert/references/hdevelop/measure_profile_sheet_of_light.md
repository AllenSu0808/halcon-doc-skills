# measure_profile_sheet_of_light (Operator)

## Name

`measure_profile_sheet_of_light` — Process the profile image provided as input and store the resulting
disparity to the sheet-of-light model.

## Signature

`measure_profile_sheet_of_light(ProfileImage : : SheetOfLightModelID, MovementPose : )`

## Description

The operator `measure_profile_sheet_of_light` processes the
*`ProfileImage`* and stores the resulting disparity values to the
sheet-of-light model. Please note that *`ProfileImage`* will only
be processed in the region defined by `ProfileRegion` as set with
the operator [`create_sheet_of_light_model`](create_sheet_of_light_model.md).
Since *`ProfileImage`*
is processed column by column, the profile must be oriented roughly
horizontal.

**Influence of different model parameters**

If the model parameter *'score_type'* has been set to
*'intensity'* or *'width'*, score values are also computed
and stored into the model. Refer to [`set_sheet_of_light_param`](set_sheet_of_light_param.md)
for details on the possible values of *'score_type'*.

If the model parameter *'calibration'* has been set to
*'xz'*, *'xyz'*, or *'offset_scale'* and all parameters
required to determine the calibration transformation have been set to the
sheet-of-light model, the calibration transformations will be automatically
applied to the disparity values after the measurement. Refer to
[`set_sheet_of_light_param`](set_sheet_of_light_param.md) for details on setting the calibration
parameters to the sheet-of-light model.

**Setting MovementPose**

*`MovementPose`* describes the movement of the object between the
acquisition of the previous profile and the acquisition of the current
profile.

If the model parameter *'calibration'* has been set to
*'none'* or *'xz'* (see [`set_sheet_of_light_param`](set_sheet_of_light_param.md))
the movement of the object is not taken into consideration by the
calibration transformation. Therefore, *`MovementPose`* is ignored,
and it can be set to an empty tuple.

If the model parameter *'calibration'* has been set to
*'xyz'*, the pose describing the movement of the object must be
specified to the sheet-of-light model. This can be done here with
*`MovementPose`* or with the parameter *'movement_pose'* in
the operator [`set_sheet_of_light_param`](set_sheet_of_light_param.md).

If the model parameter *'calibration'* has been set to
*'offset_scale'*, a movement can be specified, but it should be
considered, that the space to which this transformation is applied
is most probably not metrically.

If the movement of the object between the recording of two successive
profiles is constant, we recommend to set *`MovementPose`* here to
an empty tuple, and to set the constant pose via the parameter
*'movement_pose'* in the operator [`set_sheet_of_light_param`](set_sheet_of_light_param.md).
This configuration is often encountered, for example when the object
under measurement is moved by a conveyor belt and measured by a fixed
measurement system.

If the movement of the object between the recording of two successive
profiles is not constant, for example because the measurement system is
moved over the object by a robot, you must set *`MovementPose`* here
for each call of `measure_profile_sheet_of_light`.

*`MovementPose`* must be expressed in the world coordinate system
that is implicitly defined during the calibration of the measurement
system.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SheetOfLightModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`ProfileImage`** (input_object)  singlechannelimage `→` object (byte / uint2)

Input image.

**`SheetOfLightModelID`** (input_control, state is modified)  sheet_of_light_model `→`  (handle)

Handle of the sheet-of-light model.

**`MovementPose`** (input_control)  number-array `→`  (integer / real)

Pose describing the movement of the scene under
measurement between the previously processed profile
image and the current profile image.

## Result

The operator `measure_profile_sheet_of_light` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Successors

`apply_sheet_of_light_calibration`,
`get_sheet_of_light_result`

## See also

`query_sheet_of_light_params`,
`get_sheet_of_light_param`,
`get_sheet_of_light_result`,
`apply_sheet_of_light_calibration`

## Module

3D Metrology
