# WriteNccModel (Operator)

## Name

`WriteNccModel` — Write an NCC model to a file.

## Signature

`static void HOperatorSet.WriteNccModel(HTuple modelID, HTuple fileName)`

`void HNCCModel.WriteNccModel(string fileName)`

## Description

The operator `WriteNccModel` writes an NCC model to the file
*`fileName`*. The model can be read again with
[`ReadNccModel`](read_ncc_model.md). The default HALCON file extension for
the NCC model is 'ncm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`ncm`

## Result

If the file name is valid (write permission), the operator
`WriteNccModel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`CreateNccModel`

## Module

Matching
