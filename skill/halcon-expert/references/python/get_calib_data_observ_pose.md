# get_calib_data_observ_pose (Operator)

## Name

`get_calib_data_observ_pose` — Get observed calibration object poses from a calibration data model.

## Signature

`def get_calib_data_observ_pose(calib_data_id: HHandle, camera_idx: int, calib_obj_idx: int, calib_obj_pose_idx: int) -> Sequence[Union[float, int]]`

## Description

The operator `get_calib_data_observ_pose` reads the poses
of the calibration object given in the camera coordinate system
from a calibration data model *`calib_data_id`*. The
observation data was previously stored by
[`set_calib_data_observ_pose`](set_calib_data_observ_pose.md), [`find_calib_object`](find_calib_object.md), or
[`set_calib_data_observ_points`](set_calib_data_observ_points.md).

Note that if the model *`calib_data_id`* uses a general sensor and
no calibration object (i.e., the model was created by
[`create_calib_data`](create_calib_data.md) with `num_cameras`=0 and
`num_calib_objects`=0), then both *`camera_idx`* and
*`calib_obj_idx`* must be set to 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`calib_data_id`** (input_control)  calib_data `→` HHandle

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

**`obj_in_camera_pose`** (output_control)  pose `→` Sequence[Union[float, int]]

Stored observed calibration
object pose relative to the observing camera.

Number of elements:
7

## Module

Calibration
