# serialize_cam_par (Operator)

## Name

`serialize_cam_par` — Serialize the internal camera parameters.

## Signature

`serialize_cam_par( : : CameraParam : SerializedItemHandle)`

## Description

`serialize_cam_par` serializes the internal camera parameters
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_cam_par`](write_cam_par.md) is converted to a serialized item.
The camera parameters are defined by the tuple *`CameraParam`*.
The serialized camera parameters are returned by the handle
*`SerializedItemHandle`* and can be deserialized by
[`deserialize_cam_par`](deserialize_cam_par.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`CameraParam`** (input_control)  campar `→`  (real / integer / string)

Internal camera parameters.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_cam_par` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_cam_par`

## Module

Foundation
