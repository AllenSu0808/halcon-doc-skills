# RemoveCalibData (Operator)

## Name

`RemoveCalibData` — Remove a data set from a calibration data model.

## Signature

`static void HOperatorSet.RemoveCalibData(HTuple calibDataID, HTuple itemType, HTuple itemIdx)`

`void HCalibData.RemoveCalibData(string itemType, HTuple itemIdx)`

`void HCalibData.RemoveCalibData(string itemType, int itemIdx)`

## Description

The operator `RemoveCalibData`, removes data from the
calibration data model *`calibDataID`*. Currently, only the hand-eye
calibration data set can be altered.
With *`itemType`*=*"tool"*, you can remove the pose of the robot
tool (in robot base coordinates), which was used to obtain the observation
of the pose of the calibration object with the same index *`itemIdx`*
(corresponds to the parameter `CalibObjPoseIdx` of any of the
operators [`FindCalibObject`](find_calib_object.md), [`SetCalibDataObservPose`](set_calib_data_observ_pose.md),
or [`SetCalibDataObservPose`](set_calib_data_observ_pose.md)). Note, that the corresponding
observation of the calibration object with the same index *`itemIdx`*
that was previously set in the model also has to be removed. Otherwise,
the operator [`CalibrateHandEye`](calibrate_hand_eye.md) will report an error.

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

**`itemType`** (input_control)  string `→` [HTuple](HTuple.md) (*string*)

Type of the calibration data item.

Default:
"tool"

List of values:
"tool"

**`itemIdx`** (input_control)  number(-array) `→` [HTuple](HTuple.md) (*int* / long / string)

Index of the affected item.

Default:
0

Suggested values:
0, 1, 2

## Possible Predecessors

`SetCalibData`,
`RemoveCalibDataObserv`

## Possible Successors

`CalibrateHandEye`

## See also

`CalibrateCameras`

## Module

Calibration
