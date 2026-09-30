# ClearStereoModel (Operator)

## Name

`ClearStereoModel` — Free the memory of a stereo model.

## Signature

`static void HOperatorSet.ClearStereoModel(HTuple stereoModelID)`

`void HStereoModel.ClearStereoModel()`

## Description

The operator `ClearStereoModel` frees the memory of the
stereo model *`stereoModelID`* that was created by
[`CreateStereoModel`](create_stereo_model.md). After
calling `ClearStereoModel`, the model can no longer be used.
The handle *`stereoModelID`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- stereoModelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`stereoModelID`** (input_control, state is modified)  stereo_model `→` [HStereoModel](HStereoModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the stereo model.

## Module

3D Metrology
