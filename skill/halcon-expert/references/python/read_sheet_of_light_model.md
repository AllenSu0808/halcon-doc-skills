# read_sheet_of_light_model (Operator)

## Name

`read_sheet_of_light_model` — Read a sheet-of-light model from a file and create a new model.

## Signature

`def read_sheet_of_light_model(file_name: str) -> HHandle`

## Description

The operator `read_sheet_of_light_model` reads the sheet-of-light model
from the file *`file_name`* and creates a new model that is an identical
copy of the saved model. The parameter *`sheet_of_light_model_id`* returns
the handle of the new model.
The model file *`file_name`* must have been created
by the operator [`write_sheet_of_light_model`](write_sheet_of_light_model.md).
The default HALCON file extension for sheet-of-light model is 'solm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Name of the sheet-of-light model file.

Default:
"sheet_of_light_model.solm"

File extension:
.`solm`

**`sheet_of_light_model_id`** (output_control)  sheet_of_light_model `→` HHandle

Handle of the sheet-of-light model.

## Result

The operator `read_sheet_of_light_model` returns the value 2 (
H_MSG_TRUE)
if the named file was found and correctly read.
Otherwise, an exception is raised.

## Possible Successors

`measure_profile_sheet_of_light`

## Alternatives

`create_sheet_of_light_model`

## See also

`write_sheet_of_light_model`

## Module

3D Metrology
