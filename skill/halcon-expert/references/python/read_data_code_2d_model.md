# read_data_code_2d_model (Operator)

## Name

`read_data_code_2d_model` — Read a 2D code model from a file and create a new model.

## Signature

`def read_data_code_2d_model(file_name: str) -> HHandle`

## Description

The operator `read_data_code_2d_model` reads the 2D code
model file *`file_name`* and creates a new model that is an
identical copy of the saved model.
The parameter *`data_code_handle`* returns the handle of the new
model.
The model file *`file_name`* must be created by the operator
[`write_data_code_2d_model`](write_data_code_2d_model.md).
The default HALCON file extension for the 2D code model is 'dcm'.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`file_name`** (input_control)  filename.read `→` str

Name of the 2D code model file.

Default:
"data_code_model.dcm"

File extension:
.`dcm`

**`data_code_handle`** (output_control)  datacode_2d `→` HHandle

Handle of the created 2D code model.

## Example (HDevelop)

```
* This example demonstrates how a model that was saved in an earlier
* session can be used again by reading the model file

* Create a model by reading by reading a 2D code model file
read_data_code_2d_model ('ecc200_trained_model.dcm', DataCodeHandle)
* Read a symbol image
read_image (Image, 'datacode/ecc200/ecc200_cpu_010')
* Read the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, [], [], \
                   ResultHandles, DecodedDataStrings)
* Clear the model
clear_data_code_2d_model (DataCodeHandle)
```

## Result

The operator `read_data_code_2d_model` returns the value 2 (
H_MSG_TRUE)
if the named 2D code file was found and correctly read.
Otherwise, an exception is raised.

## Possible Successors

`find_data_code_2d`

## Alternatives

`create_data_code_2d_model`

## See also

`write_data_code_2d_model`,
`clear_data_code_2d_model`

## Module

Data Code
