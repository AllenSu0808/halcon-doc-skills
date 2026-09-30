# ClearTrainDataVariationModel (Operator)

## Name

`ClearTrainDataVariationModel` — Free the memory of the training data of a variation model.

## Signature

`static void HOperatorSet.ClearTrainDataVariationModel(HTuple modelID)`

`void HVariationModel.ClearTrainDataVariationModel()`

## Description

`ClearTrainDataVariationModel` frees the memory of a
variation model that was created by [`CreateVariationModel`](create_variation_model.md).
`ClearTrainDataVariationModel` can be used to reduce the
amount of memory required for the variation model (in main memory as
well as when writing the model to file with
[`WriteVariationModel`](write_variation_model.md)).
`ClearTrainDataVariationModel` can only be called if the
model has been prepared for comparison with an image with
[`PrepareVariationModel`](prepare_variation_model.md). After the call to
`ClearTrainDataVariationModel` the variation model can
only be used for image comparison with
[`CompareVariationModel`](compare_variation_model.md) or
[`CompareExtVariationModel`](compare_ext_variation_model.md). The model cannot be trained
any further. Furthermore, the images used for the image comparison
can no longer be read with [`GetVariationModel`](get_variation_model.md). If they are
required, [`GetVariationModel`](get_variation_model.md) must be called before
`ClearTrainDataVariationModel` is called.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- modelID

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`modelID`** (input_control, state is modified)  variation_model `→` [HVariationModel](HVariationModel.md), [HTuple](HTuple.md) (*IntPtr*)

ID of the variation model.

## Result

`ClearTrainDataVariationModel` returns 2 (
H_MSG_TRUE)
if all
parameters are correct.

## Possible Predecessors

`PrepareVariationModel`

## Possible Successors

`CompareVariationModel`,
`CompareExtVariationModel`,
`WriteVariationModel`

## Module

Matching
