# ReadVariationModel (Operator)

## Name

`ReadVariationModel` — Read a variation model from a file.

## Signature

`static void HOperatorSet.ReadVariationModel(HTuple fileName, out HTuple modelID)`

`public HVariationModel(string fileName)`

`void HVariationModel.ReadVariationModel(string fileName)`

## Description

The operator `ReadVariationModel` reads a variation model,
which has been written with [`WriteVariationModel`](write_variation_model.md), from the
file *`fileName`*.
The default HALCON file extension for a variation model is 'vam'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`fileName`** (input_control)  filename.read `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`vam`

**`modelID`** (output_control)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

## Result

If the file name is valid, the operator `ReadVariationModel`
returns 2 (
H_MSG_TRUE)
. If necessary an exception is raised.

## Possible Successors

`CompareVariationModel`,
`CompareExtVariationModel`

## See also

`WriteVariationModel`

## Module

Matching
