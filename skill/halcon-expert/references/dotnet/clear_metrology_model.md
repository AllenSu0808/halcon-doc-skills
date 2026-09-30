# ClearMetrologyModel (Operator)

## Name

`ClearMetrologyModel` — Delete a metrology model and free the allocated memory.

## Signature

`static void HOperatorSet.ClearMetrologyModel(HTuple metrologyHandle)`

`void HMetrologyModel.ClearMetrologyModel()`

## Description

`ClearMetrologyModel` deletes a metrology model that was
created by [`CreateMetrologyModel`](create_metrology_model.md), [`CopyMetrologyModel`](copy_metrology_model.md),
[`ReadMetrologyModel`](read_metrology_model.md), or [`DeserializeMetrologyModel`](deserialize_metrology_model.md).
Note that by deleting the model also the including
metrology objects are deleted. All memory used by the metrology
model and the metrology objects is freed. The handle of the model is
passed in *`metrologyHandle`*. After the operator call, the
metrology model is invalid.

For an explanation of the concept of 2D metrology see the
introduction of chapter [2D Metrology](toc_2dmetrology.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- metrologyHandle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`metrologyHandle`** (input_control, state is modified)  metrology_model `→` [HMetrologyModel](HMetrologyModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the metrology model.

## Result

The operator `ClearMetrologyModel` returns the value 2 (
H_MSG_TRUE)
if a valid handle was passed and the referred metrology model can
be freed correctly. Otherwise, an exception will be raised.

## Possible Predecessors

`GetMetrologyObjectResult`,
`WriteMetrologyModel`

## Module

2D Metrology
