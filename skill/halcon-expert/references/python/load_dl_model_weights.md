# load_dl_model_weights (Operator)

## Name

`load_dl_model_weights` — Load the weights of a source model into a target model.

## Signature

`def load_dl_model_weights(dlmodel_handle_source: HHandle, dlmodel_handle_target: HHandle) -> Sequence[int]`

`def load_dl_model_weights_s(dlmodel_handle_source: HHandle, dlmodel_handle_target: HHandle) -> int`

## Description

The operator `load_dl_model_weights` loads weights of a source model
*`dlmodel_handle_source`* into a target model *`dlmodel_handle_target`*.
Thereby applies for every layer in the target model: Its weights are only
changed if there is a layer in the source model having the same name and the
same weight-shape.
Note that *`dlmodel_handle_source`* must be different from
*`dlmodel_handle_target`*, i.e., you cannot use the same model handle as
source and target.

*`changes_by_layer`* is a tuple indicating for every target layer how many
weights changed.
Its entries are sorted by ascending layer IDs. The layer IDs can be queried
via the operator [`get_dl_model_param`](get_dl_model_param.md) with the parameter
*"summary"*.

Note, that 'weights' means all weights and biases for all layers which
can have such values (e.g., convolutional layer, batch normalization layer,
etc.).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dlmodel_handle_source`** (input_control)  dl_model `→` HHandle

Handle of the source deep learning model.

**`dlmodel_handle_target`** (input_control)  dl_model `→` HHandle

Handle of the target deep learning model.

**`changes_by_layer`** (output_control)  integer(-array) `→` Sequence[int]

Indicates for every target layer how many weights
changed.

## Result

If the parameters are valid, the operator `load_dl_model_weights`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Module

Deep Learning Professional
