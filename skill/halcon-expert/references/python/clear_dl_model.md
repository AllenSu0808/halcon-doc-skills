# clear_dl_model (Operator)

## Name

`clear_dl_model` — Clear a deep learning model.

## Signature

`def clear_dl_model(dlmodel_handle: MaybeSequence[HHandle]) -> None`

## Description

`clear_dl_model` clears the handle of the deep learning model given
by *`dlmodel_handle`* and frees all memory required for the model.
After calling `clear_dl_model`, the model can no longer be used
and the handle *`dlmodel_handle`* becomes invalid.

For further explanations to deep learning models in HALCON,
see the chapter [Deep Learning / Model](toc_deeplearning_model.md).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: local (may only be called from the same thread in which the window, model, or tool instance was created).
- Processed without parallelization.

This operator modifies the state of the following input parameter:

- dlmodel_handle

During execution of this operator, access to the value of this parameter must be synchronized if it is used across multiple threads.

## Parameters

**`dlmodel_handle`** (input_control, state is modified)  dl_model(-array) `→` MaybeSequence[HHandle]

Handle of the deep learning model.

## Result

If the parameters are valid, the operator `clear_dl_model`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Possible Predecessors

`read_dl_model`,
`apply_dl_model`,
`train_dl_model_batch`,
`train_dl_model_anomaly_dataset`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
3D Metrology, OCR/OCV, Matching, Deep Learning Enhanced, Deep Learning Professional
