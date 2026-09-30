# SetCalibDataObservPoints (Operator)

## Name

`SetCalibDataObservPoints` — Set point-based observation data in a calibration data model.

## Signature

`static void HOperatorSet.SetCalibDataObservPoints(HTuple calibDataID, HTuple cameraIdx, HTuple calibObjIdx, HTuple calibObjPoseIdx, HTuple row, HTuple column, HTuple index, HTuple pose)`

`void HCalibData.SetCalibDataObservPoints(int cameraIdx, int calibObjIdx, int calibObjPoseIdx, HTuple row, HTuple column, HTuple index, HTuple pose)`

## Description

For a calibration model of type
`calibSetup`=*"calibration_object"* (see
[`CreateCalibData`](create_calib_data.md)), cameras are calibrated based on so-called
observations of calibration objects. With
`SetCalibDataObservPoints`, you store such an observation in
the calibration data model *`calibDataID`*. An observation consists of
the following data:

- ***`cameraIdx`*:** —

  index of the observing camera
- ***`calibObjIdx`*:** —

  index of the observed calibration object
- ***`calibObjPoseIdx`*:** —

  index of the observed pose of the
  calibration object. You can choose it freely, without following a strict
  order. If you specify an index that already exists for the calibration
  object *`calibObjIdx`*, the corresponding observation data is
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
[`FindCalibObject`](find_calib_object.md) instead of `SetCalibDataObservPoints`,
since the contour information, which it stores in the calibration data
model, enables a more precise calibration procedure with
[`CalibrateCameras`](calibrate_cameras.md).

The observation data can be accessed later by calling
[`GetCalibDataObservPoints`](get_calib_data_observ_points.md) using the same values for the
arguments *`cameraIdx`*, *`calibObjIdx`*, and
*`calibObjPoseIdx`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- calibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calibDataID`** (input_control, state is modified)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

**`cameraIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observing camera.

Default:
0

Suggested values:
0, 1, 2

**`calibObjIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the calibration object.

Default:
0

Suggested values:
0, 1, 2

**`calibObjPoseIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observed calibration object.

Default:
0

Suggested values:
0, 1, 2

Restriction:
`CalibObjPoseIdx >= 0`

**`row`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Row coordinates of the extracted points.

**`column`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Column coordinates of the extracted points.

**`index`** (input_control)  number-array `→` [HTuple](HTuple.md) (*int* / long / string)

Correspondence of the extracted points to the
calibration marks of the observed calibration object.

Default:
"all"

Suggested values:
"all", 0, 1, 2

**`pose`** (input_control)  number-array `→` [HTuple](HTuple.md) (*double* / int / long)

Roughly estimated pose of the observed calibration
object relative to the observing camera.

Number of elements:
7

## Possible Predecessors

`FindMarksAndPose`,
`SetCalibDataCamParam`,
`SetCalibDataCalibObject`

## Possible Successors

`SetCalibData`,
`CalibrateCameras`

## Alternatives

`FindCalibObject`

## Module

Calibration
