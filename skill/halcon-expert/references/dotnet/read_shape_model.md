# ReadShapeModel (Operator)

## Name

`ReadShapeModel` — Read a shape model from a file.

## Signature

`static void HOperatorSet.ReadShapeModel(HTuple fileName, out HTuple modelID)`

`public HShapeModel(string fileName)`

`void HShapeModel.ReadShapeModel(string fileName)`

## Description

The operator `ReadShapeModel` reads a shape model, which has
been written with [`WriteShapeModel`](write_shape_model.md), from the file
*`fileName`*. The default HALCON file extension for
the shape model is 'shm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`shm`

**`modelID`** (output_control)  shape_model `→` [HShapeModel](HShapeModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the file name is valid, the operator `ReadShapeModel`
returns the value 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`FindGenericShapeModel`

## Module

Matching
