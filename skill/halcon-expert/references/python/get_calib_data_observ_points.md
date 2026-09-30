# get_calib_data_observ_points (Operator)

## Name

`get_calib_data_observ_points` — Get point-based observation data from a calibration data model.

## Signature

`def get_calib_data_observ_points(calib_data_id: HHandle, camera_idx: int, calib_obj_idx: int, calib_obj_pose_idx: int) -> Tuple[Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[Union[float, int]], Sequence[Union[float, int]]]`

## Description

The operator `get_calib_data_observ_points` reads point-based
observation data from a calibration data model *`calib_data_id`*. This
operator reads back observation data stored by
[`set_calib_data_observ_points`](set_calib_data_observ_points.md) or [`find_calib_object`](find_calib_object.md). See
[`set_calib_data_observ_points`](set_calib_data_observ_points.md) for a detailed description of the
arguments.

Please note that if [`set_calib_data_observ_points`](set_calib_data_observ_points.md) is used for
the calibration, the returned values of *`row`* and
*`column`* are the original values that have been set with
[`set_calib_data_observ_points`](set_calib_data_observ_points.md). Similarly, if
[`find_calib_object`](find_calib_object.md) is used for the extraction, the values of
*`row`* and *`column`* returned by
`get_calib_data_observ_points` coincide with the coordinates
of the detected points computed by [`find_calib_object`](find_calib_object.md).

Note that `get_calib_data_observ_points` returns the pose of
an uncalibrated model. To get the pose of a calibrated model, use
[`get_calib_data`](get_calib_data.md).

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

**`row`** (output_control)  number-array `→` Sequence[Union[float, int]]

Row coordinates of the detected points.

**`column`** (output_control)  number-array `→` Sequence[Union[float, int]]

Column coordinates of the detected points.

**`index`** (output_control)  number-array `→` Sequence[Union[float, int]]

Correspondence of the detected points to the
points of the observed calibration object.

**`pose`** (output_control)  number-array `→` Sequence[Union[float, int]]

Roughly estimated pose of the observed calibration
object relative to the observing camera.

Number of elements:
7

## Module

Calibration
