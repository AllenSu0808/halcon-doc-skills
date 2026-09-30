# get_dl_model_layer_activations (Operator)

## Name

`get_dl_model_layer_activations` — Get the activations of a Deep Learning model layer.

## Signature

`get_dl_model_layer_activations( : Activations : DLModelHandle, LayerName : )`

## Description

The operator `get_dl_model_layer_activations` returns in *`Activations`*
the activations of the specified *`LayerName`* of the model
*`DLModelHandle`*.

*`Activations`* is a tuple of `batch_size` many objects,
where every object is an image having the size
(`width`, `height`, `depth`) of the given *`LayerName`*.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Activations`** (output_object)  image(-array) `→` object (real)

Output activations.

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Handle of the deep learning model.

**`LayerName`** (input_control)  string `→`  (string)

Name of the layer to be queried.

## Module

Deep Learning Professional
