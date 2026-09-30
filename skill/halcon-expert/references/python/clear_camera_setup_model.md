# clear_camera_setup_model (Operator)

## Name

`clear_camera_setup_model` — Free the memory of a calibration setup model.

## Signature

`def clear_camera_setup_model(camera_setup_model_id: HHandle) -> None`

## Description

The operator `clear_camera_setup_model` frees the memory of a
camera setup model that was created by [`create_camera_setup_model`](create_camera_setup_model.md) or
[`read_camera_setup_model`](read_camera_setup_model.md) or was returned as a result
by [`get_calib_data`](get_calib_data.md). After calling `clear_camera_setup_model`,
the model can no longer be used. The handle *`camera_setup_model_id`*
becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- camera_setup_model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`camera_setup_model_id`** (input_control, state is modified)  camera_setup_model `→` HHandle

Handle of the camera setup model.

## Module

Calibration
