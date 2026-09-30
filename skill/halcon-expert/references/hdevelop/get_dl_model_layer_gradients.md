# get_dl_model_layer_gradients (Operator)

## Name

`get_dl_model_layer_gradients` — Get the gradients of a Deep Learning model layer.

## Signature

`get_dl_model_layer_gradients( : Gradients : DLModelHandle, LayerName : )`

## Description

The operator `get_dl_model_layer_gradients` returns in *`Gradients`* the
gradients of the specified *`LayerName`* of the model
*`DLModelHandle`*.

*`Gradients`* is a tuple of `batch_size` many objects,
where every object is an image having the size
(`width`, `height`, `depth`) of the given *`LayerName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Gradients`** (output_object)  image(-array) `→` object (real)

Output gradients.

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Handle of the deep learning model.

**`LayerName`** (input_control)  string `→`  (string)

Name of the layer to be queried.

## Module

Deep Learning Professional
