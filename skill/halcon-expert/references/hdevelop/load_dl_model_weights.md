# load_dl_model_weights (Operator)

## Name

`load_dl_model_weights` — Load the weights of a source model into a target model.

## Signature

`load_dl_model_weights( : : DLModelHandleSource, DLModelHandleTarget : ChangesByLayer)`

## Description

The operator `load_dl_model_weights` loads weights of a source model
*`DLModelHandleSource`* into a target model *`DLModelHandleTarget`*.
Thereby applies for every layer in the target model: Its weights are only
changed if there is a layer in the source model having the same name and the
same weight-shape.
Note that *`DLModelHandleSource`* must be different from
*`DLModelHandleTarget`*, i.e., you cannot use the same model handle as
source and target.

*`ChangesByLayer`* is a tuple indicating for every target layer how many
weights changed.
Its entries are sorted by ascending layer IDs. The layer IDs can be queried
via the operator [`get_dl_model_param`](get_dl_model_param.md) with the parameter
*'summary'*.

Note, that 'weights' means all weights and biases for all layers which
can have such values (e.g., convolutional layer, batch normalization layer,
etc.).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandleSource`** (input_control)  dl_model `→`  (handle)

Handle of the source deep learning model.

**`DLModelHandleTarget`** (input_control)  dl_model `→`  (handle)

Handle of the target deep learning model.

**`ChangesByLayer`** (output_control)  integer(-array) `→`  (integer)

Indicates for every target layer how many weights
changed.

## Result

If the parameters are valid, the operator `load_dl_model_weights`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Module

Deep Learning Professional
