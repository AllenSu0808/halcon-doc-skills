# write_data_code_2d_model (Operator)

## Name

`write_data_code_2d_model` — Writes a 2D code model into a file.

## Signature

`write_data_code_2d_model( : : DataCodeHandle, FileName : )`

## Description

The operator `write_data_code_2d_model` writes a 2D code
model, which was created by [`create_data_code_2d_model`](create_data_code_2d_model.md), into
a file with the name *`FileName`*.
This facilitates creating an identical copy of the saved model in a
later session with the operator [`read_data_code_2d_model`](read_data_code_2d_model.md).
The default HALCON file extension for the 2D code model is 'dcm'.
The handle of the model to write is passed in *`DataCodeHandle`*.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DataCodeHandle`** (input_control)  datacode_2d `→`  (handle)

Handle of the 2D code model.

**`FileName`** (input_control)  filename.write `→`  (string)

Name of the 2D code model file.

Default:
'data_code_model.dcm'

File extension:
.`dcm`

## Example (HDevelop)

```
* This example demonstrates how a trained model can be saved for
* a future session

* Create a model for reading Data Matrix ECC 200 codes
create_data_code_2d_model ('Data Matrix ECC 200', [], [], DataCodeHandle)
* Read a training image
read_image (Image, 'datacode/ecc200/ecc200_cpu_007')
* Train the model with the symbol in the image
find_data_code_2d (Image, SymbolXLDs, DataCodeHandle, 'train', 'all', \
                   ResultHandles, DecodedDataStrings)
* Write the model into a file
write_data_code_2d_model (DataCodeHandle, 'ecc200_trained_model.dcm')
* Clear the model
clear_data_code_2d_model (DataCodeHandle)
```

## Result

The operator `write_data_code_2d_model` returns the value 2 (
H_MSG_TRUE)
if the passed handle is valid and if the model can be written into
the named file.
Otherwise, an exception is raised.

## Possible Predecessors

`set_data_code_2d_param`,
`find_data_code_2d`

## Alternatives

`get_data_code_2d_param`

## See also

`create_data_code_2d_model`,
`set_data_code_2d_param`,
`find_data_code_2d`

## Module

Data Code
