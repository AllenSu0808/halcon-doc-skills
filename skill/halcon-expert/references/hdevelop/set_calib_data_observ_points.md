# set_calib_data_observ_points (Operator)

## Name

`set_calib_data_observ_points` — Set point-based observation data in a calibration data model.

## Signature

`set_calib_data_observ_points( : : CalibDataID, CameraIdx, CalibObjIdx, CalibObjPoseIdx, Row, Column, Index, Pose : )`

## Description

For a calibration model of type
`CalibSetup`=*'calibration_object'* (see
[`create_calib_data`](create_calib_data.md)), cameras are calibrated based on so-called
observations of calibration objects. With
`set_calib_data_observ_points`, you store such an observation in
the calibration data model *`CalibDataID`*. An observation consists of
the following data:

- ***`CameraIdx`*:** —

  index of the observing camera
- ***`CalibObjIdx`*:** —

  index of the observed calibration object
- ***`CalibObjPoseIdx`*:** —

  index of the observed pose of the
  calibration object. You can choose it freely, without following a strict
  order. If you specify an index that already exists for the calibration
  object *`CalibObjIdx`*, the corresponding observation data is
  replaced by the new one. Of course, the same index can be assigned to
  poses of different calibration objects.
- ***`Row`*, *`Column`*, *`Index`*:** —

  Extracted image
  coordinates and corresponding index of the calibration marks of the
  calibration object. *`Row`* and *`Column`* are tuples
  containing the same
  number of elements. *`Index`* can either contain a tuple (of the
  same length) or the value *'all'*, indicating that the points
  `[Row, Column]` correspond in a one-to-one relation to the
  calibration marks of the calibration object. If the number of row or
  column coordinates does not match the number of calibration marks, a
  corresponding error message is returned.
- ***`Pose`*:** —

  A roughly estimated pose of the observed calibration
  object relative to observing camera.

If you are using the HALCON calibration plate, it is recommended to use
[`find_calib_object`](find_calib_object.md) instead of `set_calib_data_observ_points`,
since the contour information, which it stores in the calibration data
model, enables a more precise calibration procedure with
[`calibrate_cameras`](calibrate_cameras.md).

The observation data can be accessed later by calling
[`get_calib_data_observ_points`](get_calib_data_observ_points.md) using the same values for the
arguments *`CameraIdx`*, *`CalibObjIdx`*, and
*`CalibObjPoseIdx`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- CalibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`CalibDataID`** (input_control, state is modified)  calib_data `→`  (handle)

Handle of a calibration data model.

**`CameraIdx`** (input_control)  number `→`  (integer)

Index of the observing camera.

Default:
0

Suggested values:
0, 1, 2

**`CalibObjIdx`** (input_control)  number `→`  (integer)

Index of the calibration object.

Default:
0

Suggested values:
0, 1, 2

**`CalibObjPoseIdx`** (input_control)  number `→`  (integer)

Index of the observed calibration object.

Default:
0

Suggested values:
0, 1, 2

Restriction:
`CalibObjPoseIdx >= 0`

**`Row`** (input_control)  number-array `→`  (real / integer)

Row coordinates of the extracted points.

**`Column`** (input_control)  number-array `→`  (real / integer)

Column coordinates of the extracted points.

**`Index`** (input_control)  number-array `→`  (integer / string)

Correspondence of the extracted points to the
calibration marks of the observed calibration object.

Default:
'all'

Suggested values:
'all', 0, 1, 2

**`Pose`** (input_control)  number-array `→`  (real / integer)

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
