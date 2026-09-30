# ReadBarCodeModel (Operator)

## Name

`ReadBarCodeModel` — Read a bar code model from a file and create a new model.

## Signature

`static void HOperatorSet.ReadBarCodeModel(HTuple fileName, out HTuple barCodeHandle)`

`public HBarCode(string fileName)`

`void HBarCode.ReadBarCodeModel(string fileName)`

## Description

The operator `ReadBarCodeModel` reads the bar code model from the
file *`fileName`* and creates a new model that is an identical copy of
the saved model. The parameter *`barCodeHandle`* returns the handle
of the new model. The model file *`fileName`* must have been created
by the operator [`WriteBarCodeModel`](write_bar_code_model.md).
The default HALCON file extension for bar code model is 'bcm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

Name of the bar code model file.

Default:
"bar_code_model.bcm"

File extension:
.`bcm`

**`barCodeHandle`** (output_control)  barcode `→` [HBarCode](HBarCode.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bar code model.

## Result

The operator `ReadBarCodeModel` returns the value 2 (
H_MSG_TRUE)
if the named bar code file was found and correctly read.
Otherwise, an exception is raised.

## Possible Successors

`FindBarCode`

## Alternatives

`CreateBarCodeModel`

## See also

`WriteBarCodeModel`,
`ClearBarCodeModel`

## Module

Bar Code
