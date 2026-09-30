# ReadDescriptorModel (Operator)

## Name

`ReadDescriptorModel` — Read a descriptor model from a file.

## Signature

`static void HOperatorSet.ReadDescriptorModel(HTuple fileName, out HTuple modelID)`

`public HDescriptorModel(string fileName)`

`void HDescriptorModel.ReadDescriptorModel(string fileName)`

## Description

The operator `ReadDescriptorModel` reads a descriptor
model, which has been written with [`WriteDescriptorModel`](write_descriptor_model.md),
from the file *`fileName`*. The default HALCON file extension
for the descriptor model is 'dsm'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`dsm`

**`modelID`** (output_control)  descriptor_model `→` [HDescriptorModel](HDescriptorModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the model.

## Possible Successors

`FindUncalibDescriptorModel`,
`FindCalibDescriptorModel`

## See also

`CreateCalibDescriptorModel`,
`CreateUncalibDescriptorModel`

## Module

Matching
