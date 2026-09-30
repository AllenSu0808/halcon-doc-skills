# WriteCameraSetupModel (Operator)

## Name

`WriteCameraSetupModel` — Store a camera setup model into a file.

## Signature

`static void HOperatorSet.WriteCameraSetupModel(HTuple cameraSetupModelID, HTuple fileName)`

`void HCameraSetupModel.WriteCameraSetupModel(string fileName)`

## Description

The operator `WriteCameraSetupModel` stores a camera setup model
*`cameraSetupModelID`* into a file specified by its file name
*`fileName`*.

The calibration data model can be later read with
[`ReadCameraSetupModel`](read_camera_setup_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraSetupModelID`** (input_control)  camera_setup_model `→` [HCameraSetupModel](HCameraSetupModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle to the camera setup model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

The file name of the model to be saved.

File extension:
.`csm`

## Module

Calibration
