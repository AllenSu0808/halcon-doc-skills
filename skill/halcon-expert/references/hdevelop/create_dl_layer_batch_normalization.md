# create_dl_layer_batch_normalization (Operator)

## Name

`create_dl_layer_batch_normalization` — Create a batch normalization layer.

## Signature

`create_dl_layer_batch_normalization( : : DLLayerInput, LayerName, Momentum, Epsilon, Activation, GenParamName, GenParamValue : DLLayerBatchNorm)`

## Description

The operator `create_dl_layer_batch_normalization` creates a batch
normalization layer whose handle is returned in *`DLLayerBatchNorm`*.
Batch normalization is used to improve the performance and stability of a
neural network during training.
The mean and variance of each input activation are calculated for each batch
and the input values are transformed to have zero mean and unit variance.
Moreover, a linear scale and shift transformation is learned. During training,
to take all samples into account, the batch-wise calculated mean
and variance values are combined with a *`Momentum`* into running mean
and running variance, where $i$ denotes the iteration index:
$$running_mean(i) = (1 - Momentum) * mean(i) + Momentum * running_mean(i - 1),\nrunning_variance(i) = (1 - Momentum) * variance(i) + Momentum * running_variance(i - 1).$$ ![figure](../assets/06bc7f12a9101de0.svg)
To affect the mean and variance values you can set the following options
for *`Momentum`*:

- **Given number:** —

  For example: *0.9*. This is the default and recommended option.

  Restriction:
   *0* $\le$ *`Momentum`* $<$ *1*
- ***'auto'*:** —

  Combines mean and variance values by a
  cumulative moving average. This is only recommended in case the parameters of all previous
  layers in the network are frozen, i.e., have a learning rate of *0*.
- ***'freeze'*:** —

  Stops the adjustment of the mean and
  variance and their values stay fixed. In this case, the mean and variance are used
  during training for normalizing a batch, analogously to how the batch normalization
  operates during inference. The parameters of the linear scale and shift
  transformation, however, remain learnable.

*`Epsilon`* is a small offset to the variance and
used to control the numerical stability. Usually its default value should be
adequate.

The parameter *`DLLayerInput`* determines the feeding input layer.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`Activation`* determines whether an activation is
performed after the batch normalization in order to optimize the runtime
performance.

- *'relu'*: perform a ReLU activation after the batch
  normalization.

  It is possible to specify an upper bound to the ReLU operation
  (see [`create_dl_layer_activation`](create_dl_layer_activation.md)) via the generic parameter
  *'upper_bound'*.
- *'none'*: no activation operation is performed.

It is not possible to specify a leaky ReLU, sigmoid or tanh activation
function.
Use [`create_dl_layer_activation`](create_dl_layer_activation.md) instead.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'bias_filler'*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *'xavier'*, *'msra'*,
  *'const'*.

  Default:
   *'const'*
- ***'bias_filler_const_val'*:** —

  Constant value.

  Restriction:
   *'bias_filler'* must be set to
  *'const'*.

  Default:
   *0*
- ***'bias_filler_variance_norm'*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *'norm_out'*, *'norm_in'*,
  *'norm_average'*, or constant value (in combination with
  *'bias_filler'* = *'msra'*).

  Default:
   *'norm_in'*
- ***'bias_term'*:** —

  Determines whether the created
  batch normalization layer has a bias term (*'true'*) or not
  (*'false'*).

  Default:
   *'true'*
- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*
- ***'learning_rate_multiplier'*:** —

  Multiplier for the learning
  rate for this layer that is used during training.
  If *'learning_rate_multiplier'* is set to *0.0*, the layer is
  skipped during training.

  Default:
   *1.0*
- ***'learning_rate_multiplier_bias'*:** —

  Multiplier for the
  learning rate of the bias term. The total bias learning rate is the
  product of *'learning_rate_multiplier_bias'* and
  *'learning_rate_multiplier'*.

  Default:
   *1.0*
- ***'upper_bound'*:** —

  Float value defining an upper bound
  for a rectified linear unit.
  If the activation layer is part of a model, which has been created using
  [`create_dl_model`](create_dl_model.md), the upper bound can be unset. To do so, use
  [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and set an empty tuple for
  *'upper_bound'*.

  Default:
   *[]*
- ***'weight_filler'*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *'xavier'*, *'msra'*,
  *'const'*.

  Default:
   *'const'*
- ***'weight_filler_const_val'*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  Default:
   *1.0*
- ***'weight_filler_variance_norm'*:** —

  See [`create_dl_layer_convolution`](create_dl_layer_convolution.md) for a detailed explanation of
  this parameter and its values.

  List of values:
   *'norm_in'*, *'norm_out'*,
  *'norm_average'*, or constant value (in combination with
  *'weight_filler'* = *'msra'*).

  Default:
   *'norm_in'*

Certain parameters of layers created using this operator
`create_dl_layer_batch_normalization` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'activation_mode'* (*`Activation`*) |  | `x` |
| *'epsilon'* (*`Epsilon`*) |  | `x` |
| *'input_layer'* (*`DLLayerInput`*) |  | `x` |
| *'momentum'* (*`Momentum`*) | `x` | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerBatchNorm`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'bias_filler'* | `x` | `x` |
| *'bias_filler_const_val'* | `x` | `x` |
| *'bias_filler_variance_norm'* | `x` | `x` |
| *'bias_term'* |  | `x` |
| *'is_inference_output'* | `x` | `x` |
| *'learning_rate_multiplier'* | `x` | `x` |
| *'learning_rate_multiplier_bias'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |
| *'upper_bound'* | `x` | `x` |
| *'weight_filler'* | `x` | `x` |
| *'weight_filler_const_val'* | `x` | `x` |
| *'weight_filler_variance_norm'* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Feeding layer.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`Momentum`** (input_control)  string `→`  (string / real)

Momentum.

Default:
0.9

List of values:
0.9, 0.99, 0.999, 'auto', 'freeze'

**`Epsilon`** (input_control)  number `→`  (real)

Variance offset.

Default:
0.0001

**`Activation`** (input_control)  string `→`  (string)

Optional activation function.

Default:
'none'

List of values:
'none', 'relu'

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'bias_filler', 'bias_filler_const_val', 'bias_filler_variance_norm', 'bias_term', 'is_inference_output', 'learning_rate_multiplier', 'learning_rate_multiplier_bias', 'upper_bound', 'weight_filler', 'weight_filler_const_val', 'weight_filler_variance_norm'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string / integer / real)

Generic input parameter values.

Default:
[]

Suggested values:
'xavier', 'msra', 'const', 'nearest_neighbor', 'bilinear', 'norm_in', 'norm_out', 'norm_average', 'true', 'false', 1.0, 0.9, 0.0

**`DLLayerBatchNorm`** (output_control)  dl_layer `→`  (handle)

Batch normalization layer.

## Example (HDevelop)

```
create_dl_layer_input ('input', [224,224,3], [], [], DLLayerInput)
* In practice, one typically sets ['bias_term'], ['false'] for a convolution
* that is directly followed by a batch normalization layer.
create_dl_layer_convolution (DLLayerInput, 'conv1', 3, 1, 1, 64, 1, \
                             'none', 'none', ['bias_term'], ['false'], \
                             DLLayerConvolution)
create_dl_layer_batch_normalization (DLLayerConvolution, 'bn1', 0.9, \
                                     0.0001, 'none', [], [], \
                                     DLLayerBatchNorm)
```

## Possible Predecessors

`create_dl_layer_convolution`

## Possible Successors

`create_dl_layer_activation`,
`create_dl_layer_convolution`

## References

Sergey Ioffe and Christian Szegedy,
"Batch Normalization: Accelerating Deep Network Training by Reducing Internal
Covariate Shift,"
Proceedings of the 32nd International Conference on Machine Learning,
(ICML) 2015, Lille, France, 6-11 July 2015, pp. 448--456

## Module

Deep Learning Professional
