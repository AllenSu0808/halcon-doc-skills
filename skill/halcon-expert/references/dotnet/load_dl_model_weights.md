# LoadDlModelWeights (Operator)

## Name

`LoadDlModelWeights` — Load the weights of a source model into a target model.

## Signature

`static void HOperatorSet.LoadDlModelWeights(HTuple DLModelHandleSource, HTuple DLModelHandleTarget, out HTuple changesByLayer)`

`HTuple HDlModel.LoadDlModelWeights(HDlModel DLModelHandleTarget)`

## Description

The operator `LoadDlModelWeights` loads weights of a source model
*`DLModelHandleSource`* into a target model *`DLModelHandleTarget`*.
Thereby applies for every layer in the target model: Its weights are only
changed if there is a layer in the source model having the same name and the
same weight-shape.
Note that *`DLModelHandleSource`* must be different from
*`DLModelHandleTarget`*, i.e., you cannot use the same model handle as
source and target.

*`changesByLayer`* is a tuple indicating for every target layer how many
weights changed.
Its entries are sorted by ascending layer IDs. The layer IDs can be queried
via the operator [`GetDlModelParam`](get_dl_model_param.md) with the parameter
*"summary"*.

Note, that 'weights' means all weights and biases for all layers which
can have such values (e.g., convolutional layer, batch normalization layer,
etc.).

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLModelHandleSource`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the source deep learning model.

**`DLModelHandleTarget`** (input_control)  dl_model `→` [HDlModel](HDlModel.md), [HTuple](HTuple.md) (*IntPtr*)

Handle of the target deep learning model.

**`changesByLayer`** (output_control)  integer(-array) `→` [HTuple](HTuple.md) (*int* / long)

Indicates for every target layer how many weights
changed.

## Result

If the parameters are valid, the operator `LoadDlModelWeights`
returns the value 2 (
H_MSG_TRUE)
. If necessary, an exception is raised.

## Module

Deep Learning Professional
