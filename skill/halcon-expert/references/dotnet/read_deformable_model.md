# ReadDeformableModel (Operator)

## Name

`ReadDeformableModel` — Read a deformable model from a file.

## Signature

`static void HOperatorSet.ReadDeformableModel(HTuple fileName, out HTuple modelID)`

`public HDeformableModel(string fileName)`

`void HDeformableModel.ReadDeformableModel(string fileName)`

## Description

The operator `ReadDeformableModel` reads a deformable model from the
file *`fileName`*, which has been written with
[`WriteDeformableModel`](write_deformable_model.md). The default HALCON file extension for the
deformable model is 'dfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`dfm`

**`modelID`** (output_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Possible Successors

`FindPlanarUncalibDeformableModel`,
`FindPlanarCalibDeformableModel`,
`FindLocalDeformableModel`

## See also

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`,
`CreateLocalDeformableModel`

## Module

Matching
