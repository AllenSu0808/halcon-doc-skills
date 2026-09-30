# ClearVariationModel (Operator)

## Name

`ClearVariationModel` — Free the memory of a variation model.

## Signature

`static void HOperatorSet.ClearVariationModel(HTuple modelID)`

`void HVariationModel.ClearVariationModel()`

## Description

`ClearVariationModel` frees the memory of a variation model
that was created by [`CreateVariationModel`](create_variation_model.md). After calling
[`CreateVariationModel`](create_variation_model.md), the model can no longer be used.
The handle *`modelID`* becomes invalid.

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

`ClearVariationModel` returns 2 (
H_MSG_TRUE)
if all parameters are
correct.

## Possible Predecessors

`CreateVariationModel`

## Module

Matching
