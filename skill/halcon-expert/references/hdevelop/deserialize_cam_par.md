# deserialize_cam_par (Operator)

## Name

`deserialize_cam_par` — Deserialize the serialized internal camera parameters.

## Signature

`deserialize_cam_par( : : SerializedItemHandle : CameraParam)`

## Description

`deserialize_cam_par` deserializes the internal camera parameters,
that were serialized by [`serialize_cam_par`](serialize_cam_par.md)
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an
introduction of the basic principle of serialization). The
serialized camera parameters are defined by the handle
*`SerializedItemHandle`*.
The deserialized values are stored in an automatically created
tuple with the handle *`CameraParam`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`SerializedItemHandle`** (input_control)  serialized_item `→`  (handle)

Handle of the serialized item.

**`CameraParam`** (output_control)  campar `→`  (real / integer / string)

Internal camera parameters.

## Result

If the parameters are valid, the operator
`deserialize_cam_par` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_cam_par`

## Module

Foundation
