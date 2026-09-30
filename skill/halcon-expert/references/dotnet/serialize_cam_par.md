# SerializeCamPar (Operator)

## Name

`SerializeCamPar` — Serialize the internal camera parameters.

## Signature

`static void HOperatorSet.SerializeCamPar(HTuple cameraParam, out HTuple serializedItemHandle)`

`HSerializedItem HCamPar.SerializeCamPar()`

## Description

`SerializeCamPar` serializes the internal camera parameters
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`WriteCamPar`](write_cam_par.md) is converted to a serialized item.
The camera parameters are defined by the tuple *`cameraParam`*.
The serialized camera parameters are returned by the handle
*`serializedItemHandle`* and can be deserialized by
[`DeserializeCamPar`](deserialize_cam_par.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`cameraParam`** (input_control)  campar `→` [HCamPar](HCamPar.md), [HTuple](HTuple.md) (*double* / int / long / string)

Internal camera parameters.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeCamPar` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeCamPar`

## Module

Foundation
