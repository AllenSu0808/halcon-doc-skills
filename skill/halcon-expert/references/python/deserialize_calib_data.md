# deserialize_calib_data (Operator)

## Name

`deserialize_calib_data` — Deserialize a serialized calibration data model.

## Signature

`def deserialize_calib_data(serialized_item_handle: HHandle) -> HHandle`

## Description

`deserialize_calib_data` deserializes a calibration data model,
that was serialized by [`serialize_calib_data`](serialize_calib_data.md) (see
[`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized calibration data model
is defined by the handle *`serialized_item_handle`*.
The deserialized values are stored in an automatically created
calibration data model with the handle *`calib_data_id`*.

Note that [`serialize_calib_data`](serialize_calib_data.md) does not serialize any
calibration results.
Yet, [`calibrate_cameras`](calibrate_cameras.md) can be called for a
fully configured calibration model immediately after the
deserialization. All calibration results are accessible afterwards.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serialized_item_handle`** (input_control)  serialized_item `→` HHandle

Handle of the serialized item.

**`calib_data_id`** (output_control)  calib_data `→` HHandle

Handle of a calibration data model.

## Result

If the parameters are valid, the operator
`deserialize_calib_data` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`fread_serialized_item`,
`receive_serialized_item`,
`serialize_calib_data`

## Module

Calibration
