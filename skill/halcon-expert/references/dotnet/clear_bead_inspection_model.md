# ClearBeadInspectionModel (Operator)

## Name

`ClearBeadInspectionModel` — Delete the bead inspection model and free the allocated memory.

## Signature

`static void HOperatorSet.ClearBeadInspectionModel(HTuple beadInspectionModel)`

`void HBeadInspectionModel.ClearBeadInspectionModel()`

## Description

The operator `ClearBeadInspectionModel` deletes a bead inspection
model that was created by [`CreateBeadInspectionModel`](create_bead_inspection_model.md).
All memory used by the model is freed.
The handle of the model is passed in *`beadInspectionModel`*. It is
invalid after the operator call.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- beadInspectionModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`beadInspectionModel`** (input_control, state is modified)  bead_inspection_model `→` [HBeadInspectionModel](HBeadInspectionModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the bead inspection model.

## Result

The operator `ClearBeadInspectionModel` returns the value 2 (
H_MSG_TRUE)
if a valid handle is passed and the referred bead inspection model can
be freed correctly.
Otherwise, an exception will be raised.

## Possible Predecessors

`CreateBeadInspectionModel`

## See also

`CreateBeadInspectionModel`

## Module

2D Metrology
