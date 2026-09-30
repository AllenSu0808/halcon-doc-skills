# GetCalibDataObservPose (Operator)

## Name

`GetCalibDataObservPose` — Get observed calibration object poses from a calibration data model.

## Signature

`static void HOperatorSet.GetCalibDataObservPose(HTuple calibDataID, HTuple cameraIdx, HTuple calibObjIdx, HTuple calibObjPoseIdx, out HTuple objInCameraPose)`

`HPose HCalibData.GetCalibDataObservPose(int cameraIdx, int calibObjIdx, int calibObjPoseIdx)`

## Description

The operator `GetCalibDataObservPose` reads the poses
of the calibration object given in the camera coordinate system
from a calibration data model *`calibDataID`*. The
observation data was previously stored by
[`SetCalibDataObservPose`](set_calib_data_observ_pose.md), [`FindCalibObject`](find_calib_object.md), or
[`SetCalibDataObservPoints`](set_calib_data_observ_points.md).

Note that if the model *`calibDataID`* uses a general sensor and
no calibration object (i.e., the model was created by
[`CreateCalibData`](create_calib_data.md) with `numCameras`=0 and
`numCalibObjects`=0), then both *`cameraIdx`* and
*`calibObjIdx`* must be set to 0.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`calibDataID`** (input_control)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

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

**`objInCameraPose`** (output_control)  pose `→` [HPose](HPose.md), [HTuple](HTuple.md) (*double* / int / long)

Stored observed calibration
object pose relative to the observing camera.

Number of elements:
7

## Module

Calibration
