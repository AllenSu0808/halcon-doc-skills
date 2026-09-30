# serialize_camera_setup_model (Operator)

## Name

`serialize_camera_setup_model` — Serialize a camera setup model.

## Signature

`def serialize_camera_setup_model(camera_setup_model_id: HHandle) -> HHandle`

## Description

`serialize_camera_setup_model` serializes the data of a camera
setup model (see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of
the basic principle of serialization). The same data that is written
in a file by [`write_camera_setup_model`](write_camera_setup_model.md) is converted to a serialized
item. The camera setup model is defined by the handle
*`camera_setup_model_id`*. The serialized camera setup model is
returned by the handle *`serialized_item_handle`* and can be
deserialized by [`deserialize_camera_setup_model`](deserialize_camera_setup_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camera_setup_model_id`** (input_control)  camera_setup_model `→` HHandle

Handle to the camera setup model.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_camera_setup_model` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_camera_setup_model`

## Module

Calibration
