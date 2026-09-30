# deserialize_camera_setup_model (Operator)

## Name

`deserialize_camera_setup_model` — Deserialize a serialized camera setup model.

## Signature

`deserialize_camera_setup_model( : : SerializedItemHandle : CameraSetupModelID)`

## Description

`deserialize_camera_setup_model` deserializes a camera setup
model, that was serialized by [`serialize_camera_setup_model`](serialize_camera_setup_model.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized camera setup model
is defined by the handle *`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
camera setup model with the handle *`CameraSetupModelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`CameraSetupModelID`** (output_control)  camera_setup_model `→`  (handle)

Handle to the camera setup model.

## Result

If the parameters are valid, the operator
`deserialize_camera_setup_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_camera_setup_model`

## Module

Calibration
