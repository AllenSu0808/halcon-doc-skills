# SerializeCameraSetupModel (Operator)

## Name

`SerializeCameraSetupModel` — Serialize a camera setup model.

## Signature

`static void HOperatorSet.SerializeCameraSetupModel(HTuple cameraSetupModelID, out HTuple serializedItemHandle)`

`HSerializedItem HCameraSetupModel.SerializeCameraSetupModel()`

## Description

`SerializeCameraSetupModel` serializes the data of a camera
setup model (see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of
the basic principle of serialization). The same data that is written
in a file by [`WriteCameraSetupModel`](write_camera_setup_model.md) is converted to a serialized
item. The camera setup model is defined by the handle
*`cameraSetupModelID`*. The serialized camera setup model is
returned by the handle *`serializedItemHandle`* and can be
deserialized by [`DeserializeCameraSetupModel`](deserialize_camera_setup_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraSetupModelID`** (input_control)  camera_setup_model `→` [HCameraSetupModel](HCameraSetupModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle to the camera setup model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeCameraSetupModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeCameraSetupModel`

## Module

Calibration
