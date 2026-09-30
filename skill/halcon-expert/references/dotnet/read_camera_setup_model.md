# ReadCameraSetupModel (Operator)

## Name

`ReadCameraSetupModel` — Restore a camera setup model from a file.

## Signature

`static void HOperatorSet.ReadCameraSetupModel(HTuple fileName, out HTuple cameraSetupModelID)`

`public HCameraSetupModel(string fileName)`

`void HCameraSetupModel.ReadCameraSetupModel(string fileName)`

## Description

The operator `ReadCameraSetupModel` restores a camera setup
model from a file specified by its *`fileName`* and returns a handle
to the restored model in *`cameraSetupModelID`*. The model file must
have been created by [`WriteCameraSetupModel`](write_camera_setup_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

The path and file name of the model file.

File extension:
.`csm`

**`cameraSetupModelID`** (output_control)  camera_setup_model `→` [HCameraSetupModel](HCameraSetupModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle to the camera setup model.

## Module

Calibration
