# clear_sheet_of_light_model (Operator)

## Name

`clear_sheet_of_light_model` — Delete a sheet-of-light model and free the allocated memory.

## Signature

`def clear_sheet_of_light_model(sheet_of_light_model_id: HHandle) -> None`

## Description

The operator `clear_sheet_of_light_model` deletes a sheet-of-light
model that was created by [`create_sheet_of_light_model`](create_sheet_of_light_model.md).
All memory used by the model is freed.
The handle of the model is passed in *`sheet_of_light_model_id`*.
After the operator call it is invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- sheet_of_light_model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`sheet_of_light_model_id`** (input_control, state is modified)  sheet_of_light_model `→` HHandle

Handle of the sheet-of-light model.

## Result

The operator `clear_sheet_of_light_model` returns the value 2 (
H_MSG_TRUE)
if a valid handle is passed and the referred sheet-of-light model can
be freed correctly.
Otherwise, an exception will be raised.

## See also

`create_sheet_of_light_model`

## Module

3D Metrology
