# ResetSheetOfLightModel (Operator)

## Name

`ResetSheetOfLightModel` — Reset a sheet-of-light model.

## Signature

`static void HOperatorSet.ResetSheetOfLightModel(HTuple sheetOfLightModelID)`

`void HSheetOfLightModel.ResetSheetOfLightModel()`

## Description

The operator `ResetSheetOfLightModel` resets a sheet-of-light
model that was created by [`CreateSheetOfLightModel`](create_sheet_of_light_model.md).
All indices and result arrays used by the model are reset.
The parameters of the model remain unchanged.
The handle of the model is passed in *`sheetOfLightModelID`*.

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

The operator `ResetSheetOfLightModel` returns the value 2 (
H_MSG_TRUE)
if a valid handle is passed and the sheet-of-light model can
be reset correctly. Otherwise, an exception will be raised.

## See also

`ClearSheetOfLightModel`

## Module

3D Metrology
