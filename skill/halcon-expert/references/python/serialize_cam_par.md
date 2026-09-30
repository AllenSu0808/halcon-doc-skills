# serialize_cam_par (Operator)

## Name

`serialize_cam_par` — Serialize the internal camera parameters.

## Signature

`def serialize_cam_par(camera_param: Sequence[Union[int, float, str]]) -> HHandle`

## Description

`serialize_cam_par` serializes the internal camera parameters
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The same data that is written in a
file by [`write_cam_par`](write_cam_par.md) is converted to a serialized item.
The camera parameters are defined by the tuple *`camera_param`*.
The serialized camera parameters are returned by the handle
*`serialized_item_handle`* and can be deserialized by
[`deserialize_cam_par`](deserialize_cam_par.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`camera_param`** (input_control)  campar `→` Sequence[Union[int, float, str]]

Internal camera parameters.

**`serialized_item_handle`** (output_control)  serialized_item `→` HHandle

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
