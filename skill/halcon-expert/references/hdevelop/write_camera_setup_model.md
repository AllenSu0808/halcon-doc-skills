# write_camera_setup_model (Operator)

## Name

`write_camera_setup_model` — Store a camera setup model into a file.

## Signature

`write_camera_setup_model( : : CameraSetupModelID, FileName : )`

## Description

The operator `write_camera_setup_model` stores a camera setup model
*`CameraSetupModelID`* into a file specified by its file name
*`FileName`*.

The calibration data model can be later read with
[`read_camera_setup_model`](read_camera_setup_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CameraSetupModelID`** (input_control)  camera_setup_model `→`  (handle)

Handle to the camera setup model.

**`FileName`** (input_control)  filename.write `→`  (string)

The file name of the model to be saved.

File extension:
.`csm`

## Module

Calibration
