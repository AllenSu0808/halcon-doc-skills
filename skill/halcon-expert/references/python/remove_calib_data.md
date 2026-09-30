# remove_calib_data (Operator)

## Name

`remove_calib_data` — Remove a data set from a calibration data model.

## Signature

`def remove_calib_data(calib_data_id: HHandle, item_type: str, item_idx: MaybeSequence[Union[int, str]]) -> None`

## Description

The operator `remove_calib_data`, removes data from the
calibration data model *`calib_data_id`*. Currently, only the hand-eye
calibration data set can be altered.
With *`item_type`*=*"tool"*, you can remove the pose of the robot
tool (in robot base coordinates), which was used to obtain the observation
of the pose of the calibration object with the same index *`item_idx`*
(corresponds to the parameter `CalibObjPoseIdx` of any of the
operators [`find_calib_object`](find_calib_object.md), [`set_calib_data_observ_pose`](set_calib_data_observ_pose.md),
or [`set_calib_data_observ_pose`](set_calib_data_observ_pose.md)). Note, that the corresponding
observation of the calibration object with the same index *`item_idx`*
that was previously set in the model also has to be removed. Otherwise,
the operator [`calibrate_hand_eye`](calibrate_hand_eye.md) will report an error.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- calib_data_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calib_data_id`** (input_control, state is modified)  calib_data `→` HHandle

Handle of a calibration data model.

**`item_type`** (input_control)  string `→` str

Type of the calibration data item.

Default:
"tool"

List of values:
"tool"

**`item_idx`** (input_control)  number(-array) `→` MaybeSequence[Union[int, str]]

Index of the affected item.

Default:
0

Suggested values:
0, 1, 2

## Possible Predecessors

`set_calib_data`,
`remove_calib_data_observ`

## Possible Successors

`calibrate_hand_eye`

## See also

`calibrate_cameras`

## Module

Calibration
