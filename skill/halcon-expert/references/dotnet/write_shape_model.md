# WriteShapeModel (Operator)

## Name

`WriteShapeModel` — Write a shape model to a file.

## Signature

`static void HOperatorSet.WriteShapeModel(HTuple modelID, HTuple fileName)`

`void HShapeModel.WriteShapeModel(string fileName)`

## Description

The operator `WriteShapeModel` writes a shape model to the
file *`fileName`*. The model can be read again with
[`ReadShapeModel`](read_shape_model.md). The default HALCON file extension for
the shape model is 'shm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`shm`

## Result

If the file name is valid (write permission), the operator
`WriteShapeModel` returns the value 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`SetGenericShapeModelParam`,
`SetGenericShapeModelObject`

## Module

Matching
