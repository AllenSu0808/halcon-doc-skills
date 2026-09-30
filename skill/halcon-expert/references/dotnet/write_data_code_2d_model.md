# WriteDataCode2dModel (Operator)

## Name

`WriteDataCode2dModel` — Writes a 2D code model into a file.

## Signature

`static void HOperatorSet.WriteDataCode2dModel(HTuple dataCodeHandle, HTuple fileName)`

`void HDataCode2D.WriteDataCode2dModel(string fileName)`

## Description

The operator `WriteDataCode2dModel` writes a 2D code
model, which was created by [`CreateDataCode2dModel`](create_data_code_2d_model.md), into
a file with the name *`fileName`*.
This facilitates creating an identical copy of the saved model in a
later session with the operator [`ReadDataCode2dModel`](read_data_code_2d_model.md).
The default HALCON file extension for the 2D code model is 'dcm'.
The handle of the model to write is passed in *`dataCodeHandle`*.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dataCodeHandle`** (input_control)  datacode_2d `→` [HDataCode2D](HDataCode2D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 2D code model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

Name of the 2D code model file.

Default:
"data_code_model.dcm"

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

The operator `WriteDataCode2dModel` returns the value 2 (
H_MSG_TRUE)
if the passed handle is valid and if the model can be written into
the named file.
Otherwise, an exception is raised.

## Possible Predecessors

`SetDataCode2dParam`,
`FindDataCode2d`

## Alternatives

`GetDataCode2dParam`

## See also

`CreateDataCode2dModel`,
`SetDataCode2dParam`,
`FindDataCode2d`

## Module

Data Code
