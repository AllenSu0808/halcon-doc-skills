# DeserializeCamPar (Operator)

## Name

`DeserializeCamPar` — Deserialize the serialized internal camera parameters.

## Signature

`static void HOperatorSet.DeserializeCamPar(HTuple serializedItemHandle, out HTuple cameraParam)`

`void HCamPar.DeserializeCamPar(HSerializedItem serializedItemHandle)`

## Description

`DeserializeCamPar` deserializes the internal camera parameters,
that were serialized by [`SerializeCamPar`](serialize_cam_par.md)
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized camera parameters are defined by the handle
*`serializedItemHandle`*.
The deserialized values are stored in an automatically created
tuple with the handle *`cameraParam`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`cameraParam`** (output_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

## Result

If the parameters are valid, the operator
`DeserializeCamPar` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeCamPar`

## Module

Foundation
