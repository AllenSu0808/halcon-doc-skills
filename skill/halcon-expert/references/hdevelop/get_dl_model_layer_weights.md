# get_dl_model_layer_weights (Operator)

## Name

`get_dl_model_layer_weights` — Get the weights (or values) of a Deep Learning model layer.

## Signature

`get_dl_model_layer_weights( : Weights : DLModelHandle, LayerName, WeightsType : )`

## Description

The operator `get_dl_model_layer_weights` returns in *`Weights`*
the values of a *`LayerName`* of the model *`DLModelHandle`*.

The parameter *`WeightsType`* determines which type of layer values are
retrieved.
The following values are supported for *`WeightsType`*:

- *'batchnorm_mean'*: Batch-wise calculated mean values to
  normalize the inputs. For further information, please refer to
  [`create_dl_layer_batch_normalization`](create_dl_layer_batch_normalization.md).

  Restriction:
   This value is only supported if the layer is of type
  *'batchnorm'*.
- *'batchnorm_mean_avg'*: Average of the batch-wise calculated
  mean values to normalize the inputs. For further information, please refer
  to [`create_dl_layer_batch_normalization`](create_dl_layer_batch_normalization.md).

  Restriction:
   This value is only supported if the layer is of type
  *'batchnorm'*.
- *'batchnorm_variance'*: Batch-wise calculated variance values to
  normalize the inputs. For further information, please refer to
  [`create_dl_layer_batch_normalization`](create_dl_layer_batch_normalization.md).

  Restriction:
   This value is only supported if the layer is of type
  *'batchnorm'*.
- *'batchnorm_variance_avg'*: Average of the batch-wise calculated
  variance values to normalize the inputs. For further information, please
  refer to [`create_dl_layer_batch_normalization`](create_dl_layer_batch_normalization.md).

  Restriction:
   This value is only supported if the layer is of type
  *'batchnorm'*.
- *'bias'*: Biases of the layer.
- *'bias_gradient'*: Gradients of the biases of the layer.
- *'bias_gradient_norm_l2'*: Gradients of the biases of the
  layer in terms of L2 norm.
- *'bias_norm_l2'*: Biases of the layer in terms of L2 norm.
- *'bias_update'*: Update of the biases of the layer.
  This is used in e.g., a solver which uses the last update.
- *'bias_update_norm_l2'*: Update of the biases of the layer
  in terms of L2 norm.
  This is used in a solver which uses the last update.
- *'weights'*: Weights of the layer.
- *'weights_gradient'*: Gradients of the weights of the layer.
- *'weights_gradient_norm_l2'*: Gradients of the weights of the
  layer in terms of L2 norm.
- *'weights_norm_l2'*: Weights of the layer in terms of L2 norm.
- *'weights_update'*: Update of the weights of the layer.
  This is used in a solver which uses the last update.
- *'weights_update_norm_l2'*: Update of the weights of the layer
  in terms of L2 norm.
  This is used in a solver which uses the last update.

The following tables give an overview, which parameters for *`WeightsType`*
can be set using [`set_dl_model_layer_weights`](set_dl_model_layer_weights.md) and which ones can be retrieved
using `get_dl_model_layer_weights`.

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'batchnorm_mean'* | `x` | `x` |
| *'batchnorm_mean_avg'* | `x` | `x` |
| *'batchnorm_variance'* | `x` | `x` |
| *'batchnorm_variance_avg'* | `x` | `x` |
| *'bias'* | `x` | `x` |
| *'bias_gradient'* |  | `x` |
| *'bias_gradient_norm_l2'* |  | `x` |
| *'bias_norm_l2'* |  | `x` |
| *'bias_update'* |  | `x` |
| *'bias_update_norm_l2'* |  | `x` |
| *'weights'* | `x` | `x` |
| *'weights_gradient'* |  | `x` |
| *'weights_gradient_norm_l2'* |  | `x` |
| *'weights_norm_l2'* |  | `x` |
| *'weights_update'* |  | `x` |
| *'weights_update_norm_l2'* |  | `x` |

## Attention

The operator `get_dl_model_layer_weights` is only applicable to self-created
networks. For networks delivered by HALCON, the operator returns an
empty tuple.

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`Weights`** (output_object)  image(-array) `→` object (real)

Output weights.

**`DLModelHandle`** (input_control)  dl_model `→`  (handle)

Handle of the deep learning model.

**`LayerName`** (input_control)  string `→`  (string)

Name of the layer to be queried.

**`WeightsType`** (input_control)  string `→`  (string)

Selected type of layer values to be returned.

Default:
'weights'

List of values:
'batchnorm_mean', 'batchnorm_mean_avg', 'batchnorm_variance', 'batchnorm_variance_avg', 'bias', 'bias_gradient', 'bias_gradient_norm_l2', 'bias_norm_l2', 'bias_update', 'bias_update_norm_l2', 'weights', 'weights_gradient', 'weights_gradient_norm_l2', 'weights_norm_l2', 'weights_update', 'weights_update_norm_l2'

## Example (HDevelop)

```
set_system ('seed_rand', 42)
* Create a small model network.
create_dl_layer_input ('input', [InputImageSize[0],InputImageSize[1],1], [],\
                       [], DLGraphNodeInput)
create_dl_layer_convolution (DLGraphNodeInput, 'conv', 3, 1, 1, 2, 1, 'none',\
                             'none', [], [], DLGraphNodeConvolution)
create_dl_layer_activation (DLGraphNodeConvolution, 'relu', 'relu', [], [],\
                            DLGraphNodeActivation)
create_dl_layer_dense (DLGraphNodeActivation, 'dense', 3, [], [],\
                       DLGraphNodeDense)
create_dl_layer_softmax (DLGraphNodeDense, 'softmax', [], [],\
                          DLGraphNodeSoftMax)
create_dl_model (DLGraphNodeSoftMax, DLModelHandle)
*
set_dl_model_param (DLModelHandle, 'type', 'classification')
set_dl_model_param (DLModelHandle, 'batch_size', 1)
set_dl_model_param (DLModelHandle, 'runtime', 'gpu')
set_dl_model_param (DLModelHandle, 'runtime_init', 'immediately')
*
* Train for 5 iterations.
for TrainIterations := 1 to NumTrainIterations by 1
    train_dl_model_batch (DLModelHandle, DLSample, DLTrainResult)
endfor
*
* Get the gradients, weights, and activations.
get_dl_model_layer_gradients (GradientsSoftmax, DLModelHandle, 'softmax')
get_dl_model_layer_gradients (GradientsDense, DLModelHandle, 'dense')
get_dl_model_layer_gradients (GradientsConv, DLModelHandle, 'conv')
*
get_dl_model_layer_weights (WeightsDense, DLModelHandle, 'dense',\
                      'weights_gradient')
get_dl_model_layer_weights (WeightsConv, DLModelHandle, 'conv',\
                      'weights_gradient')
*
get_dl_model_layer_activations (ActivationsDense,  DLModelHandle, 'dense')
get_dl_model_layer_activations (ActivationsConv,  DLModelHandle, 'conv')
```

## Possible Predecessors

`create_dl_model`,
`train_dl_model_batch`,
`set_dl_model_layer_weights`

## Possible Successors

`set_dl_model_layer_weights`

## Alternatives

`get_dl_model_layer_activations`,
`get_dl_model_layer_gradients`

## Module

Foundation. This operator uses dynamic licensing (see the 'Installation Guide'). Which of the following modules is required depends on the specific usage of the operator:  
Deep Learning Professional
