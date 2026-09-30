# create_dl_layer_loss_huber (Operator)

## Name

`create_dl_layer_loss_huber` — Create a Huber loss layer.

## Signature

`def create_dl_layer_loss_huber(dllayer_input: HHandle, dllayer_target: HHandle, dllayer_weights: HHandle, dllayer_normalization: HHandle, layer_name: str, loss_weight: float, beta: float, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_loss_huber` creates a Huber loss layer
whose handle is returned in *`dllayer_loss_huber`*.
The Huber loss is defined by
$$L_{Huber}(x,t,w,n) := \frac{\alpha}{n}\sum_{i=0}^{N-1} w_i l(x_i - t_i),\quad with\\ l(y) := \begin{cases} 0.5 y^2 / \beta & \text{if } |y| < \beta \\ |y| - 0.5 \beta & \text{else.} \\ \end{cases}$$ ![figure](../assets/e38e3d33c8726ec5.svg)

This layer expects multiple layers as input:

- *`dllayer_input`*: Specifies $x$
  (usually a softmax layer).
- *`dllayer_target`*: Specifies the
  targets $t$.
- *`dllayer_weights`*: Specifies the
  weights $w$.

The underlying data tensors are assumed to be of the same shape with
a total number of $N$ elements.

The parameter *`dllayer_normalization`* can be used to determine the
normalization factor $n$. If *`dllayer_normalization`* is set to an
empty tuple, the sum over all weights is used for the normalization
$n$.

The parameter *`loss_weight`* determines the scalar weight factor
$\alpha$.

The parameter *`beta`* sets the value for $\beta$ in the
formula.
If *`beta`* is set to *0*, the Huber loss is equal to an L1-loss.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_loss_huber` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md).
Note, the operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and
[`get_dl_model_layer_param`](get_dl_model_layer_param.md) require a model created by
[`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"beta"* (*`beta`*) | `x` | `x` |
| *"input_layer"* (*`dllayer_input`*, *`dllayer_target`*, *`dllayer_weights`*, and/or *`dllayer_normalization`*) |  | `x` |
| *"loss_weight"* (*`loss_weight`*) | `x` | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_loss_huber`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |

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

**`dllayer_normalization`** (input_control)  dl_layer `→` HHandle

Normalization layer.

Default:
[]

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`loss_weight`** (input_control)  number `→` float

Scalar weight factor.

Default:
1.0

**`beta`** (input_control)  number `→` float

Beta value in the loss-defining formula.

Default:
1.1

Restriction:
`Beta >= 0`

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"true", "false"

**`dllayer_loss_huber`** (output_control)  dl_layer `→` HHandle

Huber loss layer.

## Module

Deep Learning Professional
