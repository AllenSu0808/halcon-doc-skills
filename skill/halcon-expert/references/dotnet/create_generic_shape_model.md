# CreateGenericShapeModel (Operator)

## Name

`CreateGenericShapeModel` — Create a shape model.

## Signature

`static void HOperatorSet.CreateGenericShapeModel(out HTuple modelID)`

`public HShapeModel()`

`void HShapeModel.CreateGenericShapeModel()`

## Description

The operator `CreateGenericShapeModel` creates a shape
model and returns its handle in *`modelID`*.

The created model is not trained. See [`TrainGenericShapeModel`](train_generic_shape_model.md)
for information about training a model.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`modelID`** (output_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the shape model.

## Result

If successful the operator `CreateGenericShapeModel` returns the
value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Successors

`SetGenericShapeModelParam`,
`TrainGenericShapeModel`,
`WriteShapeModel`,
`SetShapeModelOrigin`

## Module

Matching
