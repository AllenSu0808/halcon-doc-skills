# serialize_calib_data (Operator)

## Name

`serialize_calib_data` — Serialize a calibration data model.

## Signature

`serialize_calib_data( : : CalibDataID : SerializedItemHandle)`

## Description

`serialize_calib_data` serializes the data of a calibration data model
(see [`fwrite_serialized_item`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`write_calib_data`](write_calib_data.md) is converted to a serialized
item. The calibration data model is defined by the handle
*`CalibDataID`*. The serialized calibration data model is returned
by the handle *`SerializedItemHandle`* and can be deserialized
by [`deserialize_calib_data`](deserialize_calib_data.md).

Note that no calibration results are serialized. You can
access them with the operator [`get_calib_data`](get_calib_data.md), either as
individual items or in form of a camera setup model and
store them separately.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- CalibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`CalibDataID`** (input_control, state is modified)  calib_data `→`  (handle)

Handle of a calibration data model.

**`SerializedItemHandle`** (output_control)  serialized_item `→`  (handle)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`serialize_calib_data` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`fwrite_serialized_item`,
`send_serialized_item`,
`deserialize_calib_data`

## Module

Calibration
