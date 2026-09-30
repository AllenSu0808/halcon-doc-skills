# set_calib_data_observ_points (Operator)

## Name

`set_calib_data_observ_points` — Set point-based observation data in a calibration data model.

## Signature

`def set_calib_data_observ_points(calib_data_id: HHandle, camera_idx: int, calib_obj_idx: int, calib_obj_pose_idx: int, row: Sequence[Union[float, int]], column: Sequence[Union[float, int]], index: Sequence[Union[int, str]], pose: Sequence[Union[float, int]]) -> None`

## Description

For a calibration model of type
`calib_setup`=*"calibration_object"* (see
[`create_calib_data`](create_calib_data.md)), cameras are calibrated based on so-called
observations of calibration objects. With
`set_calib_data_observ_points`, you store such an observation in
the calibration data model *`calib_data_id`*. An observation consists of
the following data:

- ***`camera_idx`*:** —

  index of the observing camera
- ***`calib_obj_idx`*:** —

  index of the observed calibration object
- ***`calib_obj_pose_idx`*:** —

  index of the observed pose of the
  calibration object. You can choose it freely, without following a strict
  order. If you specify an index that already exists for the calibration
  object *`calib_obj_idx`*, the corresponding observation data is
  replaced by the new one. Of course, the same index can be assigned to
  poses of different calibration objects.
- ***`row`*, *`column`*, *`index`*:** —

  Extracted image
  coordinates and corresponding index of the calibration marks of the
  calibration object. *`row`* and *`column`* are tuples
  containing the same
  number of elements. *`index`* can either contain a tuple (of the
  same length) or the value *"all"*, indicating that the points
  `[Row, Column]` correspond in a one-to-one relation to the
  calibration marks of the calibration object. If the number of row or
  column coordinates does not match the number of calibration marks, a
  corresponding error message is returned.
- ***`pose`*:** —

  A roughly estimated pose of the observed calibration
  object relative to observing camera.

If you are using the HALCON calibration plate, it is recommended to use
[`find_calib_object`](find_calib_object.md) instead of `set_calib_data_observ_points`,
since the contour information, which it stores in the calibration data
model, enables a more precise calibration procedure with
[`calibrate_cameras`](calibrate_cameras.md).

The observation data can be accessed later by calling
[`get_calib_data_observ_points`](get_calib_data_observ_points.md) using the same values for the
arguments *`camera_idx`*, *`calib_obj_idx`*, and
*`calib_obj_pose_idx`*.

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

Suggested values:
0, 1, 2

**`calib_obj_idx`** (input_control)  number `→` int

Index of the calibration object.

Default:
0

Suggested values:
0, 1, 2

**`calib_obj_pose_idx`** (input_control)  number `→` int

Index of the observed calibration object.

Default:
0

Suggested values:
0, 1, 2

Restriction:
`CalibObjPoseIdx >= 0`

**`row`** (input_control)  number-array `→` Sequence[Union[float, int]]

Row coordinates of the extracted points.

**`column`** (input_control)  number-array `→` Sequence[Union[float, int]]

Column coordinates of the extracted points.

**`index`** (input_control)  number-array `→` Sequence[Union[int, str]]

Correspondence of the extracted points to the
calibration marks of the observed calibration object.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`pose`** (input_control)  number-array `→` Sequence[Union[float, int]]

Roughly estimated pose of the observed calibration
object relative to the observing camera.

Number of elements:
7

## Possible Predecessors

`find_marks_and_pose`,
`set_calib_data_cam_param`,
`set_calib_data_calib_object`

## Possible Successors

`set_calib_data`,
`calibrate_cameras`

## Alternatives

`find_calib_object`

## Module

Calibration
