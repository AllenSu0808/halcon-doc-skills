# read_camera_setup_model (Operator)

## Name

`read_camera_setup_model` — Restore a camera setup model from a file.

## Signature

`read_camera_setup_model( : : FileName : CameraSetupModelID)`

## Description

The operator `read_camera_setup_model` restores a camera setup
model from a file specified by its *`FileName`* and returns a handle
to the restored model in *`CameraSetupModelID`*. The model file must
have been created by [`write_camera_setup_model`](write_camera_setup_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`FileName`** (input_control)  filename.read `→`  (string)

The path and file name of the model file.

File extension:
.`csm`

**`CameraSetupModelID`** (output_control)  camera_setup_model `→`  (handle)

Handle to the camera setup model.

## Module

Calibration
