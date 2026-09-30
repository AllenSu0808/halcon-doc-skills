# ClearCalibData (Operator)

## Name

`ClearCalibData` — Free the memory of a calibration data model.

## Signature

`static void HOperatorSet.ClearCalibData(HTuple calibDataID)`

`void HCalibData.ClearCalibData()`

## Description

The operator `ClearCalibData` frees the memory of the
calibration data model *`calibDataID`*. After calling
`ClearCalibData`, the model can no longer be used. The
handle *`calibDataID`* becomes invalid.

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

## Module

Calibration
