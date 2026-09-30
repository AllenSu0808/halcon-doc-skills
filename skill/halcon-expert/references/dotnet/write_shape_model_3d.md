# WriteShapeModel3d (Operator)

## Name

`WriteShapeModel3d` — Write a 3D shape model to a file.

## Signature

`static void HOperatorSet.WriteShapeModel3d(HTuple shapeModel3DID, HTuple fileName)`

`void HShapeModel3D.WriteShapeModel3d(string fileName)`

## Description

The operator `WriteShapeModel3d` writes a 3D shape model to
the file *`fileName`*. The model can be read again with
[`ReadShapeModel3d`](read_shape_model_3d.md). The default HALCON file extension for the
3D shape model is 'sm3'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`shapeModel3DID`** (input_control)  shape_model_3d `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`sm3`

## Result

If the file name is valid (write permission), the operator
`WriteShapeModel3d` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## Possible Predecessors

`CreateShapeModel3d`

## Module

3D Metrology
