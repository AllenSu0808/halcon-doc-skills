# create_dl_layer_softmax (Operator)

## Name

`create_dl_layer_softmax` — Create a softmax layer.

## Signature

`def create_dl_layer_softmax(dllayer_input: HHandle, layer_name: str, gen_param_name: MaybeSequence[str], gen_param_value: MaybeSequence[Union[int, float, str]]) -> HHandle`

## Description

The operator `create_dl_layer_softmax` creates a softmax layer whose
handle is returned in *`dllayer_soft_max`*.

The parameter *`dllayer_input`* determines the feeding input layer and
expects the layer handle as value.

The parameter *`layer_name`* sets an individual layer name.
Note that if creating a model using [`create_dl_model`](create_dl_model.md) each layer of
the created network must have a unique name.

The softmax layer applies the softmax function which is defined for each input
$x_{i}$ as follows:
$$Softmax(x_i) = \frac{\exp(x_i)}{\sum_{j=0}^{N-1} \exp(x_j)}$$ ![figure](../assets/19c685431d9ee439.svg)
where $N$ is the number of inputs. During training, the result of the
softmax function is transformed by a logarithm
function, such that the values are suitable as input to e.g., a cross
entropy loss layer.
This behavior can be changed by setting the generic parameter
*"output_mode"*, see below.

The following generic parameters *`gen_param_name`* and the corresponding
values *`gen_param_value`* are supported:

- ***"output_mode"*:** —

  This parameter determines if and in which case the output is transformed
  by a logarithm function:

  - *"default"*: During inference, the result of the softmax
    function is returned as output while during training, the softmax is
    further transformed by a logarithm function.
  - *"no_log_training"*: During training the result of the
    softmax function is not transformed by a logarithm function.
  - *"log_inference"*: The logarithm of the softmax is
    calculated during inference in the same way as during training.

  Default:
   *"default"*.
- ***"is_inference_output"*:** —

  Determines whether [`apply_dl_model`](apply_dl_model.md) will include the output of this
  layer in the dictionary `dlresult_batch` even without specifying this
  layer in `outputs` (*"true"*) or not (*"false"*).

  Default:
   *"false"*

Certain parameters of layers created using this operator
`create_dl_layer_softmax` can be set and retrieved using
further operators.
The following tables give an overview, which parameters can be set
using [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and which ones can be retrieved
using [`get_dl_model_layer_param`](get_dl_model_layer_param.md) or [`get_dl_layer_param`](get_dl_layer_param.md). Note, the
operators [`set_dl_model_layer_param`](set_dl_model_layer_param.md) and [`get_dl_model_layer_param`](get_dl_model_layer_param.md)
require a model created by [`create_dl_model`](create_dl_model.md).

| Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"input_layer"* (*`dllayer_input`*) |  | `x` |
| *"name"* (*`layer_name`*) | `x` | `x` |
| *"output_layer"* (*`dllayer_soft_max`*) |  | `x` |
| *"shape"* |  | `x` |
| *"type"* |  | `x` |

| Generic Layer Parameters | `set` | `get` |
| --- | --- | --- |
| *"is_inference_output"* | `x` | `x` |
| *"num_trainable_params"* |  | `x` |
| *"output_mode"* |  | `x` |

## Execution Information

- Multithreading type: reentrant (runs in parallel with non-exclusive operators).
- Multithreading scope: global (may be called from any thread).
- Processed without parallelization.

## Parameters

**`dllayer_input`** (input_control)  dl_layer `→` HHandle

Feeding layer.

**`layer_name`** (input_control)  string `→` str

Name of the output layer.

**`gen_param_name`** (input_control)  attribute.name(-array) `→` MaybeSequence[str]

Generic input parameter names.

Default:
[]

List of values:
"is_inference_output", "output_mode"

**`gen_param_value`** (input_control)  attribute.value(-array) `→` MaybeSequence[Union[int, float, str]]

Generic input parameter values.

Default:
[]

Suggested values:
"default", "no_log_training", "log_inference", "true", "false"

**`dllayer_soft_max`** (output_control)  dl_layer `→` HHandle

Softmax layer.

## Module

Deep Learning Professional
