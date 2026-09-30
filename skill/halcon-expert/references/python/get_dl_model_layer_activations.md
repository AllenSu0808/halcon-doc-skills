# get_dl_model_layer_activations (Operator)

## Name

`get_dl_model_layer_activations` — Get the activations of a Deep Learning model layer.

## Signature

`def get_dl_model_layer_activations(dlmodel_handle: HHandle, layer_name: str) -> HObject`

## Description

The operator `get_dl_model_layer_activations` returns in *`activations`*
the activations of the specified *`layer_name`* of the model
*`dlmodel_handle`*.

*`activations`* is a tuple of `batch_size` many objects,
where every object is an image having the size
(`width`, `height`, `depth`) of the given *`layer_name`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`activations`** (output_object)  image(-array) `→` HObject (real)

Output activations.

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Handle of the deep learning model.

**`layer_name`** (input_control)  string `→` str

Name of the layer to be queried.

## Module

Deep Learning Professional
