# ClearShapeModel3d (Operator)

## Name

`ClearShapeModel3d` — Free the memory of a 3D shape model.

## Signature

`static void HOperatorSet.ClearShapeModel3d(HTuple shapeModel3DID)`

`static void HShapeModel3D.ClearShapeModel3d(HShapeModel3D[] shapeModel3DID)`

`void HShapeModel3D.ClearShapeModel3d()`

## Description

The operator `ClearShapeModel3d` frees the memory of a 3D
shape model that was created by [`CreateShapeModel3d`](create_shape_model_3d.md).
After calling `ClearShapeModel3d`, the model can no longer
be used. The handle *`shapeModel3DID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- shapeModel3DID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`shapeModel3DID`** (input_control, state is modified)  shape_model_3d(-array) `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

## Result

If the handle of the model is valid, the operator
`ClearShapeModel3d` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`CreateShapeModel3d`,
`ReadShapeModel3d`,
`WriteShapeModel3d`

## Module

3D Metrology
