# get_dl_model_layer_gradients (Operator)

## Name

`get_dl_model_layer_gradients` — Get the gradients of a Deep Learning model layer.

## Signature

`def get_dl_model_layer_gradients(dlmodel_handle: HHandle, layer_name: str) -> HObject`

## Description

The operator `get_dl_model_layer_gradients` returns in *`gradients`* the
gradients of the specified *`layer_name`* of the model
*`dlmodel_handle`*.

*`gradients`* is a tuple of `batch_size` many objects,
where every object is an image having the size
(`width`, `height`, `depth`) of the given *`layer_name`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`gradients`** (output_object)  image(-array) `→` HObject (real)

Output gradients.

**`dlmodel_handle`** (input_control)  dl_model `→` HHandle

Handle of the deep learning model.

**`layer_name`** (input_control)  string `→` str

Name of the layer to be queried.

## Module

Deep Learning Professional
