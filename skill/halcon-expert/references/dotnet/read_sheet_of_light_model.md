# ReadSheetOfLightModel (Operator)

## Name

`ReadSheetOfLightModel` — Read a sheet-of-light model from a file and create a new model.

## Signature

`static void HOperatorSet.ReadSheetOfLightModel(HTuple fileName, out HTuple sheetOfLightModelID)`

`public HSheetOfLightModel(string fileName)`

`void HSheetOfLightModel.ReadSheetOfLightModel(string fileName)`

## Description

The operator `ReadSheetOfLightModel` reads the sheet-of-light model
from the file *`fileName`* and creates a new model that is an identical
copy of the saved model. The parameter *`sheetOfLightModelID`* returns
the handle of the new model.
The model file *`fileName`* must have been created
by the operator [`WriteSheetOfLightModel`](write_sheet_of_light_model.md).
The default HALCON file extension for sheet-of-light model is 'solm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the sheet-of-light model file.

Default:
"sheet_of_light_model.solm"

File extension:
.`solm`

**`sheetOfLightModelID`** (output_control)  sheet_of_light_model `→` [HSheetOfLightModel](HSheetOfLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the sheet-of-light model.

## Result

The operator `ReadSheetOfLightModel` returns the value 2 (
H_MSG_TRUE)
if the named file was found and correctly read.
Otherwise, an exception is raised.

## Possible Successors

`MeasureProfileSheetOfLight`

## Alternatives

`CreateSheetOfLightModel`

## See also

`WriteSheetOfLightModel`

## Module

3D Metrology
