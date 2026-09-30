# RemoveCalibDataObserv (Operator)

## Name

`RemoveCalibDataObserv` — Remove observation data from a calibration data model.

## Signature

`static void HOperatorSet.RemoveCalibDataObserv(HTuple calibDataID, HTuple cameraIdx, HTuple calibObjIdx, HTuple calibObjPoseIdx)`

`void HCalibData.RemoveCalibDataObserv(int cameraIdx, int calibObjIdx, int calibObjPoseIdx)`

## Description

The operator `RemoveCalibDataObserv` removes observations that were
set in a calibration data model *`calibDataID`* using
[`FindCalibObject`](find_calib_object.md), [`SetCalibDataObservPoints`](set_calib_data_observ_points.md), or
[`SetCalibDataObservPose`](set_calib_data_observ_pose.md). The parameters *`cameraIdx`*,
*`calibObjIdx`*, and *`calibObjPoseIdx`* should specify a valid
observation from the calibration model.
Note that if the calibration data model *`calibDataID`* is used
in [`CalibrateHandEye`](calibrate_hand_eye.md), the corresponding tool pose also has to
be deleted using [`RemoveCalibData`](remove_calib_data.md).

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

**`calibObjIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observed calibration object.

Default:
0

**`calibObjPoseIdx`** (input_control)  number `→` [HTuple](HTuple.md) (*int* / long)

Index of the observed calibration object pose.

Default:
0

## Possible Predecessors

`FindCalibObject`,
`SetCalibDataObservPoints`,
`SetCalibDataObservPose`

## Possible Successors

`RemoveCalibData`,
`CalibrateCameras`,
`CalibrateHandEye`

## Module

Calibration
