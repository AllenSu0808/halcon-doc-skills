# ReadDataCode2dModel (Operator)

## Name

`ReadDataCode2dModel` — Read a 2D code model from a file and create a new model.

## Signature

`static void HOperatorSet.ReadDataCode2dModel(HTuple fileName, out HTuple dataCodeHandle)`

`public HDataCode2D(string fileName)`

`void HDataCode2D.ReadDataCode2dModel(string fileName)`

## Description

The operator `ReadDataCode2dModel` reads the 2D code
model file *`fileName`* and creates a new model that is an
identical copy of the saved model.
The parameter *`dataCodeHandle`* returns the handle of the new
model.
The model file *`fileName`* must be created by the operator
[`WriteDataCode2dModel`](write_data_code_2d_model.md).
The default HALCON file extension for the 2D code model is 'dcm'.

For an explanation of the concept of the 2D code reader
see the introduction of chapter [Identification / 2D Code](toc_identification_datacode.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the 2D code model file.

Default:
"data_code_model.dcm"

File extension:
.`dcm`

**`dataCodeHandle`** (output_control)  datacode_2d `→` [HDataCode2D](HDataCode2D.md), [HTuple](HTuple.md) (*IntPtr*)

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

The operator `ReadDataCode2dModel` returns the value 2 (
H_MSG_TRUE)
if the named 2D code file was found and correctly read.
Otherwise, an exception is raised.

## Possible Successors

`FindDataCode2d`

## Alternatives

`CreateDataCode2dModel`

## See also

`WriteDataCode2dModel`,
`ClearDataCode2dModel`

## Module

Data Code
