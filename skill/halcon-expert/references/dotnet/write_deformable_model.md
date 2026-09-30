# WriteDeformableModel (Operator)

## Name

`WriteDeformableModel` — Write a deformable model to a file.

## Signature

`static void HOperatorSet.WriteDeformableModel(HTuple modelID, HTuple fileName)`

`void HDeformableModel.WriteDeformableModel(string fileName)`

## Description

The operator `WriteDeformableModel` writes a deformable model
to the file *`fileName`*. The model can be read again with
[`ReadDeformableModel`](read_deformable_model.md). The default HALCON file extension for
the deformable model is 'dfm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  deformable_model `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a model to be saved.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

The path and filename of the model to be saved.

File extension:
.`dfm`

## Possible Predecessors

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`,
`CreateLocalDeformableModel`

## Module

Matching
