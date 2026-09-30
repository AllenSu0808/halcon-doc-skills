# DeserializeCalibData (Operator)

## Name

`DeserializeCalibData` — Deserialize a serialized calibration data model.

## Signature

`static void HOperatorSet.DeserializeCalibData(HTuple serializedItemHandle, out HTuple calibDataID)`

`void HCalibData.DeserializeCalibData(HSerializedItem serializedItemHandle)`

## Description

`DeserializeCalibData` deserializes a calibration data model,
that was serialized by [`SerializeCalibData`](serialize_calib_data.md) (see
[`FwriteSerializedItem`](fwrite_serialized_item.md) for an introduction of the basic
principle of serialization). The serialized calibration data model
is defined by the handle *`serializedItemHandle`*.
The deserialized values are stored in an automatically created
calibration data model with the handle *`calibDataID`*.

Note that [`SerializeCalibData`](serialize_calib_data.md) does not serialize any
calibration results.
Yet, [`CalibrateCameras`](calibrate_cameras.md) can be called for a
fully configured calibration model immediately after the
deserialization. All calibration results are accessible afterwards.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`serializedItemHandle`** (input_control)  serialized_item `→` [HSerializedItem](HSerializedItem.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the serialized item.

**`calibDataID`** (output_control)  calib_data `→` [HCalibData](HCalibData.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a calibration data model.

## Result

If the parameters are valid, the operator
`DeserializeCalibData` returns the value 2 (
H_MSG_TRUE)
. If
necessary, an exception is raised.

## Possible Predecessors

`FreadSerializedItem`,
`ReceiveSerializedItem`,
`SerializeCalibData`

## Module

Calibration
