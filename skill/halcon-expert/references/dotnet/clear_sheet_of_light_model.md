# ClearSheetOfLightModel (Operator)

## Name

`ClearSheetOfLightModel` — Delete a sheet-of-light model and free the allocated memory.

## Signature

`static void HOperatorSet.ClearSheetOfLightModel(HTuple sheetOfLightModelID)`

`void HSheetOfLightModel.ClearSheetOfLightModel()`

## Description

The operator `ClearSheetOfLightModel` deletes a sheet-of-light
model that was created by [`CreateSheetOfLightModel`](create_sheet_of_light_model.md).
All memory used by the model is freed.
The handle of the model is passed in *`sheetOfLightModelID`*.
After the operator call it is invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- sheetOfLightModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`sheetOfLightModelID`** (input_control, state is modified)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model.

## Result

The operator `ClearSheetOfLightModel` returns the value 2 (
H_MSG_TRUE)
if a valid handle is passed and the referred sheet-of-light model can
be freed correctly.
Otherwise, an exception will be raised.

## See also

`CreateSheetOfLightModel`

## Module

3D Metrology
