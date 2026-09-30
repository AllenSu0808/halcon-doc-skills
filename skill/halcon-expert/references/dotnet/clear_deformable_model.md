# ClearDeformableModel (Operator)

## Name

`ClearDeformableModel` — Free the memory of a deformable model.

## Signature

`static void HOperatorSet.ClearDeformableModel(HTuple modelID)`

`static void HDeformableModel.ClearDeformableModel(HDeformableModel[] modelID)`

`void HDeformableModel.ClearDeformableModel()`

## Description

The operator `ClearDeformableModel` frees the memory of a deformable
model that was created by [`CreatePlanarUncalibDeformableModel`](create_planar_uncalib_deformable_model.md)
or [`CreatePlanarCalibDeformableModel`](create_planar_calib_deformable_model.md).
After calling `ClearDeformableModel`, the deformable model can no
longer be used. The handle *`modelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  deformable_model(-array) `→` [HDeformableModel](HDeformableModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Result

If the parameters are valid, the operator
`ClearDeformableModel` returns the value 2 (
H_MSG_TRUE)
. If
necessary an exception is raised.

## See also

`CreatePlanarUncalibDeformableModel`,
`CreatePlanarCalibDeformableModel`,
`CreateLocalDeformableModel`

## Module

Matching
