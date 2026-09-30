# reset_sheet_of_light_model (Operator)

## Name

`reset_sheet_of_light_model` — Reset a sheet-of-light model.

## Signature

`reset_sheet_of_light_model( : : SheetOfLightModelID : )`

## Description

The operator `reset_sheet_of_light_model` resets a sheet-of-light
model that was created by [`create_sheet_of_light_model`](create_sheet_of_light_model.md).
All indices and result arrays used by the model are reset.
The parameters of the model remain unchanged.
The handle of the model is passed in *`SheetOfLightModelID`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- SheetOfLightModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`SheetOfLightModelID`** (input_control, state is modified)  sheet_of_light_model `→`  (handle)

Handle of the sheet-of-light model.

## Result

The operator `reset_sheet_of_light_model` returns the value 2 (
H_MSG_TRUE)
if a valid handle is passed and the sheet-of-light model can
be reset correctly. Otherwise, an exception will be raised.

## See also

`clear_sheet_of_light_model`

## Module

3D Metrology
