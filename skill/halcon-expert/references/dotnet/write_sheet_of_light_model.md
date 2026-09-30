# WriteSheetOfLightModel (Operator)

## Name

`WriteSheetOfLightModel` — Write a sheet-of-light model to a file.

## Signature

`static void HOperatorSet.WriteSheetOfLightModel(HTuple sheetOfLightModelID, HTuple fileName)`

`void HSheetOfLightModel.WriteSheetOfLightModel(string fileName)`

## Description

The operator `WriteSheetOfLightModel` writes the sheet-of-light
model *`sheetOfLightModelID`* to the file *`fileName`*. The model
can be read again with [`ReadSheetOfLightModel`](read_sheet_of_light_model.md).
The stored data contains all generic model parameters
(see [`SetSheetOfLightParam`](set_sheet_of_light_param.md)) and the results of
[`CalibrateSheetOfLight`](calibrate_sheet_of_light.md).

The default HALCON file extension for sheet-of-light model is 'solm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sheetOfLightModelID`** (input_control)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the sheet-of-light model file.

Default:
"sheet_of_light_model.solm"

File extension:
.`solm`

## Result

The operator `WriteSheetOfLightModel` returns the value 2 (
H_MSG_TRUE)
if the passed handle is valid and if the model can be written into
the named file.
Otherwise, an exception is raised.

## Possible Predecessors

`CreateSheetOfLightModel`,
`SetSheetOfLightParam`

## See also

`ReadSheetOfLightModel`

## Module

3D Metrology
