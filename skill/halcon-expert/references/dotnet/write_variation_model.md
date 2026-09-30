# WriteVariationModel (Operator)

## Name

`WriteVariationModel` — Write a variation model to a file.

## Signature

`static void HOperatorSet.WriteVariationModel(HTuple modelID, HTuple fileName)`

`void HVariationModel.WriteVariationModel(string fileName)`

## Description

`WriteVariationModel` writes a variation model to the file
*`fileName`*. The model can be read with
[`ReadVariationModel`](read_variation_model.md). The default HALCON file extension for a
variation model is 'vam'.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`modelID`** (input_control)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

**`fileName`** (input_control)  filename.write `→` [HTuple](HTuple.md) (*string*)

File name.

File extension:
.`vam`

## Result

If the file name is valid (write permission), the operator
`WriteVariationModel` returns 2 (
H_MSG_TRUE)
. If necessary an
exception is raised.

## Possible Predecessors

`TrainVariationModel`

## See also

`ReadVariationModel`

## Module

Matching
