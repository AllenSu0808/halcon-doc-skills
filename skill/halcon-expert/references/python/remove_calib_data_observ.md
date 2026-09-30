# remove_calib_data_observ (Operator)

## Name

`remove_calib_data_observ` — Remove observation data from a calibration data model.

## Signature

`def remove_calib_data_observ(calib_data_id: HHandle, camera_idx: int, calib_obj_idx: int, calib_obj_pose_idx: int) -> None`

## Description

The operator `remove_calib_data_observ` removes observations that were
set in a calibration data model *`calib_data_id`* using
[`find_calib_object`](find_calib_object.md), [`set_calib_data_observ_points`](set_calib_data_observ_points.md), or
[`set_calib_data_observ_pose`](set_calib_data_observ_pose.md). The parameters *`camera_idx`*,
*`calib_obj_idx`*, and *`calib_obj_pose_idx`* should specify a valid
observation from the calibration model.
Note that if the calibration data model *`calib_data_id`* is used
in [`calibrate_hand_eye`](calibrate_hand_eye.md), the corresponding tool pose also has to
be deleted using [`remove_calib_data`](remove_calib_data.md).

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

**`camera_idx`** (input_control)  number `→` int

Index of the observing camera.

Default:
0

**`calib_obj_idx`** (input_control)  number `→` int

Index of the observed calibration object.

Default:
0

**`calib_obj_pose_idx`** (input_control)  number `→` int

Index of the observed calibration object pose.

Default:
0

## Possible Predecessors

`find_calib_object`,
`set_calib_data_observ_points`,
`set_calib_data_observ_pose`

## Possible Successors

`remove_calib_data`,
`calibrate_cameras`,
`calibrate_hand_eye`

## Module

Calibration
