# set_dl_model_layer_weights (Operator)

## Name

`set_dl_model_layer_weights` — Set the weights (or values) of a Deep Learning model layer.

## Signature

`set_dl_model_layer_weights(Weights : : DLModelHandle, LayerName, WeightsType : )`

## Description

The operator `set_dl_model_layer_weights` sets for the model
*`DLModelHandle`* the given *`Weights`* in the specified
*`LayerName`*.

The parameter *`WeightsType`* determines which type of layer values
are set.
Which values can be set, please refer to the [`get_dl_model_layer_weights`](get_dl_model_layer_weights.md)
documentation.

## Attention

The operator `set_dl_model_layer_weights` is only applicable to self-created
networks. For networks delivered by HALCON, the operator does have no impact.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Weights`** (input_object)  (multichannel-)image(-array) `→` object (real)

Input weights.

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Handle of the deep learning model.

**`LayerName`** (input_control)  string `→`  (string)

Name of the layer, whose weights are to be set.

**`WeightsType`** (input_control)  string `→`  (string)

Selected type of layer values to be set.

Default:
'weights'

List of values:
'batchnorm_mean', 'batchnorm_mean_avg', 'batchnorm_variance', 'batchnorm_variance_avg', 'bias', 'weights'

## Example (HDevelop)

```
* Create weights for a convolution layer.
gen_image_const (Weights, 'real', 1, 1)
paint_region (Weights, Weights, Weights, 1, 'fill')
gen_empty_obj (WeightsArray)
for Index := 0 to 10 by 1
    concat_obj (WeightsArray, Weights, WeightsArray)
endfor
*
* Input image with rows consisting of 1s to 10s.
gen_image_const (Image, 'real', 10, 10)
for Index := 0 to 9 by 1
    gen_rectangle1 (Rectangle, Index, 0, Index, 9)
    paint_region (Rectangle, Image, Image, Index + 1, 'fill')
endfor
*
* Create a small model network.
create_dl_layer_input ('image', [10, 2, 1], [], [], ImageNode)
create_dl_layer_convolution (ImageNode, 'conv', 1, 1, 2, 11, 1, 'none', \
                             'none', [], [], ConvNode)
create_dl_layer_zoom_factor (ConvNode, 'zoom', 2, 2, 'bilinear', 'true', [],\
                             [], ZoomNode)
create_dl_model (ZoomNode, DLModelHandle)
set_dl_model_param (DLModelHandle, 'runtime', 'cpu')
*
* Set the weights to the convolution layer.
set_dl_model_layer_weights (WeightsArray, DLModelHandle, 'conv', 'weights')
```

## Possible Predecessors

`create_dl_model`,
`get_dl_model_layer_weights`

## Possible Successors

`get_dl_model_layer_weights`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
Deep Learning Professional
