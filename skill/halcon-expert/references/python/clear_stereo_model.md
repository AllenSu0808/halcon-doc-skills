# clear_stereo_model (Operator)

## Name

`clear_stereo_model` — Free the memory of a stereo model.

## Signature

`def clear_stereo_model(stereo_model_id: HHandle) -> None`

## Description

The operator `clear_stereo_model` frees the memory of the
stereo model *`stereo_model_id`* that was created by
[`create_stereo_model`](create_stereo_model.md). After
calling `clear_stereo_model`, the model can no longer be used.
The handle *`stereo_model_id`* becomes invalid.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- stereo_model_id

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`stereo_model_id`** (input_control, state is modified)  stereo_model `→` HHandle

Handle of the stereo model.

## Module

3D Metrology
