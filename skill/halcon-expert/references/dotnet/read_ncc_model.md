# ReadNccModel (Operator)

## Name

`ReadNccModel` — Read an NCC model from a file.

## Signature

`static void HOperatorSet.ReadNccModel(HTuple fileName, out HTuple modelID)`

`public HNCCModel(string fileName)`

`void HNCCModel.ReadNccModel(string fileName)`

## Description

The operator `ReadNccModel` reads an NCC model, which has
been written with [`WriteNccModel`](write_ncc_model.md), from the file
*`fileName`*. The default HALCON file extension for
the NCC model is 'ncm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`ncm`

**`modelID`** (output_control)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the file name is valid, the operator `ReadNccModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`FindNccModel`,
`FindNccModels`

## See also

`CreateNccModel`,
`ClearNccModel`

## Module

Matching
