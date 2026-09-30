# set_profile_sheet_of_light (Operator)

## Name

`set_profile_sheet_of_light` — Set sheet of light profiles by measured disparities.

## Signature

`def set_profile_sheet_of_light(profile_disparity_image: HObject, sheet_of_light_model_id: HHandle, movement_poses: Sequence[Union[int, float]]) -> None`

## Description

`set_profile_sheet_of_light` adds sheet-of-light profiles to the
sheet-of-light model *`sheet_of_light_model_id`*. The profiles are specified
as rows in a disparity image in *`profile_disparity_image`*.
Each of the profiles can have an individual Pose set in
*`movement_poses`* which is interpreted as relative movement
to the previous row.
If no pose is set, the default transformation is
used, which can be set by [`set_sheet_of_light_param`](set_sheet_of_light_param.md). If only one pose
is set, this pose will become the default transformation.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- sheet_of_light_model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`profile_disparity_image`** (input_object)  singlechannelimage `→` HObject (byte / uint2 / real)

Disparity image that contains several profiles.

**`sheet_of_light_model_id`** (input_control, state is modified)  sheet_of_light_model `→` HHandle

Handle of the sheet-of-light model.

**`movement_poses`** (input_control)  number-array `→` Sequence[Union[int, float]]

Poses describing the movement of the scene under
measurement between the previously processed profile
image and the current profile image.

## Result

The operator `set_profile_sheet_of_light` returns the
value 2 (
H_MSG_TRUE)
if the given parameters are correct.
Otherwise, an exception will be raised.

## Possible Successors

`get_sheet_of_light_result`,
`get_sheet_of_light_result_object_model_3d`

## See also

`query_sheet_of_light_params`,
`get_sheet_of_light_param`,
`get_sheet_of_light_result`,
`apply_sheet_of_light_calibration`

## Module

3D Metrology
