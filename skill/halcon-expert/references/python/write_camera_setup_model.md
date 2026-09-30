# write_camera_setup_model (Operator)

## Name

`write_camera_setup_model` — Store a camera setup model into a file.

## Signature

`def write_camera_setup_model(camera_setup_model_id: HHandle, file_name: str) -> None`

## Description

The operator `write_camera_setup_model` stores a camera setup model
*`camera_setup_model_id`* into a file specified by its file name
*`file_name`*.

The calibration data model can be later read with
[`read_camera_setup_model`](read_camera_setup_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camera_setup_model_id`** (input_control)  camera_setup_model `→` HHandle

Handle to the camera setup model.

**`file_name`** (input_control)  filename.write `→` str

The file name of the model to be saved.

File extension:
.`csm`

## Module

Calibration
