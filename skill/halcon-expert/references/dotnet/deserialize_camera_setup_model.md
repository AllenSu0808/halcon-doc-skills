# DeserializeCameraSetupModel (Operator)

## Name

`DeserializeCameraSetupModel` — Deserialize a serialized camera setup model.

## Signature

`static void HOperatorSet.DeserializeCameraSetupModel(HTuple serializedItemHandle, out HTuple cameraSetupModelID)`

`void HCameraSetupModel.DeserializeCameraSetupModel(HSerializedItem serializedItemHandle)`

## Description

`DeserializeCameraSetupModel` deserializes a camera setup
model, that was serialized by [`SerializeCameraSetupModel`](serialize_camera_setup_model.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized camera setup model
is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
camera setup model with the handle *`cameraSetupModelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`cameraSetupModelID`** (output_control)  camera_setup_model `→` [HCameraSetupModel](HCameraSetupModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle to the camera setup model.

## Result

If the parameters are valid, the operator
`DeserializeCameraSetupModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeCameraSetupModel`

## Module

Calibration
