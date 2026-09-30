# create_dl_layer_loss_distance (Operator)

## Name

`create_dl_layer_loss_distance` — Create a distance loss layer.

## Signature

`def create_dl_layer_loss_distance(dllayer_input: HHandle, dllayer_target: HHandle, dllayer_weights: HHandle, layer_name: str, distance_type: str, loss_weight: float, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[str]) -> HHandle`

## Description

The operator `create_dl_layer_loss_distance` creates a distance loss
layer whose handle is returned in *`dllayer_loss_distance`*.

This layer expects multiple layers as input:

- *`dllayer_input`*: Specifies the
  prediction (e.g., a softmax layer).
- *`dllayer_target`*: Specifies the
  target sequences (originating from the ground truth information).
- *`dllayer_weights`*: Specifies the weight sequences. This parameter
  is optional. If an empty tuple *[]* is passed for all values the
  weighting factor *1.0* is used.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The parameter *`loss_weight`* is an overall loss weight if there are
multiple losses in the network.

The parameter *`distance_type`* determines which distance measure is
applied. Currently, *"l2"* and *"l1"* are implemented.
Depending on the generic parameter *"reduce"* this results in

- L2 loss distance as a tensor:
  $$DLLayerLossDistance[i] = 0.5·LossWeight·DLLayerWeights[i]·(DLLayerInput[i] - DLLayerTarget[i])^2$$ ![figure](../assets/b88523fa6b138efc.svg)
  in this case loss is the tensor of the same size as *`dllayer_input`*.
- L2 loss distance as a scalar:
  $$DLayerLossDistance = \frac{\sum_{i=0}^{N-1} DLIayerLossDistance[i]}{\sum_{i=0}^{N-1} DLILayerWeights[i]}$$ ![figure](../assets/bb320885b2b7de3b.svg)
  where $N$ is a number of elements in *`dllayer_input`*.
- L1 loss distance as a tensor:
  $$DLLayerLossDistance[i] = LossWeight · DLLayerWeights[i] · |DLLayerInput[i] − DLLayerTarget[i]|$$ ![figure](../assets/f894d131ceef625b.svg)
  in this case loss is the tensor of the same size as *`dllayer_input`*.
- L1 loss distance as a scalar:
  $$DLayerLossDistance = \frac{\sum_{i=0}^{N-1} DLIayerLossDistance[i]}{\sum_{i=0}^{N-1} DLILayerWeights[i]}$$ ![figure](../assets/bb320885b2b7de3b.svg)
  where $N$ is a number of elements in *`dllayer_input`*.

Thus *`dllayer_input`*, *`dllayer_target`* and
*`dllayer_weights`* should have the same size. Setting the weights in
*`dllayer_weights`* to *1* will result in a loss normalized over
the number of elements.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*
- ***"reduce"*:** —

  Determines whether the output of the layer is reduced:

  - *"true"*: The output is reduced to a scalar.
  - *"false"*: The output of the layer is a tensor, where each
    element is a 'per-pixel' loss (squared differences).

  Default:
   *"true"*.

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
| *"input_layer"* (*`dllayer_input`*, *`dllayer_target`*, and/or *`dllayer_weights`*) |  | `x` |
| *"loss_weight"* (*`loss_weight`*) | `x` | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_loss_distance`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |
| *"distance_type"* (*`distance_type`*) |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"reduce"* | `x` | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Input layer.

**`dllayer_target`** (input_control)  dl_layer `→` HHandle

Target layer.

**`dllayer_weights`** (input_control)  dl_layer `→` HHandle

Weights layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`distance_type`** (input_control)  string `→` str

Type of distance.

Default:
"l2"

List of values:
"l1", "l2"

**`loss_weight`** (input_control)  number `→` float

Loss weight. Applies to all losses, if several losses
occur in the network.

Default:
1.0

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output", "reduce"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[str]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`dllayer_loss_distance`** (output_control)  dl_layer `→` HHandle

Distance loss layer.

## Module

Deep Learning Professional
