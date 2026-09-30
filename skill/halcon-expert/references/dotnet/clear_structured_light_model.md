# ClearStructuredLightModel (Operator)

## Name

`ClearStructuredLightModel` — Clear a structured light model and free the allocated memory.

## Signature

`static void HOperatorSet.ClearStructuredLightModel(HTuple structuredLightModel)`

`static void HStructuredLightModel.ClearStructuredLightModel(HStructuredLightModel[] structuredLightModel)`

`void HStructuredLightModel.ClearStructuredLightModel()`

## Description

The operator `ClearStructuredLightModel` deletes a structured
light model that was created by [`CreateStructuredLightModel`](create_structured_light_model.md).
All memory used by the model is freed.
The handle of the model is passed in *`structuredLightModel`*. It is
invalid after the operator call.

For an explanation of the concept of structured light and its supported
applications, see the introduction of chapter
[Inspection / Structured Light](toc_inspection_structuredlight.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- structuredLightModel

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`structuredLightModel`** (input_control, state is modified)  structured_light_model(-array) `→` [HStructuredLightModel](HStructuredLightModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the structured light model.

## Result

The operator `ClearStructuredLightModel` returns the value 2 (
H_MSG_TRUE)
if a valid handle is passed and the referred structured light model can
be freed correctly. Otherwise, an exception will be raised.

## See also

`CreateStructuredLightModel`

## Module

3D Metrology
