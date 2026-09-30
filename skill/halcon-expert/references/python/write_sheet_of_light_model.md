# write_sheet_of_light_model (Operator)

## Name

`write_sheet_of_light_model` — Write a sheet-of-light model to a file.

## Signature

`def write_sheet_of_light_model(sheet_of_light_model_id: HHandle, file_name: str) -> None`

## Description

The operator `write_sheet_of_light_model` writes the sheet-of-light
model *`sheet_of_light_model_id`* to the file *`file_name`*. The model
can be read again with [`read_sheet_of_light_model`](read_sheet_of_light_model.md).
The stored data contains all generic model parameters
(see [`set_sheet_of_light_param`](set_sheet_of_light_param.md)) and the results of
[`calibrate_sheet_of_light`](calibrate_sheet_of_light.md).

The default HALCON file extension for sheet-of-light model is 'solm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`sheet_of_light_model_id`** (input_control)  sheet_of_light_model `→` HHandle

Handle of the sheet-of-light model.

**`file_name`** (input_control)  filename.write `→` str

Name of the sheet-of-light model file.

Default:
"sheet_of_light_model.solm"

File extension:
.`solm`

## Result

The operator `write_sheet_of_light_model` returns the value 2 (
H_MSG_TRUE)
if the passed handle is valid and if the model can be written into
the named file.
Otherwise, an exception is raised.

## Possible Predecessors

`create_sheet_of_light_model`,
`set_sheet_of_light_param`

## See also

`read_sheet_of_light_model`

## Module

3D Metrology
