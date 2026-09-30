# SerializeCalibData (Operator)

## Name

`SerializeCalibData` — Serialize a calibration data model.

## Signature

`static void HOperatorSet.SerializeCalibData(HTuple calibDataID, out HTuple serializedItemHandle)`

`HSerializedItem HCalibData.SerializeCalibData()`

## Description

`SerializeCalibData` serializes the data of a calibration data model
(see [`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the
basic principle of serialization). The same data that is written
in a file by [`WriteCalibData`](write_calib_data.md) is converted to a serialized
item. The calibration data model is defined by the handle
*`calibDataID`*. The serialized calibration data model is returned
by the handle *`serializedItemHandle`* and can be deserialized
by [`DeserializeCalibData`](deserialize_calib_data.md).

Note that no calibration results are serialized. You can
access them with the operator [`GetCalibData`](get_calib_data.md), either as
individual items or in form of a camera setup model and
store them separately.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- calibDataID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`calibDataID`** (input_control, state is modified)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

**`serializedItemHandle`** (output_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

## Result

If the parameters are valid, the operator
`SerializeCalibData` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Successors

`FwriteSerializedItem`,
`SendSerializedItem`,
`DeserializeCalibData`

## Module

Calibration
