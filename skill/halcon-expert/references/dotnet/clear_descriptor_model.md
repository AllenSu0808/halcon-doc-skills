# ClearDescriptorModel (Operator)

## Name

`ClearDescriptorModel` — Free the memory of a descriptor model.

## Signature

`static void HOperatorSet.ClearDescriptorModel(HTuple modelID)`

`static void HDescriptorModel.ClearDescriptorModel(HDescriptorModel[] modelID)`

`void HDescriptorModel.ClearDescriptorModel()`

## Description

The operator `ClearDescriptorModel` frees the memory of a
descriptor model that was created by
[`CreateCalibDescriptorModel`](create_calib_descriptor_model.md)
or [`CreateUncalibDescriptorModel`](create_uncalib_descriptor_model.md).
After calling `ClearDescriptorModel`, the model can no longer be
used. The handle *`modelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  descriptor_model(-array) `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the descriptor model.

## Result

If the handle of the model is valid, the operator
`ClearDescriptorModel` returns the value 2 (
H_MSG_TRUE)
. If necessary
an exception is raised.

## See also

`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`

## Module

Matching
