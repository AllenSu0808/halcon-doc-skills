# deserialize_camera_setup_model (Operator)

## Name

`deserialize_camera_setup_model` — Deserialize a serialized camera setup model.

## Signature

`def deserialize_camera_setup_model(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_camera_setup_model` deserializes a camera setup
model, that was serialized by [`serialize_camera_setup_model`](serialize_camera_setup_model.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized camera setup model
is defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
camera setup model with the handle *`camera_setup_model_id`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`camera_setup_model_id`** (output_control)  camera_setup_model `→` HHandle

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
