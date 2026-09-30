# ReadShapeModel3d (Operator)

## Name

`ReadShapeModel3d` — Read a 3D shape model from a file.

## Signature

`static void HOperatorSet.ReadShapeModel3d(HTuple fileName, out HTuple shapeModel3DID)`

`public HShapeModel3D(string fileName)`

`void HShapeModel3D.ReadShapeModel3d(string fileName)`

## Description

The operator `ReadShapeModel3d` reads a 3D shape model, which
has been written with [`WriteShapeModel3d`](write_shape_model_3d.md), from the file
*`fileName`*. The default HALCON file extension for the 3D
shape model is 'sm3'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`sm3`

**`shapeModel3DID`** (output_control)  shape_model_3d `→` [HShapeModel3D](HShapeModel3D.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the 3D shape model.

## Result

If the file name is valid, the operator `ReadShapeModel3d`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`FindShapeModel3d`,
`GetShapeModel3dParams`

## See also

`CreateShapeModel3d`,
`ClearShapeModel3d`

## Module

3D Metrology
