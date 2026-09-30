# WriteDescriptorModel (Operator)

## Name

`WriteDescriptorModel` — Write a descriptor model to a file.

## Signature

`static void HOperatorSet.WriteDescriptorModel(HTuple modelID, HTuple fileName)`

`void HDescriptorModel.WriteDescriptorModel(string fileName)`

## Description

The operator `WriteDescriptorModel` writes a descriptor model
to the file *`fileName`*. The model can be read again with
[`ReadDescriptorModel`](read_descriptor_model.md). The default HALCON file extension
for the descriptor model is 'dsm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of a model to be saved.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

The path and filename of the model to be saved.

File extension:
.`dsm`

## Possible Predecessors

`PointsLepetit`,
`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`

## See also

`CreateUncalibDescriptorModel`,
`CreateCalibDescriptorModel`

## Module

Matching
