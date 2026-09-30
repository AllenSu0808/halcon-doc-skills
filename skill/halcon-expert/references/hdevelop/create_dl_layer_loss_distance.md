# create_dl_layer_loss_distance (Operator)

## Name

`create_dl_layer_loss_distance` — Create a distance loss layer.

## Signature

`create_dl_layer_loss_distance( : : DLLayerInput, DLLayerTarget, DLLayerWeights, LayerName, DistanceType, LossWeight, GenParamName, GenParamValue : DLLayerLossDistance)`

## Description

The operator `create_dl_layer_loss_distance` creates a distance loss
layer whose handle is returned in *`DLLayerLossDistance`*.

This layer expects multiple layers as input:

- *`DLLayerInput`*: Specifies the
  prediction (e.g., a softmax layer).
- *`DLLayerTarget`*: Specifies the
  target sequences (originating from the ground truth information).
- *`DLLayerWeights`*: Specifies the weight sequences. This parameter
  is optional. If an empty tuple *[]* is passed for all values the
  weighting factor *1.0* is used.

The parameter *`LayerName`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`LossWeight`* is an overall loss weight if there are
multiple losses in the network.

The parameter *`DistanceType`* determines which distance measure is
applied. Currently, *'l2'* and *'l1'* are implemented.
Depending on the generic parameter *'reduce'* this results in

- L2 loss distance as a tensor:
  $$DLLayerLossDistance[i] = 0.5·LossWeight·DLLayerWeights[i]·(DLLayerInput[i] - DLLayerTarget[i])^2$$ ![figure](../assets/b88523fa6b138efc.svg)
  in this case loss is the tensor of the same size as *`DLLayerInput`*.
- L2 loss distance as a scalar:
  $$DLayerLossDistance = \frac{\sum_{i=0}^{N-1} DLIayerLossDistance[i]}{\sum_{i=0}^{N-1} DLILayerWeights[i]}$$ ![figure](../assets/bb320885b2b7de3b.svg)
  where $N$ is a number of elements in *`DLLayerInput`*.
- L1 loss distance as a tensor:
  $$DLLayerLossDistance[i] = LossWeight · DLLayerWeights[i] · |DLLayerInput[i] − DLLayerTarget[i]|$$ ![figure](../assets/f894d131ceef625b.svg)
  in this case loss is the tensor of the same size as *`DLLayerInput`*.
- L1 loss distance as a scalar:
  $$DLayerLossDistance = \frac{\sum_{i=0}^{N-1} DLIayerLossDistance[i]}{\sum_{i=0}^{N-1} DLILayerWeights[i]}$$ ![figure](../assets/bb320885b2b7de3b.svg)
  where $N$ is a number of elements in *`DLLayerInput`*.

Thus *`DLLayerInput`*, *`DLLayerTarget`* and
*`DLLayerWeights`* should have the same size. Setting the weights in
*`DLLayerWeights`* to *1* will result in a loss normalized over
the number of elements.

The following generic parameters *`GenParamName`* and the corresponding
values *`GenParamValue`* are supported:

- ***'is_inference_output'*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `DLResultBatch` even without specifying this
  layer in `Outputs` (*'true'*) or not (*'false'*).

  Default:
   *'false'*
- ***'reduce'*:** —

  Determines whether the output of the layer is reduced:

  - *'true'*: The output is reduced to a scalar.
  - *'false'*: The output of the layer is a tensor, where each
    element is a 'per-pixel' loss (squared differences).

  Default:
   *'true'*.

Certain parameters of layers created using this operator
`create_dl_layer_loss_distance` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'input_layer'* (*`DLLayerInput`*, *`DLLayerTarget`*, and/or *`DLLayerWeights`*) |  | `x` |
| *'loss_weight'* (*`LossWeight`*) | `x` | `x` |
| *'name'* (*`LayerName`*) | `x` | `x` |
| *'output_layer'* (*`DLLayerLossDistance`*) |  | `x` |
| *'shape'* |  | `x` |
| *'type'* |  | `x` |
| *'distance_type'* (*`DistanceType`*) |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *'is_inference_output'* | `x` | `x` |
| *'num_trainable_params'* |  | `x` |
| *'reduce'* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`DLLayerInput`** (input_control)  dl_layer `→`  (handle)

Input layer.

**`DLLayerTarget`** (input_control)  dl_layer `→`  (handle)

Target layer.

**`DLLayerWeights`** (input_control)  dl_layer `→`  (handle)

Weights layer.

**`LayerName`** (input_control)  string `→`  (string)

Name of the output layer.

**`DistanceType`** (input_control)  string `→`  (string)

Type of distance.

Default:
'l2'

List of values:
'l1', 'l2'

**`LossWeight`** (input_control)  number `→`  (real)

Loss weight. Applies to all losses, if several losses
occur in the network.

Default:
1.0

**`GenParamName`** (input_control)  attribute.name(-array) `→`  (string)

Generic input parameter names.

Default:
[]

List of values:
'is_inference_output', 'reduce'

**`GenParamValue`** (input_control)  attribute.value(-array) `→`  (string)

Generic input parameter values.

Default:
[]

Suggested values:
'true', 'false'

**`DLLayerLossDistance`** (output_control)  dl_layer `→`  (handle)

Distance loss layer.

## Module

Deep Learning Professional
