# ClearCameraSetupModel (Operator)

## Name

`ClearCameraSetupModel` — Free the memory of a calibration setup model.

## Signature

`static void HOperatorSet.ClearCameraSetupModel(HTuple cameraSetupModelID)`

`void HCameraSetupModel.ClearCameraSetupModel()`

## Description

The operator `ClearCameraSetupModel` frees the memory of a
camera setup model that was created by [`CreateCameraSetupModel`](create_camera_setup_model.md) or
[`ReadCameraSetupModel`](read_camera_setup_model.md) or was returned as a result
by [`GetCalibData`](get_calib_data.md). After calling `ClearCameraSetupModel`,
the model can no longer be used. The handle *`cameraSetupModelID`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- cameraSetupModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`cameraSetupModelID`** (input_control, state is modified)  camera_setup_model `→` [HCameraSetupModel](HCameraSetupModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the camera setup model.

## Module

Calibration
