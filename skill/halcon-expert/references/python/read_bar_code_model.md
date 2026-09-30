# read_bar_code_model (Operator)

## Name

`read_bar_code_model` — Read a bar code model from a file and create a new model.

## Signature

`def read_bar_code_model(file_name: str) -> HHandle`

## Description

The operator `read_bar_code_model` reads the bar code model from the
file *`file_name`* and creates a new model that is an identical copy of
the saved model. The parameter *`bar_code_handle`* returns the handle
of the new model. The model file *`file_name`* must have been created
by the operator [`write_bar_code_model`](write_bar_code_model.md).
The default HALCON file extension for bar code model is 'bcm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Name of the bar code model file.

Default:
"bar_code_model.bcm"

File extension:
.`bcm`

**`bar_code_handle`** (output_control)  barcode `→` HHandle

Handle of the bar code model.

## Result

The operator `read_bar_code_model` returns the value 2 (
H_MSG_TRUE)
if the named bar code file was found and correctly read.
Otherwise, an exception is raised.

## Possible Successors

`find_bar_code`

## Alternatives

`create_bar_code_model`

## See also

`write_bar_code_model`,
`clear_bar_code_model`

## Module

Bar Code
