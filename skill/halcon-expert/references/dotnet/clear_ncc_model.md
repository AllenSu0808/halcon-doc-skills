# ClearNccModel (Operator)

## Name

`ClearNccModel` — Free the memory of an NCC model.

## Signature

`static void HOperatorSet.ClearNccModel(HTuple modelID)`

`void HNCCModel.ClearNccModel()`

## Description

The operator `ClearNccModel` frees the memory of an NCC
model that was created by [`CreateNccModel`](create_ncc_model.md). After calling
`ClearNccModel`, the model can no longer be used. The
handle *`modelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  ncc_model `→` [HNCCModel](HNCCModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the handle of the model is valid, the operator
`ClearNccModel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`CreateNccModel`,
`ReadNccModel`,
`WriteNccModel`,
`FindNccModel`,
`FindNccModels`

## Module

Matching
