# get_dl_model_layer (Operator)

## Name

`get_dl_model_layer` — Create a deep copy of the layers and all
of their graph ancestors in a given deep learning model.

## Signature

`get_dl_model_layer( : : DLModelHandle, LayerNames : DLLayers)`

## Description

The operator `get_dl_model_layer` creates a deep copy of every layer
named in *`LayerNames`* and all their
graph ancestors in the deep learning model *`DLModelHandle`*.
You can retrieve the unique layer names using [`get_dl_model_param`](get_dl_model_param.md) with
its option *'summary'*.

You might use the output layers returned in *`DLLayers`* as inputs to
the `create_dl_layer_*` and [`create_dl_model`](create_dl_model.md) operators in order
to create novel model architectures based on existing models.

If you want to get multiple layers of a single model, these layers have to be
specified as a *`LayerNames`* tuple in a single call to
`get_dl_model_layer`. Doing so, you avoid multiple deep copies of graph
ancestors that are potentially shared by the layers.

*Example:*

|  |
| --- |
| `get_dl_model_layer(DLModelHandleOrig, ['layer_name_3', 'layer_name_6'], DLLayersOutput)` |
| [`create_dl_model([DLLayersOutput], DLModelHandle)`](create_dl_model.md) |

Please note, that the output layers are copies. They contain the same weights
and settings as in the given input model but they are unique copies.
You cannot alter the existing model by changing the output layers.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

This operator returns a handle. Note that the state of an instance of this handle type may be changed by specific operators even though the handle is used as an input parameter by those operators.

## Parameters

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Deep learning model.

**`LayerNames`** (input_control)  string(-array) `→`  (string)

Names of the layers to be copied.

**`DLLayers`** (output_control)  dl_layer(-array) `→`  (handle)

Copies of layers and all of their ancestors.

## Possible Predecessors

`read_dl_model`

## Possible Successors

`create_dl_model`,
`create_dl_layer_activation`,
`create_dl_layer_batch_normalization`,
`create_dl_layer_class_id_conversion`,
`create_dl_layer_class_id_conversion`,
`create_dl_layer_concat`,
`create_dl_layer_convolution`,
`create_dl_layer_dense`,
`create_dl_layer_depth_max`,
`create_dl_layer_dropout`,
`create_dl_layer_elementwise`,
`create_dl_layer_loss_cross_entropy`,
`create_dl_layer_loss_ctc`,
`create_dl_layer_loss_distance`,
`create_dl_layer_loss_focal`,
`create_dl_layer_loss_huber`,
`create_dl_layer_lrn`,
`create_dl_layer_pooling`,
`create_dl_layer_reduce`,
`create_dl_layer_reshape`,
`create_dl_layer_softmax`,
`create_dl_layer_transposed_convolution`,
`create_dl_layer_zoom_factor`,
`create_dl_layer_zoom_size`,
`create_dl_layer_zoom_to_layer_size`

## Module

Deep Learning Professional
