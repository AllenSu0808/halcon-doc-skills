# ClearShapeModel (Operator)

## Name

`ClearShapeModel` — Free the memory of a shape model.

## Signature

`static void HOperatorSet.ClearShapeModel(HTuple modelID)`

`void HShapeModel.ClearShapeModel()`

## Description

The operator `ClearShapeModel` frees the memory of a shape
model that was created by [`CreateShapeModel`](create_shape_model.md),
[`CreateScaledShapeModel`](create_scaled_shape_model.md), or
[`CreateAnisoShapeModel`](create_aniso_shape_model.md). After calling
`ClearShapeModel`, the model can no longer be used. The
handle *`modelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the handle of the model is valid, the operator
`ClearShapeModel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`CreateGenericShapeModel`,
`WriteShapeModel`

## Module

Matching
